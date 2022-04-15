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
    

# or, download an audio file if it possible
import youtube_dl
from __future__ import unicode_literals


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/...'])
    
    
# With postprocessors argument
import youtube_dl
from __future__ import unicode_literals


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': True
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/...'])
    
    
#  using pytube
import os
from pytube import YouTube


URL = YouTube('')
video = URL.streams.filter(only_audio=True).first()
out_file = video.download(output_path=".")
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
    
    
# Download video
# pip install pytube

from pytube import YouTube


URL = ""
yt = YouTube(URL)
yt = yt.get('mp4', '720p')
yt.download('/path/to/download/directory')


# Download video to a certain directory
# Need to use
"""
ydl_opts = {
    'outtmpl': os.path.join(download_path, '%(title)s-%(id)s.%(ext)s'),
}
"""
# download_path should be 'C:/Users/Desktop'.
# need use %(title)s.%(ext)s instead of %(title)s-%(id)s.%(ext)s if a file name without video ID.

# or
import os
import youtube_dl
from __future__ import unicode_literals


ydl_opts = {}
os.chdir('C:/Users/Desktop')
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/...'])

# or
import os
from pytube import YouTube


def YouTubeVideo(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

YouTubeVideo('https://www.youtube.com/...', './videos/...')

# or
"""
URL = ""
loc = '%s \%(extractor)s-%(id)s-%(title)s.%(ext)s'.replace("%s ", URL)
ytdl_format_options = {
'outtmpl': loc
}

with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
     ydl.download(['https://www.youtube.com/...'])
"""

# or
import youtube_dl
from __future__ import unicode_literals


ydl_opts = {'outtmpl': 'yourPathToDirectory/%(title)s.%(ext)s',}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/...'])
    
    
#  Some example to download
# pip install pytube
# python download.py

from pytube import YouTube


yt = YouTube("https://www.youtube.com/watch...", 
             use_oauth=False,
             allow_oauth_cache=True)
yt.streams.filter(file_extension='mp4', res="720p").first().download()

