import openai

GPT3_PROMPT = {
    "en": "Summarize this audio transcript in English:",
    "de": "Fasse das folgende Audiotranskript in Deutsch zusammen:",
}


def summarize(transcript: str, lang: str) -> str:
    """
    Sends request to OpenAI's davinci text completion model.
    Uses a different prompt depending on specified language.
    """
    return (
        openai.Completion.create(  # type: ignore
            model="text-davinci-003",
            prompt=f"{GPT3_PROMPT[lang]}:\n\n{transcript}",
            temperature=0.7,
            max_tokens=256,
        )
        .choices[0]  # type: ignore
        .text.strip()
    )
