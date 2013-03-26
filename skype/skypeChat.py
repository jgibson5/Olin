import Skype4Py



#from Skype4Py.api.posix_x11 import threads_init
#threads_init()

class skypeChat():
	def __init__(self, skype, user):
		self.user = user
		self.skype = skype
		
	def message(self, text):
		self.skype.SendMessage(self.user, text)
		
	def addUser(self, *users):
		for user in users:
			skype.AddMember(self.user.Handle)


#lisa = skype.User(Username = 'gorillagirl28')
#shley = skype.User(Username = 'ashley.guertin')
#joe = skype.User(Username = 'joe.gibson55')

#chat = skypeChat(lisa)
#chat.message("Hi Lisa, just testing once more")
