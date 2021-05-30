#  pip install pytubemp3

from pytubemp3 import YouTube


YouTube(video_url).streams.filter(only_audio=True).first().download()

