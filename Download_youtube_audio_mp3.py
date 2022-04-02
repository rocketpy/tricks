import YouTube from pytube

URL = ""

url = YouTube(URL)
result = url.streams.filter(only_audio=True)
result[0].download(/path)
