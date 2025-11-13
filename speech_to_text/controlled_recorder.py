import pyaudio
import wave
import numpy as np
from typing import Optional
import threading


class ControlledRecorder:
    
    """Class to handle audio recording with additional control"""
    
    def __init__(
        self,
        filename: str = "recording.wav",
        channels: int = 1,
        rate: int = 44100,
        chunk_size: int = 1024,
        format: int = pyaudio.paInt16,
        recordingState: bool = False
    ):
        self.filename = filename
        self.channels = channels
        self.rate = rate
        self.frames = []
        self.chunk_size = chunk_size
        self.format = format
        self.audio_interface = pyaudio.PyAudio()
        self.recordingState = recordingState
        self.stream: pyaudio.Stream | None = None
        self.thread: threading.Thread | None = None
    
    def start_recording(self):
        """start recording"""
        if self.recordingState:
            print("Recording is going now!!!")
            return

        self.recordingState = True
        self.frames = []
        
        self.stream = self.audio_interface.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        self.thread = threading.Thread(target=self._record, daemon=True)
        self.thread.start()
        
        print("Record was started . . . Now you can speak.")
        
        
    def _record(self):
        """record in another thread method"""
        while self.recordingState:
            try:
                if self.stream is not None:
                    data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                    self.frames.append(data)
            except Exception as e:
                print(f"Error while recording: {e}")
                break
    
    def stop_recording(self):
        """stop recording"""
        if not self.recordingState:
            print("Recording has been ended!")
            return
        self.recordingState = False
        
        if self.thread:
            self.thread.join()
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        
        self.save_recording()

    def save_recording(self) -> str:
        """save recording"""
        try:
            with wave.open(self.filename, 'wb') as wf:
                wf.setnchannels(self.channels)
                wf.setsampwidth(self.audio_interface.get_sample_size(self.format))
                wf.setframerate(self.rate)
                wf.writeframes(b''.join(self.frames))
                print(f"Recording saved to {self.filename}")
                return self.filename
        except Exception as e:
            print(f"Error saving recording: {e}")
            return ""
    def __del__(self):
        """Clear all resources if deleting object"""
        if self.audio_interface:
            self.audio_interface.terminate()