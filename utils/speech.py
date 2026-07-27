import whisper

# Load the Whisper model only once
model = whisper.load_model("base")


def transcribe_audio(audio_path):
    """
    Convert an audio file into text using OpenAI Whisper.
    """

    result = model.transcribe(audio_path)

    print("========== WHISPER RESULT ==========")
    print(result)
    print("===================================")

    return result["text"]