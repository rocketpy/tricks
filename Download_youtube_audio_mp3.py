import YouTube from pytube

URL = ""
url = YouTube(URL)
result = url.streams.filter(only_audio=True)
result[0].download(/path)


# pip install --upgrade youtube-dl
from __future__ import unicode_literals
import youtube_dl

URL = ""
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])

