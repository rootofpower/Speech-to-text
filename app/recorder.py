# record audio from microphone or audio file
# and save it to a wav file
import wave, pyaudio, threading, time, os


class AudioRecorder:
    """"Class to handle audio recording from a given source."""
    
    def __init__(self, source):
        self.source = source

    def record(self, duration, output_file):
        # logic to record audio from self.source for duration seconds
        # and save it to output_file
        pass