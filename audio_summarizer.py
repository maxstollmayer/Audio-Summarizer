"""
Simple CLI tool to transcribe and summarize an audio file.
"""

import datetime
import time
from typing import Optional

import click
import openai

STT_MODEL = "whisper-1"
SUMMARY_MODEL = "text-davinci-003"
MAX_TOKENS = 256
TEMPERATURE = 0.7
PROMPT = {
    "en": "Summarize this audio transcript in English:",
    "de": "Fasse das folgende Audiotranskript in Deutsch zusammen:",
}


def transcribe(audio_path: str) -> str:
    """
    Sends request to OpenAI's whisper STT model.
    """
    with open(audio_path, "rb") as audio_file:
        transcript: str = openai.Audio.transcribe(STT_MODEL, audio_file).text  # type: ignore

    return transcript.strip()


def summarize(transcript: str, lang: str) -> str:
    """
    Sends request to OpenAI's davinci text completion model.
    Uses a different prompt depending on specified language.
    """
    return (
        openai.Completion.create(  # type: ignore
            model=SUMMARY_MODEL,
            prompt=f"{PROMPT[lang]}:\n\n{transcript}",
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )
        .choices[0]  # type: ignore
        .text.strip()
    )


def write_output(out_path: str, audio_path: str, text: str, kind: str) -> None:
    """
    Writes given transcript or summary to the output file
    with a timestamp and the location of the audio.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"[{now}] {kind.capitalize()} of {audio_path}:\n{text}\n\n"
    with open(out_path, "a+", encoding="utf-8") as out_file:
        out_file.write(content)


@click.command()
@click.option("--audio", type=click.Path(), required=True, help="Path to audio file.")
@click.option(
    "--out",
    type=click.Path(),
    required=False,
    help="Path to optional output file. (Will be created if non-existent.)",
)
@click.option(
    "--key",
    type=click.Path(),
    required=False,
    help="Path to API key file.",
)
@click.option(
    "--lang",
    type=click.Choice(["en", "de"], case_sensitive=False),
    default="en",
    show_default=True,
    help="Language to use for the summarization.",
)
@click.option(
    "--transcribe-only", is_flag=True, help="Only transcribe and not summarize."
)
@click.option(
    "--summarize-only",
    is_flag=True,
    help="Only summarize the text file given with '--audio'.",
)
def main(
    audio: str,
    out: Optional[str],
    lang: str,
    key: Optional[str],
    transcribe_only: bool,
    summarize_only: bool,
) -> None:
    """
    Entry point of the CLI tool. For usage run `python -m audio_summarizer.py --help`.
    """
    if key is not None:
        openai.api_key_path = key

    if summarize_only:
        with open(audio, "r", encoding="utf-8") as file:
            transcript = file.read()
    else:
        print("Transcribing audio...", end=" ", flush=True)
        start_time = time.time()
        transcript = transcribe(audio)
        end_time = time.time()
        seconds = round(end_time - start_time, 2)
        print(f"finished in {seconds} seconds.", end=" ", flush=True)
        if out is not None:
            write_output(out, audio, transcript, "Transcript")
            print(f"Saved to file {out}.")

    if transcribe_only:
        print("\n")
        print(transcript)
    else:
        print("Summarizing transcript...", end=" ", flush=True)
        start_time = time.time()
        summary = summarize(transcript, lang)
        end_time = time.time()
        seconds = round(end_time - start_time, 2)
        print(f" finished in {seconds} seconds.", end=" ", flush=True)
        if out is not None:
            write_output(out, audio, summary, "Summary")
            print(f"Saved to file {out}.\n")
        print(summary)
