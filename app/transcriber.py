from typing import Optional, Dict
from .models import WhisperModel
from .recorder import AudioRecorder
from pathlib import Path

class SpeechToText:
    """The main class for speech-to-text transcription."""
    
    def __init__(self, model_size: str = "base"):
        """
        Args:
            model_size: Model size(e.g., "tiny", "base", "small", "medium", "large")
        """
        self.model_manager = WhisperModel()
        self.model = self.model_manager.load_model(model_size)
        self.recorder = AudioRecorder()

    def transcribe_file(self,
                        audio_file: str,
                        language: Optional[str] = None
    ) -> Dict:
        """Transcribe audiofile

        Args:
            audio_file (str): Path to audio file
            language (Optional[str], optional): Language of the audio. Defaults to None.

        Returns:
            Dict: Transcription result
        """
        
        print(f"Transcribing file: {audio_file}")
        kwargs = {}
        if language:
            kwargs["language"] = language
            
        result = self.model.transcribe(audio_file, **kwargs)
        print(f"Transcription language: {result['language']}")
        
        return {
            'text': result['text'],
            'language': result['language'],
            'segments': result.get('segments', [])
        }
    def transcribe_from_microphone(
        self,
        duration: float = 5.0,
        language: Optional[str] = None,
        cleanup: bool = True
    ) -> Dict:
        """Record audio from microphone and transcribe it.

        Args:
            duration (float): Duration to record in seconds. Defaults to 5.0.
            language (Optional[str], optional): Language of the audio. Defaults to None.
            cleanup (bool, optional): Whether to delete the temporary audio file after transcription. Defaults to True.

        Returns:
            Dict: Transcription result
        """
        audio_file = self.recorder.record(duration)
        result = self.transcribe_file(audio_file, language=language)
        if cleanup:
            Path(audio_file).unlink(missing_ok=True)
            
        return result
    
    
    def transcribe_until_silence(
        self,
        language: Optional[str] = None,
        silence_threshold: float = 500.0,
        silence_duration: float = 2.0,
        max_duration: float = 30.0,
        cleanup: bool = True
    ) -> Dict:
        """
        Record audio from microphone until silence
        
        Args:
            language (Optional[str], optional): Language of the audio. Defaults to None.
            silence_threshold (float, optional): Threshold for silence detection. Defaults to 500.0.
            silence_duration (float, optional): Duration of silence to stop recording. Defaults to 2.0.
            max_duration (float, optional): Maximum duration to record. Defaults to 30.0.
            cleanup (bool, optional): Whether to delete the temporary audio file after transcription. Defaults to True.
        """
        
        temp_audio_file = self.recorder.record_until_silence(
            silence_threshold=silence_threshold,
            silence_duration=silence_duration,
            max_duration=max_duration
        )
        
        result = self.transcribe_file(temp_audio_file, language=language)
        
        if cleanup:
            Path(temp_audio_file).unlink(missing_ok=True)
            
        return result
    