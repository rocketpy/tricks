# pydub - Manipulate audio with an simple and easy high level interface

# http://pydub.com/
# https://github.com/jiaaro/pydub/

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


# Make the beginning louder and the end quieter
# boost volume by 6dB
beginning = first_10_seconds + 6
# reduce volume by 3dB
end = last_5_seconds - 3


# Concatenate audio (add one file to the end of another)
without_the_middle = beginning + end

# AudioSegments are immutable
# song is not modified
backwards = song.reverse()

# Crossfade (again, beginning and end are not modified)
# 1.5 second crossfade
with_style = beginning.append(end, crossfade=1500)

# Repeat
# repeat the clip twice
do_it_over = with_style * 2

# Fade (note that you can chain operations because everything returns an AudioSegment)
# 2 sec fade in, 3 sec fade out
awesome = do_it_over.fade_in(2000).fade_out(3000)

# Save the results (again whatever ffmpeg supports)
awesome.export("mashup.mp3", format="mp3")


# Example
import os
import glob
from pydub import AudioSegment


video_dir = '/home/johndoe/downloaded_videos/'  # Path where the videos are located
extension_list = ('*.mp4', '*.flv')

os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')
        

# Example 2
from glob import glob
from pydub import AudioSegment


playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("*.mp3")]
first_song = playlist_songs.pop(0)

# let's just include the first 30 seconds of the first song (slicing
# is done by milliseconds)
beginning_of_song = first_song[:30*1000]

playlist = beginning_of_song
for song in playlist_songs:
    # We don't want an abrupt stop at the end, so let's do a 10 second crossfades
    playlist = playlist.append(song, crossfade=(10 * 1000))
    
# let's fade out the end of the last song
playlist = playlist.fade_out(30)

# hmm I wonder how long it is... ( len(audio_segment) returns milliseconds )
playlist_length = len(playlist) / (1000*60)

# lets save it!
with open("%s_minute_playlist.mp3" % playlist_length, 'wb') as out_f:
    playlist.export(out_f, format='mp3')
    
    
# Kapre
# Keras Audio Preprocessors - compute STFT, InverseSTFT, Melspectrogram, and others on GPU real-time.

# https://kapre.readthedocs.io/en/latest/
# https://github.com/keunwoochoi/kapre

# pip install kapre
# https://github.com/keunwoochoi/kapre/tree/master/examples

from tensorflow.keras.models import Sequential
from kapre import STFT, Magnitude, MagnitudeToDecibel
from kapre.composed import get_melspectrogram_layer, get_log_frequency_spectrogram_layer
from tensorflow.keras.layers import Conv2D, BatchNormalization, ReLU, GlobalAveragePooling2D, Dense, Softmax


# 6 channels (!), maybe 1-sec audio signal, for an example.
input_shape = (44100, 6)
sr = 44100
model = Sequential()
# A STFT layer
model.add(STFT(n_fft=2048, win_length=2018, hop_length=1024,
               window_name=None, pad_end=False,
               input_data_format='channels_last', output_data_format='channels_last',
               input_shape=input_shape))

model.add(Magnitude())
model.add(MagnitudeToDecibel())  # these three layers can be replaced with get_stft_magnitude_layer()
# Alternatively, you may want to use a melspectrogram layer
# melgram_layer = get_melspectrogram_layer()
# or log-frequency layer
# log_stft_layer = get_log_frequency_spectrogram_layer()


# pyAudioAnalysis

# Example of convert Video to MP3
# To convert video (mkv) to audio (mp3)
# ffmpeg -i video.mkv audio.mp3

# https://github.com/tyiannak/pyAudioAnalysis/
"""
Installation

    Clone the source of this library: git clone https://github.com/tyiannak/pyAudioAnalysis.git
    Install dependencies: pip install -r ./requirements.txt 
    Install using pip: pip install -e .
    
Dependencies:

NUMPY
pip install numpy
MATPLOTLIB
pip install matplotlib
SCIPY
pip install scipy  
SKLEARN
pip install sklearn 
hmmlearn
pip install hmmlearn
Simplejson
pip install simplejson
eyeD3
pip install eyed3
pydub
pip install pydub
"""

from pyAudioAnalysis import audioTrainTest as aT
aT.extract_features_and_train(["classifierData/music","classifierData/speech"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
aT.file_classification("data/doremi.wav", "svmSMtemp","svm")

# Beat extraction
# The beat rate estimation is implemented in function beat_extraction() of MidTermFeatures.py file. It accepts 2 arguments:
# (a) the short-term feature matrix and (b) the window step (in seconds). Obviously, the feature_extraction() function of the ShortTermFeatures.py
# file is needed to extract the sequence of feature vectors before extracting the beat.

# Command-line example:
# python audioAnalysis.py beatExtraction -i data/beat/small.wav --plot

# example, the same signal stored in WAV and MP3 files is loaded to numpy arrays.
# Original here: https://hackernoon.com/audio-handling-basics-how-to-process-audio-files-using-python-cli-jo283u3y

# Read WAV and MP3 files to array
import plotly
import numpy as np
from scipy.io import wavfile
import plotly.graph_objs as go
from pydub import AudioSegment
from plotly.offline import init_notebook_mode


# read WAV file using scipy.io.wavfile
fs_wav, data_wav = wavfile.read("data/music_8k.wav")

# read MP3 file using pudub
audiofile = AudioSegment.from_file("data/music_8k.mp3")
data_mp3 = np.array(audiofile.get_array_of_samples())
fs_mp3 = audiofile.frame_rate

print('Sq Error Between mp3 and wav data = {}'.
      format(((data_mp3 - data_wav)**2).sum()))
print('Signal Duration = {} seconds'.
      format(data_wav.shape[0] / fs_wav))
