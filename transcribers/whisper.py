import openai


class Whisper:
    def transcribe(self, audio_path: str, language: str) -> str:
        """
        Sends request to OpenAI's whisper STT model.
        """
        with open(audio_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file).text

        return transcript.strip()
