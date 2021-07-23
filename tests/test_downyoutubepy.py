import sys, os
sys.path.insert(0,'./src')
import unittest
from downyoutubepy import DownYoutubePy

class TestDownYoutubePy(unittest.TestCase):

	def setUp(self):
		self.app = DownYoutubePy()
		self.app.url = "https://www.youtube.com/watch?v=3hCLhanF0A0"
		self.app.typefile = "audio"

		self.file = "00:09:30"
		self.inicio = "00:09:30"
		self.fim = "00:10:40"
		self.path = os.path.abspath(__file__)
		self.file = "miniatura.mp4"
		self.full_path = os.path.join(self.path, self.file)

	def tearDown(self):
		pass

	def test_download_audio(self):
		self.app.ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{ 'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '128'}],}
		opened = self.app.download()
		self.assertTrue(opened)

	def test_download_video(self):
		self.app.ydl_opts = {'format': 'bestvideo+bestaudio', 'postprocessors': [{ 'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],}
		opened = self.app.download()
		self.assertTrue(opened)

	#def test_cut(self, file, inicio, fim):

if __name__ == '__main__':
	unittest.main()