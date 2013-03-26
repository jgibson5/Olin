import Tkinter as Tk
import skypeChat
import skypeHome

import logging
logging.basicConfig(level=logging.DEBUG)

class Gui():
	def __init__(self):
		self.root = Tk.Tk()
		self.skypeHome = skypeHome.skypeHome()
		self.skype = self.skypeHome.skype
		self.construct()
		#self.root.mainloop()
		
	def construct(self):
		#self.friendsFrame = Tk.Frame(self.root, width = 200, height = 600)
		#self.friendsFrame.pack(side = 'left')
		#self.friendsList = Tk.Listbox(self.friendsFrame)
		#self.friendsList.pack(fill = 'both', expand = 1)
		#self.friends = self.skypeHome.getFriends()
		self.skypeHome.createChat('guerillagirl28')
		self.skypeHome.chat.message("Testing")
		
		
gui = Gui()
	

