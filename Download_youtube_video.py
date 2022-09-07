# pytube3 - Python 3 library for downloading YouTube Videos.

# https://pytube3.readthedocs.io/en/latest/
# https://pypi.org/project/pytube3/

# pip install pytube3

from pytube import YouTube

YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
# or
# YouTube('http://youtube.com/watch?v=9bZkp7q19f0').streams[0].download()
# This example will download the highest quality progressive download stream available.

yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams
"""
 .filter(progressive=True, file_extension='mp4')
 .order_by('resolution')
 .desc()
 .first()
 .download()
"""


# to show video streams are available:
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
print(yt.streams)

# To only view these progressive download streams:
yt.streams.filter(progressive=True)

# only want to see the DASH streams (also referred to as "adaptive") you can do:
yt.streams.filter(adaptive=True)


# Playlists
# You can also download a complete Youtube playlist:
from pytube import Playlist

playlist = Playlist("https://www.youtube.com/playlist?list=PLynhp4cZEpTbRs_PYISQ8v_uwO0_mDg_X")
for video in playlist:
    video.streams.get_highest_resolution().download()


# Filtering
yt.streams.filter(only_audio=True)

# To list only mp4 streams
yt.streams.filter(subtype='mp4')

# Multiple filters can also be specified:
yt.streams.filter(subtype='mp4', progressive=True)
# this can also be expressed as:
yt.streams.filter(subtype='mp4').filter(progressive=True)

# select streams by their itag, without needing to filter:
yt.streams.get_by_itag(22)

#  to optimize for a specific feature, such as the "highest resolution" or "lowest average bitrate":
yt.streams.filter(progressive=True).order_by('resolution').desc()

