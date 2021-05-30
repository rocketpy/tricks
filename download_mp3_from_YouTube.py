#  pip install pytubemp3

from pytubemp3 import YouTube

YouTube(video_url).streams.filter(only_audio=True).first().download()

# or 
from pytube import YouTube


yt = YouTube(url)
yt.streams.get_audio_only().download(output_path='/home/', filename=yt.title)

# or
# Pytube does not support "mp3" format but you can download audio in webm format.

from pytube import YouTube
  
yt = YouTube("https://www.youtube.com/watch?v=")
stream = yt.streams.get_by_itag(251)
stream.download()


