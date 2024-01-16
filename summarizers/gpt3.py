import openai


GPT3_PROMPT = {
    "en": "Summarize this audio transcript in English:",
    "de": "Fasse das folgende Audiotranskript in Deutsch zusammen:",
}


class GPT3:
    def summarize(self, transcript: str, language: str) -> str:
        """
        Sends request to OpenAI's davinci text completion model.
        Uses a different prompt depending on specified language.
        """
        lang = language.lower().strip()
        if lang not in GPT3_PROMPT.keys():
            raise ValueError(
                f"ERROR: language {language} not supported. Should be in {GPT3_PROMPT.keys()}."
            )
        return (
            openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{GPT3_PROMPT[lang]}:\n\n{transcript}",
                temperature=0.7,
                max_tokens=256,
            )
            .choices[0]
            .text.strip()
        )
