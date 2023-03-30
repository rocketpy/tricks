# pydub - Manipulate audio with an simple and easy high level interface

# http://pydub.com/
# pip install pydub


from pydub import AudioSegment

# Open a WAV file
song = AudioSegment.from_wav("song_name.wav")

# mp3
song = AudioSegment.from_mp3("song_name.mp3")
