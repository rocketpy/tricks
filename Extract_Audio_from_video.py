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
