from speech_to_text import SpeechToText, AudioRecorder, WhisperModel
from pathlib import Path
import unittest

class TestSpeechToText(unittest.TestCase):
    def test_initialization(self):
        stt = SpeechToText(model_size="tiny")
        self.assertIsNotNone(stt.model)
        self.assertIsNotNone(stt.recorder)
        
        
class TestAudioRecorder(unittest.TestCase):
    def test_initialization(self):
        recorder = AudioRecorder()
        self.assertIsNotNone(recorder)
        self.assertEqual(recorder.channels, 1)
        self.assertEqual(recorder.rate, 16000)
        
class TestWhisperModel(unittest.TestCase):
    def test_singleton(self):
        model_manager1 = WhisperModel()
        model_manager2 = WhisperModel()
        self.assertIs(model_manager1, model_manager2)
        
        