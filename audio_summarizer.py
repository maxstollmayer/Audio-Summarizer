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


def authenticate(key_path: str) -> None:
    pass


def transcribe(audio_path: str) -> str:
    with open(audio_path, "rb") as audio_file:
        transcript: str = openai.Audio.transcribe(STT_MODEL, audio_file).text  # type: ignore

    return transcript.strip()


def summarize(transcript: str, lang: str) -> str:
    return (
        openai.Completion.create(  # type: ignore
            model="text-davinci-003",
            prompt=f"{PROMPT[lang]}:\n\n{transcript}",
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS,
        )
        .choices[0]  # type: ignore
        .text.strip()
    )


def write_output(
    out_path: str, audio_path: str, transcript: str, summary: Optional[str]
) -> None:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"[{now}] Transcript of {audio_path}:\n{transcript}\n\n"

    if summary is not None:
        content += f"[{now}] Summary of {audio_path}:\n{summary}\n\n"

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
def main(
    audio: str,
    out: Optional[str],
    lang: str,
    key: Optional[str],
    transcribe_only: bool,
) -> None:
    summary = None
    # authenticate(key)

    print("Transcribing audio...", end="", flush=True)
    start_time = time.time()
    transcript = transcribe(audio)
    end_time = time.time()
    print(f" finished in {round(end_time - start_time, 2)} seconds.")

    if not transcribe_only:
        print("Summarizing transcript...", end="", flush=True)
        start_time = time.time()
        summary = summarize(transcript, lang)
        end_time = time.time()
        print(f" finished in {round(end_time - start_time, 2)} seconds.")

    if out is not None:
        print(f"Wrote to file {out}.")
        write_output(out, audio, transcript, summary)

    print("\n")
    if transcribe_only:
        print(transcript)
    else:
        print(summary)
