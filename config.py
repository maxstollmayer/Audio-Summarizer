"""
Add new transcribers and summarizers here:
"""

from typing import Protocol

from transcribers.whisper import Whisper
from transcribers.coqui import Coqui

from summarizers.gpt3 import GPT3
from summarizers.accel_brain import Accel_Brain


class Transcriber(Protocol):
    def transcribe(self, audio_path: str, language: str) -> str:
        ...


class Summarizer(Protocol):
    def summarize(self, transcript: str, language: str) -> str:
        ...


TRANSCRIBERS: dict[str, Transcriber] = {
    "whisper": Whisper(),
    "coqui": Coqui(),
}

SUMMARIZERS: dict[str, Summarizer] = {
    "gpt3": GPT3(),
    "accel_brain": Accel_Brain(),
}
