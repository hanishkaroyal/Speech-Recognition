import speech_recognition as sr  # Speech-to-text
from pydub import AudioSegment   # Audio format conversion
import os

def transcribe_audio_speechrecognition(audio_path):
    """
    Transcribes an audio file using the SpeechRecognition library with Google Web Speech API.

    Args:
        audio_path (str): Path to the audio file. Supports formats like WAV, MP3, etc.

    Returns:
        str: Transcribed text or an error message.
    """
    recognizer = sr.Recognizer()

    # Convert audio to WAV if it's not already
    file_ext = os.path.splitext(audio_path)[1].lower()
    if file_ext != ".wav":
        sound = AudioSegment.from_file(audio_path)
        wav_path = "temp_audio.wav"
        sound.export(wav_path, format="wav")
        audio_file = wav_path
        temp_file_created = True
    else:
        audio_file = audio_path
        temp_file_created = False

    try:
        with sr.AudioFile(audio_file) as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening to the audio...")
            audio_data = recognizer.record(source)

        print("Transcribing...")
        transcription = recognizer.recognize_google(audio_data)
        return transcription.lower()

    except sr.UnknownValueError:
        return "Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        # Clean up temporary WAV file if created
        if temp_file_created and os.path.exists(audio_file):
            os.remove(audio_file)


# ----- Example Usage -----

if __name__ == "__main__":
    # Provide your own audio file path (WAV, MP3, etc.)
    audio_path = "your_audio_file.wav"  # Example: "sample.mp3" or "test.wav"

    if os.path.exists(audio_path):
        result = transcribe_audio_speechrecognition(audio_path)
        print("\nTranscription Result:")
        print(result)
    else:
        print(f"Audio file not found: {audio_path}")