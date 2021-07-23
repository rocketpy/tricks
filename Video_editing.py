#  moviepy - Video editing with Python

# PyPi: https://pypi.org/project/moviepy/
# Docs: https://zulko.github.io/moviepy/

# Example Scripts: https://zulko.github.io/moviepy/examples/examples.html

#  pip install moviepy

# Example
from moviepy.editor import *


video = VideoFileClip("myHolidays.mp4").subclip(50,60)

# Make the text. Many more options are available.
txt_clip = (TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25) # Many options


#  Text with moving letters
"""
import numpy as np
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects


# WE CREATE THE TEXT THAT IS GOING TO MOVE, WE CENTER IT.

screensize = (720,460)
txtClip = TextClip('Cool effect',color='white', font="Amiri-Bold",
                   kerning = 5, fontsize=100)
cvc = CompositeVideoClip( [txtClip.set_pos('center')],
                        size=screensize)

# THE NEXT FOUR FUNCTIONS DEFINE FOUR WAYS OF MOVING THE LETTERS

"""
 
