#  pip install pydub
#  docs - http://pydub.com/

from pydub import AudioSegment


song = AudioSegment.from_wav("song_name.wav")  # wav 
song = AudioSegment.from_mp3("song_name.mp3")  # mp3
#  others format look at docs

#  take a slice
ten_seconds = 10 * 1000  # in miliseconds
first_10_seconds = song[:10000]
last_5_seconds = song[-5000:]

# make louder and the end quieter 
beginning = first_10_seconds + 6  # boost volume by 6dB
end = last_5_seconds - 3  # reduce volume by 3dB

#  concatenate audio (add one file to the end of another)
without_the_middle = beginning + end


