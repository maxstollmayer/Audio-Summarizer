"""
Simple CLI tool to transcribe and summarize an audio file.
"""

import datetime
import time
from typing import Optional

import click

from config import TRANSCRIBERS, SUMMARIZERS


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
@click.option(
    "--audio",
    type=click.Path(),
    required=True,
    help="Path to audio file or in summarize-only mode the path to transcript text.",
)
@click.option(
    "--out",
    type=click.Path(),
    required=False,
    help="Path to optional output file. Note that it will be created if non-existent. If not provided then output will only be printed to the screen.",
)
@click.option(
    "--lang",
    type=click.Choice(["en", "de"], case_sensitive=False),
    default="en",
    show_default=True,
    help="Language to use for the summarization.",
)
@click.option(
    "--stt-model",
    type=click.Choice(list(TRANSCRIBERS.keys()), case_sensitive=False),
    default=list(TRANSCRIBERS.keys())[0],
    show_default=True,
    help="Model to use for the transcription. Note that Whisper requires the environment variable `OPENAI_API_KEY` to be set.",
)
@click.option(
    "--summary-model",
    type=click.Choice(list(SUMMARIZERS.keys()), case_sensitive=False),
    default=list(SUMMARIZERS.keys())[0],
    show_default=True,
    help="Model to use for the summarization. Note that GPT3 requires the environment variable `OPENAI_API_KEY` to be set.",
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
    stt_model: str,
    summary_model: str,
    transcribe_only: bool,
    summarize_only: bool,
) -> None:
    """
    Summarize the spoken content of an audio file.
    """

    if summarize_only:
        with open(audio, "r", encoding="utf-8") as file:
            transcript = file.read()
    else:
        click.echo("Transcribing audio... ", nl=False)
        start_time = time.time()
        transcript = TRANSCRIBERS[stt_model].transcribe(audio, lang)
        end_time = time.time()
        click.echo(f"finished in {round(end_time - start_time, 2)} seconds ", nl=False)

        if out is not None:
            write_output(out, audio, transcript, "Transcript")
            click.echo(f"and saved to file {out}", nl=False)

    if transcribe_only:
        click.echo("")
        click.echo("")
        click.echo(transcript)
    else:
        click.echo("")
        click.echo("Summarizing transcript... ", nl=False)
        start_time = time.time()
        summary = SUMMARIZERS[summary_model].summarize(transcript, lang)
        end_time = time.time()
        click.echo(f"finished in {round(end_time - start_time, 2)} seconds ", nl=False)

        if out is not None:
            write_output(out, audio, summary, "Summary")
            click.echo(f"and saved to file {out}", nl=False)

        click.echo("")
        click.echo("")
        click.echo(summary)
        click.echo("")
