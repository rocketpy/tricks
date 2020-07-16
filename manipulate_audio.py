#  pip install pydub
#  docs - http://pydub.com/

from pydub import AudioSegment


song_wav = AudioSegment.from_wav("song_name.wav")  # wav 
song_mp_3 = AudioSegment.from_mp3("song_name.mp3")  # mp3
#  others format look at docs

#  take a slice
ten_seconds = 10 * 1000  # in miliseconds
first_10_seconds = song[:10000]
last_5_seconds = song[-5000:]

# make louder and the end quieter 
beginning = first_10_seconds + 6  # boost volume by 6dB
end = last_5_seconds - 3  # reduce volume by 3dB

#  save the results (again whatever ffmpeg supports)
awesome.export("new_song.mp3", format="mp3")

#  concatenate audio (add one file to the end of another)
without_the_middle = beginning + end

#  AudioSegments are immutable
backwards = song.reverse()  # song is not modified

#  crossfade (again, beginning and end are not modified)
with_style = beginning.append(end, crossfade=1500)  # 1.5 second crossfade

# repeat
do_it_over = with_style * 2  # repeat the clip twice

#  fade (note that you can chain operations because everything returns an AudioSegment)
awesome = do_it_over.fade_in(2000).fade_out(3000)  # 2 sec fade in, 3 sec fade out
