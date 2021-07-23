import youtube_dl
import sys
from moviepy.editor import *
#import os
#from pathvalidate import sanitize_filename

class DownYoutubePy:

	url = None
	ydl_opts = None
	typefile = None
	file = None
	inicio = None
	fim = None

	def __init__(self):
		return True

	def download(self):
	    with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
	        filenames = [self.url]
	        ydl.download(filenames)

	    return True

	def cut(self):
		clip = VideoFileClip(self.file)
		clip = clip.subclip(self.inicio, self.fim)
	    #clip.write_videofile("cut{}".format(self.file))