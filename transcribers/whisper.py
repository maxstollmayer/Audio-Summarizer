import openai


def transcribe(audio_path: str, _: str) -> str:
    """
    Sends request to OpenAI's whisper STT model.
    """
    with open(audio_path, "rb") as audio_file:
        transcript: str = openai.Audio.transcribe("whisper-1", audio_file).text  # type: ignore

    return transcript.strip()
