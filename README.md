# Audio-Summarizer

Summarize the spoken content of an audio file.

## Installation

Requires Python >=3.9. Clone the repository and install from inside the folder using `pip install .`.

## Usage

You can now use `summarize --audio <path> --out <path>` to summarize the speech of an audio file (<25MB) and log the transcript and summary to an output file. For more options see `summarize --help`.

## Development Setup

Create virtual environment with `python -m venv .venv`, activate it and install development requirements `python -m pip install -r requirements.txt`. Inside the folder install using `python -m pip install --editable .`. To add a new transcriber or summarizer model add the implementation to their respective folders and the cli option to the dictionary within `__init__.py`.
