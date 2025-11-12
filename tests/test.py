from speech_to_text import SpeechToText
from pynput.keyboard import Key, Listener

stt = SpeechToText(model_size="small")
# result = stt.transcribe_file("../audio/test_audio.ogg")

# print(f"Transcribed Text: {result['text']}")

# result_mic = stt.transcribe_from_microphone()

# print(f"Transcribed Text from Microphone: {result_mic['text']}")

# result_mic = stt.transcribe_until_silence()

# print(f"Transcribed Text from Microphone until Silence: {result_mic['text']}")



