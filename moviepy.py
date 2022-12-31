# Path: audio.py
import moviepy.editor
video = moviepy.editor.VideoFileClip("video.mp4")
video.audio.write_audiofile("final.mp3")
print("Done")
