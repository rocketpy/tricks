#  mhyt - download files from youtube using simple code

# PyPi: https://pypi.org/project/mhyt/
# https://github.com/matan-h/mhyt

# pip install mhyt


from mhyt import yt_download


url = "https://www.youtube.com/..."
file = "Video.mp4"
yt_download(url,file)

file = "music.mp3"
yt_download(url,file,ismusic=True)


#  The audio example is not fully working because ytdl downloads a webm format. To fix this you can do:
from mhyt import yt_download


url = "https://www.youtube.com/..."
file = "music.mp3"
tmp_file = "music.webm"
yt_download(url,tmp_file,ismusic=True,codec  = "mp3")

