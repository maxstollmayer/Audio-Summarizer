# Audio-Summarizer

Summarize the spoken content of an audio file.

## Installation

Requires Python >=3.9. Clone the repository and install from inside the folder using `pip install .`.

## Usage

You can now use `summarize --audio <path> --out <path>` to summarize the speech of an audio file and log the transcript and summary to an output file. For more options see `summarize --help`.

## Development

Clone the repository. Inside the folder create a virtual environment with `python -m venv .venv` and activate it. Install the module using `python -m pip install --editable .`. To include a new transcriber or summarizer model add the interface to the respective folder and the CLI option to the respective dictionary in `config.py`.
