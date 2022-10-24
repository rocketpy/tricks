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


# Command-line interface
# pytube3 ships with a simple CLI interface for downloading videos, playlists, and captions.

# downloading:
$ pytube3 http://youtube.com/watch?v=9bZkp7q19f0 --itag=18

# To view available streams:
$ pytube3 http://youtube.com/watch?v=9bZkp7q19f0 --list

 
# set of flags are:
"""
usage: pytube3 [-h] [--version] [--itag ITAG] [-r RESOLUTION] [-l] [-v]
               [--build-playback-report] [-c [CAPTION_CODE]] [-t TARGET]
               [-a [AUDIO]] [-f [FFMPEG]]
               [url]

Command line application to download youtube videos.

positional arguments:
  url                   The YouTube /watch or /playlist url

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --itag ITAG           The itag for the desired stream
  -r RESOLUTION, --resolution RESOLUTION
                        The resolution for the desired stream
  -l, --list            The list option causes pytube cli to return a list of
                        streams available to download
  -v, --verbose         Verbosity level, use up to 4 to increase logging -vvvv
  --build-playback-report
                        Save the html and js to disk
  -c [CAPTION_CODE], --caption-code [CAPTION_CODE]
                        Download srt captions for given language code. Prints
                        available language codes if no argument given
  -t TARGET, --target TARGET
                        The output directory for the downloaded stream.
                        Default is current working directory
  -a [AUDIO], --audio [AUDIO]
                        Download the audio for a given URL at the highest
                        bitrate availableDefaults to mp4 format if none is
                        specified
  -f [FFMPEG], --ffmpeg [FFMPEG]
                        Downloads the audio and video stream for resolution
                        providedIf no resolution is provided, downloads the
                        best resolutionRuns the command line program ffmpeg to
                        combine the audio and video
"""

# Using PyTube

# pip install pytube

# 

from pytube import YouTube 
  
# save to 
SAVE_PATH = "E:/"
  
# link of the video to be downloaded 
link="https://www.youtube.com/watch?v="

try:
    yt = YouTube(link) 
except: 
    print("Connection Error")
  
mp4files = yt.filter('mp4') 
yt.set_filename('New_Video')  
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    d_video.download(SAVE_PATH) 
except: 
    print("Error!") 
print('Completed!')


# downloading multiple videos
from pytube import YouTube 
  
# to save 
SAVE_PATH = "E:/"

link=["https://www.youtube.com/watch?v=", 
      "https://www.youtube.com/watch?v="]
for i in link: 
    try:
        yt = YouTube(i) 
    except:
        # exception 
        print("Error") 
    mp4_files = yt.filter('mp4') 
    video = yt.get(mp4_files[-1].extension,mp4files[-1].resolution) 
    try:
        video.download(SAVE_PATH) 
    except: 
        print("Error!") 
print('Completed!')

