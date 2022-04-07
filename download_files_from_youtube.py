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
