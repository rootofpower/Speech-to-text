# record audio from microphone or audio file
# and save it to a wav file
import time
import wave
import pyaudio
import threading
import os
import numpy as np
from pathlib import Path
from typing import Optional

class AudioRecorder:
    
    """"Class to handle audio recording from a given source."""
    
    def __init__(
        self,
        channels: int = 1,
        rate: int = 16000,
        chunk_size: int = 1024,
        format: int = pyaudio.paInt16
    ):  
        self.channels = channels
        self.rate = rate
        self.chunk_size = chunk_size
        self.format = format
        self.audio_interface = pyaudio.PyAudio()        

    def record(self, duration: float, output_file: Optional[str] = None) -> str:
        """
        Record audio
        
        Args:
            duration (float): Duration of the recording in seconds.
            output_file (Optional[str]): Path to save the recorded audio file.
            
        Returns:
            str: Path to the saved audio file.
        """ 
        
        if output_file is None:
            output_file = "temp.wav"
            
        stream = self.audio_interface.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        print("Recording...")
        frames = []
        
        for _ in range(0, int(self.rate / self.chunk_size * duration)):
            data = stream.read(self.chunk_size)
            frames.append(data)
            
        print("Recording finished.")
        stream.stop_stream()
        stream.close()
        
        wf = wave.open(output_file, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio_interface.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        return output_file
    
    def record_until_silence(
        self,
        silence_threshold: float = 500.0,
        silence_duration: float = 2.0,
        max_duration: float = 30.0,
        output_file: Optional[str] = None
    ) -> str:
        """
        Record audio until silence is detected.
        
        Args:
            silence_threshold (float): Threshold to consider as silence.
            silence_duration (float): Duration of silence to stop recording.
            max_duration (float): Maximum duration to record.
            output_file (Optional[str]): Path to save the recorded audio file.
        """
        if output_file is None:
            output_file = "temp.wav"
            
        stream = self.audio_interface.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk_size
        )
        
        print("Recording... Speak now!")
        frames = []
        silent_chunks = 0
        max_silent_chunks = int(self.rate / self.chunk_size * silence_duration)
        max_chunks = int(self.rate / self.chunk_size * max_duration)
        
        for i in range(max_chunks):
            data = stream.read(self.chunk_size)
            frames.append(data)
            
            audio_data = np.frombuffer(data, dtype=np.int16)
            rms = np.sqrt(np.mean(audio_data**2))
            
            if rms < silence_threshold:
                silent_chunks += 1
                if silent_chunks >= max_silent_chunks:
                    print("Silence detected, stopping recording.")
                    break
            else:
                silent_chunks = 0
                
        print("Recording finished.")
        stream.stop_stream()
        stream.close()
        
        wf = wave.open(output_file, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio_interface.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        return output_file
    
    def __del__(self):
        """close PyAudio interface"""
        self.audio_interface.terminate()