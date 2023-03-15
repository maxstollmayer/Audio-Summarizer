# Audio-Summarizer

Summarize the spoken content of an audio file.

## Installation

Clone the repository and install from inside the folder using `pip install .`. Make sure you have a valid OpenAI API key set to the environment variable `OPENAI_API_KEY` or in a file that will be given as an optional parameter. You can sign up for one at <https://platform.openai.com/>.

## Usage

You can now use `summarize --audio <path> --out <path>` to summarize the speech of an audio file (<25MB) and log the transcript and summary to an output file. For more options see `summarize --help`.

## Development Setup

Create virtual environment, activate it and install development requirements `python -m pip install -r requirements.txt`. Inside the folder install using `python -m pip install --editable .`.
