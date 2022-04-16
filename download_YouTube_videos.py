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


# Example 2
from pytube import YouTube
from moviepy.editor import *
 
    
# download a file from youtube
youtube_link = 'https://www.youtube.com/watch?v=yourtubevideos'
w = YouTube(youtube_link).streams.first()
w.download(output_path="/your/target/directory")
 
# download a file with only audio, to save space
# if the final goal is to convert to mp3
youtube_link = 'https://www.youtube.com/watch?v=targetyoutubevideos'
y = YouTube(youtube_link)
t = y.streams.filter(only_audio=True).all()
t[0].download(output_path="/your/target/directory")


# or how to download video from youtube
import os
from pytube import YouTube


def YouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

YouTube('https://www.youtube.com/...', './videos/...')


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


# 
import os
import sys
from pytube import YouTube



def downloadYoutube(vid_url, path):
    yt = YouTube(vid_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)

    yt.download(path)
