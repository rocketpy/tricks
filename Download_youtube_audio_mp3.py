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
    
    
# Download video
# pip install pytube

from pytube import YouTube


URL = ""
yt = YouTube(URL)
yt = yt.get('mp4', '720p')
yt.download('/path/to/download/directory')


