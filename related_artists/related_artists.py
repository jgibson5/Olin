import MySQLdb as mdb
import sys
import copy
import time
sys.setrecursionlimit(100000)

query = "SELECT related_artist FROM artists_related_to WHERE artist = "

seen = set()
queue = []

class Artist(object):
	
	def __init__(self, name = ""):
		self.hist = []
		self.name = name
		
	def copy_hist(self, hist):
		self.hist = copy.copy(hist)
		
	def append_hist(self, artist):
		self.hist.append(artist)
		

def breadth_first_search(cur, current_artist, desired_artist):
	#if len(queue) == 0: return
	
	cur.execute(query + "'%s'" % current_artist.name)
	
	data = cur.fetchall()
	print data
	for d in data:
		a = Artist(d[0])
		
		#print "    %s" % d[0]
		if a.name == desired_artist.name:
			print "SUCCESS!\n", a.name, current_artist.hist
			return
		if a.name not in seen:
			#print d[0], queue
			seen.add(a.name)
			a.copy_hist(current_artist.hist)
			a.append_hist(current_artist.name)
			queue.append(a)
	
	new_artist = queue.pop(0)
	print new_artist.name
	#time.sleep(1)
	breadth_first_search(cur, new_artist, desired_artist)


def connect_db():
	con = mdb.connect('localhost', 'root', 
		'root', 'related_artists');

	cur = con.cursor()
	return cur


def main():
	cur = connect_db()
	
	a_old = Artist("justin-bieber-artist")
	a_new = Artist("beatles")
	
	breadth_first_search(cur, a_new, a_old)


if __name__ == "__main__":
	main()
