import re
import moviepy.editor as mp


tgt_folder = "/folder/contains/your/mp4"
 
for file in [n for n in os.listdir(tgt_folder) if re.search('mp4',n)]:
    full_path = os.path.join(tgt_folder, file)
    output_path = os.path.join(tgt_folder, os.path.splitext(file)[0] + '.mp3')
    clip = mp.AudioFileClip(full_path).subclip(10,) # disable if do not want any clipping
    clip.write_audiofile(output_path)

