#  pyttsx3 - Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. 
#  Supports multiple TTS engines, including Sapi5, nsss, and espeak.

# PyPi: https://pypi.org/project/pyttsx3/

#  pip install pyttsx3



# Usage :

import pyttsx3


engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


