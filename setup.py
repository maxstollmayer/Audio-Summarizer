from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="audio-summarizer",
    version="0.1",
    description="Summarize the spoken content of an audio file.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Maximilian Stollmayer",
    author_email="max.stolly@gmail.com",
    url="https://github.com/maxstolly/Audio-Summarizer",
    license="Mozilla Public License Version 2.0",
    py_modules=["main", "config", "transcribers", "summarizers"],
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        summarize=main:main
    """,
)
