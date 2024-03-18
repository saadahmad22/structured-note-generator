import ffmpeg
import os
import speech_recognition as sr

r = sr.Recognizer()

def extract(input_loc, output_loc):
    if not os.path.isfile(output_loc):
        input_ = ffmpeg.input(input_loc)
        input_.output(output_loc, acodec='pcm_s16le', ar='16000', ac='1').run()
    return open(output_loc, "rb")

def audio_to_text(input_loc):
    try:
        speech = sr.AudioFile(input_loc)
        with speech as source:
            audio = r.record(source)
            return r.recognize_google(audio)
    except:
        return {"done": False}