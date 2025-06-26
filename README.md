# Speech-Recognition

Company: CODTECH IT SOLUTIONS

NAME: PASUPULATE HANISHKA ROYAL

INTERN ID: CTO6DG22

DOMAIN: ARTIFICIAL INTELLIGENCE

DURATION: 6 WEEKS

MENTOR: NEELA SANTOSH

Description : This Python code is designed to convert speech from an audio file into text using the SpeechRecognition library, which interfaces with online speech-to-text services like Google’s Web Speech API. It simplifies the process of transcribing spoken words into written text from various audio file formats, including WAV, MP3, and FLAC.
The core of this code is the function transcribe_audio_speechrecognition(audio_path). This function accepts the path to an audio file as its input. One of the challenges in speech recognition is that most speech-to-text engines, including the one used in the SpeechRecognition library, prefer audio files in WAV format. To solve this, the code uses the pydub library to automatically convert audio files from formats like MP3, FLAC, and others into WAV if necessary.

Once the audio is ready in WAV format, the function initializes the SpeechRecognition Recognizer class, which acts as the main interface for capturing and processing the audio. The recognizer then opens the audio file using the AudioFile class. Before transcribing, it uses the adjust_for_ambient_noise() function, which listens to a short segment (default 1 second) to detect background noise levels. This helps improve transcription accuracy by reducing the impact of static, hums, or other background sounds.

The recognizer then listens to the entire audio file using the record() method, which reads the full audio into memory. Once the audio is captured, the transcription process is executed using recognize_google(), which sends the audio data to Google’s free Web Speech API over the internet. The API returns the recognized text in string format. The resulting text is converted to lowercase for consistency and returned by the function.
