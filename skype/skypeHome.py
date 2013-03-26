import Skype4Py
import skypeChat
		
class skypeHome():
	def __init__(self):
		self.skype = Skype4Py.Skype(Transport = 'x11')
		self.skype.Attach()
		self.chat = None
		
	def getFriends(self):
		friends = []
		for friend in self.skype.Friends:
			friends.append(friend)
		return friends
		
	def createChat(self, user):
		self.chat = skypeChat.skypeChat(self.skype, user)
		
