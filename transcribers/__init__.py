"""
Add new transcriber here:
"""

from transcribers import whisper, coqui

TRANSCRIBE = {
    "whisper": whisper.transcribe,
    "coqui": coqui.transcribe,
}
