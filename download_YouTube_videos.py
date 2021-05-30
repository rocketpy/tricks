#  pytube - is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.

# PyPi: https://pypi.org/project/pytube/
# Docs: https://pytube.io/en/latest/

# pip install pytube

from pytube import YouTube

YouTube('https://youtu.be/...').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=')
yt.streams
# .filter(progressive=True, file_extension='mp4')
# .order_by('resolution')
# .desc()
# .first()
# .download()


# Example, download all the videos from a playlist and saving them with the title from youtube in mp4 and mp4 audio formats.
"""
import os
import re
import subprocess
from pytube import YouTube
from pytube import Playlist


path = r'to destination folder'
playlist_url = '...'

play = Playlist(playlist_url)
play._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
# print(len(play.video_urls))

for url in play.video_urls:
    yt = YouTube(url)
    audio = yt.streams.get_audio_only()
    audio.download(path)
    nome = yt.title
    new_filename=nome+'.mp3'
    default_filename =nome+'.mp4'
    ffmpeg = ('ffmpeg -i ' % path default_filename + new_filename)
    subprocess.run(ffmpeg, shell=True)
         
print('Download complete !')
"""
