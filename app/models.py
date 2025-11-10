import whisper 
from typing import Optional

class WhisperModel:
    """Class to handle Whisper model"""
    
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def load_model(self, model_size: str = "base"):
        """Load the Whisper model 

            Args: 
                model_size (str): tiny, base, small, medium, large
        """
        if self._model is None:
            print(f"Loading Whisper model: {model_size}...")
            self._model = whisper.load_model(model_size)
            print("Model loaded.")
        return self._model
    
    def get_model(self):
        """Get the loaded Whisper model"""
        if self._model is None:
            return self.load_model()
        return self._model