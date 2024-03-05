import ffmpeg

def extract():
    pass

# Load the video file
input_file = ffmpeg.input('vid.mp4')

# Extract the audio and save it as an MP3 file
input_file.output('audio.mp3', acodec='mp3').run()
