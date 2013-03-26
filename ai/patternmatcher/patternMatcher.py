"""
PatternMatcher assignment
Joe Gibson
2-13-13
Artificial Intelligence at Olin College

Implementation of a simple chat bot using AI techniques from the original Eliza bot.
Uses regular expressions to match an appropriate response to the input.

NOTE: I chose to use Python for this assignment because it presented a great opportunity
for me to experiment with and learn about regular expressions.

EXAMPLE CHAT:

            Hi, my name is Eliza^2!
Hi Eliza, how are you?
            Fine, how are you?
I am sad today.
            Why are you sad today?
Your friend is being mean to me.
            Why is my friend being mean to you?
Because I like dogs.
            Why do you like dogs?
Why are you asking me so many questions?
            Because...
You are being annoying...
            Sorry I didn't understand that.


"""


import re
import random

def main():
	"""
	Runs the while loop used for interacting with the chat bot.
	Takes input and finds appropriate response in each loop.
	"""
	res = "            %s"
	print res % "Hi, my name is Eliza^2!"
	while True:
		text = raw_input()
		for pat in patterns:
			match = pat[0].search(text)
			if match:
				if len(match.groups()) == 1:
					response = random.choice(pat[1]) % replaceAll(match.groups()[0])
				elif len(match.groups()) == 2:
					response = random.choice(pat[1]) % (replaceAll(match.groups()[0]), replaceAll(match.groups()[1]))
				else:
					response = random.choice(pat[1])
				break
		if not match:
			response = "Sorry I didn't understand that."
		print res % response

def replaceAll(string):
	"""
	Takes a string and replaces all occurences of subject specific grammar with the appropriate form.
	"""
	for i in range(len(replacePats)):
		rep = replacePats[i]
		if re.search(rep[0][0], string):
			string = re.sub(rep[0][0], rep[0][1], string)
		else:
			string = re.sub(rep[1][0], rep[1][1], string)
	return string

if __name__ == "__main__":

	# Patterns used for replacing subject specific grammar.
	replacePats = [
		((r"(^|\s)[Mm]e(\s|$)", r"\1you\2"), (r"(^|\s)[Yy]ou(\s|$)", r"\1me\2")),
		((r"(^|\s)[Mm]y(\s|$)", r"\1your\2"), (r"(^|\s)[Yy]our(\s|$)", r"\1my\2")),
		((r"(^|\s)[Mm]ine(\s|$)", r"\1yours\2"), (r"(^|\s)[Yy]ours(\s|$)", r"\1mine\2")),
	]

	# Patterns used for determining the appropriate response.
	patterns = [
		(re.compile(r"how are you",re.IGNORECASE), ["Fine, how are you?"]),
		(re.compile(r"Hello",re.IGNORECASE), ["Hello.", "Hi!"]),
		(re.compile(r"Hi",re.IGNORECASE), ["Hello.", "Hi!"]),
		(re.compile(r"Hey",re.IGNORECASE), ["Hello.", "Hi!"]),
		(re.compile(r"why",re.IGNORECASE), ["Because...", "Google it."]),
		(re.compile(r"but",re.IGNORECASE), ["No buts!"]),
		(re.compile(r"I like ([a-z][^\.!?]*)",re.IGNORECASE), ["Why do you like %s?", "What is your favorite thing about %s?"]),
		(re.compile(r"I am ([a-z][^\.!?]*)",re.IGNORECASE), ["Why are you %s?"]),
		(re.compile(r"([a-z ]*) is ([a-z ][^\.!?]*)",re.IGNORECASE), ["Why is %s %s?"]),
		(re.compile(r"It is ([a-z][^\.!?]*)",re.IGNORECASE), ["Why is it %s?"]),
	]

	main()