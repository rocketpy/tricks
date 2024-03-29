# pip install python-opencv moviepy

# to run script
# $ python extract_frames_opencv.py file_name.mp4

import os
import cv2
import numpy as np
from datetime import timedelta


SAVING_FRAMES_PER_SECOND = 10

def format_timedelta(td):
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")


def get_saving_frames_durations(cap, saving_fps):
    s = []
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)

    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s


def main(video_file):
    filename, _ = os.path.splitext(video_file)
    filename += "-opencv"

    if not os.path.isdir(filename):
        os.mkdir(filename)

    cap = cv2.VideoCapture(video_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    count = 0

    while True:
        is_read, frame = cap.read()
        if not is_read:
            break
        frame_duration = count / fps
        try:
            closest_duration = saving_frames_durations[0]
        except IndexError:
            break

        if frame_duration >= closest_duration:
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            cv2.imwrite(os.path.join(filename, f"frame{frame_duration_formatted}.jpg"), frame) 
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        count += 1

if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    main(video_file)
    
    
# using MoviePy
# $ python extract_frames_moviepy.py file_name.mp4
import os
import numpy as np
from datetime import timedelta
from moviepy.editor import VideoFileClip


SAVING_FRAMES_PER_SECOND = 10

def format_timedelta(td):
    result = str(td)
    
    try:
        result, ms = result.split(".")
    except ValueError:
        return (result + ".00").replace(":", "-")

    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")

def main(video_file):
    # load the video clip
    video_clip = VideoFileClip(video_file)
    # make a folder by the name of the video file
    filename, _ = os.path.splitext(video_file)
    filename += "-moviepy"
    if not os.path.isdir(filename):
        os.mkdir(filename)

    saving_frames_per_second = min(video_clip.fps, SAVING_FRAMES_PER_SECOND)
    step = 1 / video_clip.fps if saving_frames_per_second == 0 else 1 / saving_frames_per_second

    for current_duration in np.arange(0, video_clip.duration, step):
        frame_duration_formatted = format_timedelta(timedelta(seconds=current_duration))
        frame_filename = os.path.join(filename, f"frame{frame_duration_formatted}.jpg")
        video_clip.save_frame(frame_filename, current_duration)
        
if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    main(video_file)
