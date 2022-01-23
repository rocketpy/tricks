#  pyttsx3 - Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. 
#  Supports multiple TTS engines, including Sapi5, nsss, and espeak.

# PyPi: https://pypi.org/project/pyttsx3/

#  pip install pyttsx3


# Usage :
import pyttsx3


engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


# Changing Voice , Rate and Volume :
import pyttsx3

engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()


# This code to iterate through the voices to find the female voice 
# On Windows 10 the female voice was HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
import pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')

for voice in voices:
    engine.setProperty('voice', voice.id)
    print voice.id
    engine.say('Bla bla bla')  # Some text
    
engine.runAndWait()

# Update
import pyttsx

engine = pyttsx.init()
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait() 

# or
engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

