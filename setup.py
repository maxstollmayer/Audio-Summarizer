from setuptools import setup

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

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
    py_modules=["audio_summarizer"],
    python_requires=">=3.9.0",
    install_requires=["click==8.1.3", "openai==0.27.2"],
    entry_points="""
        [console_scripts]
        summarize=audio_summarizer:main
    """,
)
