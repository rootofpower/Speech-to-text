from pathlib import Path
from typing import List

SUPPORTED_LANGUAGES = {
    "en": "English",
    "sk": "Slovak",
    "ukr": "Ukrainian",
    "de": "German",
    "ru": "Russian",
    "cs": "Czech",
    "pl": "Polish",
    "es": "Spanish",
    "fr": "French",
    "it": "Italian",
    # and more else
}

def get_supported_languages() -> List[str]:
    """Get a list of supported language codes.

    Returns:
        List[str]: List of supported language codes
    """
    return list(SUPPORTED_LANGUAGES.keys())

def validate_audio_file(file_path: str) -> bool:
    """Validate if the audio file exists and is of a supported format.

    Args:
        file_path (str): Path to the audio file
    Returns:
        bool: True if valid, False otherwise
    """
    path = Path(file_path)
    if not path.exists():
        return False    
    
    valid_extensions = {".mp3", ".wav", ".m4a", ".flac", ".aac", ".ogg"}
    return path.suffix.lower in valid_extensions