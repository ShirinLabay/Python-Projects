# sounddevice library will help you to record your voice.
# SciPy's library will save the voice in a specific file format.

import sounddevice
from scipy.io.wavfile import write


def voice_recorder(seconds, file):
    # enter the number of seconds you want to record your voice
    # file - record file to be saved
    print("Recording started..")
    recording = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording finished")


voice_recorder(10, "record.wav")
