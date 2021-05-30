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
