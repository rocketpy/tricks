# pydub - Manipulate audio with an simple and easy high level interface

# http://pydub.com/
# pip install pydub


from pydub import AudioSegment

# Open a WAV file
song = AudioSegment.from_wav("song_name.wav")

# mp3
song = AudioSegment.from_mp3("song_name.mp3")

# others
ogg_version = AudioSegment.from_ogg("never_gonna_give_you_up.ogg")
flv_version = AudioSegment.from_flv("never_gonna_give_you_up.flv")
mp4_version = AudioSegment.from_file("never_gonna_give_you_up.mp4", "mp4")
wma_version = AudioSegment.from_file("never_gonna_give_you_up.wma", "wma")
aac_version = AudioSegment.from_file("never_gonna_give_you_up.aiff", "aac")


# Take a slice audio

# pydub does things in miliseconds
ten_seconds = 10 * 1000
first_10_seconds = song[:10000]
last_5_seconds = song[-5000:]
