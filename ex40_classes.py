class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def reproduce_music(self):
		for i in self.lyrics:
			print i

happy_birthday = Song(["Happy birthday", "to you", "be happy!"])

happy_birthday.reproduce_music()

class Song_v2(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def reproduce_music(self):
		print self.lyrics
	def setLyrics(self, newLyrics):
		self.lyrics = newLyrics
happy_birthday2 = Song_v2("Happy birthday to you, be happy!")
happy_birthday2.reproduce_music()
happy_birthday2.setLyrics("Have a horrible day.")
happy_birthday2.reproduce_music()