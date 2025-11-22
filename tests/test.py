from speech_to_text import SpeechToText
from pynput.keyboard import Key, Listener
import threading
import time
from datetime import datetime
from speech_to_text.controlled_recorder import ControlledRecorder
stt = SpeechToText(model_size="small")
result = stt.transcribe_file("/home/rootofpower/personal/pygovno/projects/speech_to_text/audio/test.ogg")
print(f"Transcribed Text: {result['text']}")

# result_mic = stt.transcribe_from_microphone()

# print(f"Transcribed Text from Microphone: {result_mic['text']}")

# result_mic = stt.transcribe_until_silence()

# print(f"Transcribed Text from Microphone until Silence: {result_mic['text']}")


# i need a two threads one for listening for key presses and one for transcribing,
# if i press 's' it starts transcribing from microphone until i press 'q' to stop it

# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# recording_filename = f"recording_{timestamp}.wav"

# recorder = ControlledRecorder(filename=recording_filename)

# try: 
#     while True:
#         cmd = input("Press 's' to start recording, 'q' to stop recording and transcribe: ").strip().lower()
#         if cmd == 's':
#             recorder.start_recording()
#         elif cmd == 'q':
#             if recorder.recordingState:
#                 recorder.stop_recording()
#                 print("Transcribing the recorded audio...")
#                 result = stt.transcribe_file(recording_filename)
#                 print(f"Transcribed Text: {result['text']}")
#             print("ended transcription.")
#             break
#         else:
#             print("not exisiting command.")
# except KeyboardInterrupt:
#     print("Exiting the program.")
#     if recorder.recordingState:
#         recorder.stop_recording()        