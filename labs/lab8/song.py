#
# song.py
# Created by Nicolas Lara Fonseca and Rodrigo Andrade
# 19 February 2020
# 

class Song:
	"""Song Object"""
	def __init__(self,name,artist,genre,length,album):
		self.name = name
		self.artist = artist
		self.genre = genre
		self.length = length
		self.album = album

song_list=[]
song_list.append(Song('Been Away','Brent Faiyaz','R&B/Soul',224,'F the World'))
song_list.append(Song('Blue World','Mac Miller','Hip-Hop/Rap',209,'Circles'))
song_list.append(Song('Sacrifices','Drake','Hip-Hop/Rap',308,'More Life'))
song_list.append(Song('No Bullets Spent','Spoon','Alternative',221,'Everything Hits at Once'))

for s in song_list:
	print(f'{s.name} by {s.artist} off their album {s.album}, is classified as {s.genre} and is {s.length} seconds long.\n')

