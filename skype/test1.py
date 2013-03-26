from Skype4Py import Skype
import sys

client = Skype(Transport = 'x11')
client.Attach()
user = sys.argv[1]
message = ' '.join(sys.argv[2:]
client.SendMessage(user, message)
