import urllib2
import re
import _mysql
import time

class Scraper(object):
	url = 'http://www.pandora.com/'
	pattern = r'<a href="/([\w-]+)" class="similar_artist hash">(.+)</a>'

	queue = []
	finished = {}
	
	db = None
	
	def __init__(self):
		self.connectToDB()

	def scrape(self, artist):
		pageUrl = self.url + artist
		try:
			page = urllib2.urlopen(pageUrl)
		except:
			print "FAILED:", artist
			self.db.query("INSERT INTO failed (artist) VALUES ('%s');" %(artist,))
			return []
		data = page.read()
		page.close()
		results = re.findall(self.pattern, data)
		print results
		return results
		
	def connectToDB(self):
		host = "localhost"
		user = "root"
		password = "root"
		database = "related_artists"
		self.db = _mysql.connect(host = host, user = user, passwd = password, db = database)
		
	def addRelatedToDB(self, artist, artists):
		for rel_artist in artists:
			q = """INSERT INTO artists_related_to (artist, related_artist) 
			       VALUES ('%s', '%s');""" %(artist, rel_artist[0])
			self.db.query(q)
			self.db.query("INSERT INTO artist_info (artist, artist_name) VALUES ('%s', '%s') ON DUPLICATE KEY UPDATE artist_name = '%s';" %(rel_artist[0], rel_artist[1].replace("'", ""), rel_artist[1].replace("'", "")))
			
	def getQueue(self):
		q = "SELECT artist FROM queue WHERE completed = 0;"
		self.db.query(q)
		r = self.db.use_result()
		self.queue = [artist[0] for artist in r.fetch_row(0)]
		q = "SELECT artist FROM queue WHERE completed = 1;"
		self.db.query(q)
		r = self.db.use_result()
		r = (artist[0] for artist in r.fetch_row(0))
		for a in r:
			self.finished[a] = 0
		
	def updateQueue(self, flag, *artists):
		print flag, artists
		if len(artists) > 0:
			valueQ = ""
			for artist in artists:
				valueQ += "('%s')," %(artist,)
			valueQ = valueQ.rstrip(",")
			q = "INSERT INTO queue (artist) VALUES %s ON DUPLICATE KEY UPDATE completed = %s;" %(valueQ, flag)
			self.db.query(q)
		
	def process(self, artist):
		related_artists = self.scrape(artist)
		self.queue.extend([artst[0] for artst in related_artists if artst[0] not in self.finished])
		self.updateQueue('completed', *[a[0] for a in related_artists])
		self.updateQueue('1', artist)
		self.addRelatedToDB(artist, related_artists)
		
	def start(self, starting_artist = None):
		if starting_artist != None:
			self.updateQueue('1', starting_artist)
			
		self.getQueue()
		
		while len(self.queue) > 0:
			artist = self.queue.pop(0)
			print artist
			if artist not in self.finished:
				print "pass"
				self.process(artist)
				self.finished[artist] = 0
				
	def clearDB(self):
		self.db.query("TRUNCATE artists_related_to;")
		self.db.query("TRUNCATE queue;")
		self.db.query("TRUNCATE artist_info;")
		self.db.query("TRUNCATE failed;")


S = Scraper()
#S.clearDB()	
S.start('adele')


