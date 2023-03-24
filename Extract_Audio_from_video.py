# pip install moviepy
# $ sudo apt update
# $ sudo apt install ffmpeg


# Using FFmpeg
import os
import sys
import subprocess


def convert_video_to_audio_ffmpeg(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    
if __name__ == "__main__":
    vf = sys.argv[1]
    convert_video_to_audio_ffmpeg(vf)
    
    
    
# Use MoviePy
# $ python video2audio_moviepy.py file_name.webm
import os
import sys
from moviepy.editor import VideoFileClip


def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")
    
if __name__ == "__main__":
    vf = sys.argv[1]
    convert_video_to_audio_moviepy(vf)
