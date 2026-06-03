from app.llm.gpt_handler import ask_llm


class TranslationAgent:

    def translate(self, text, language="Hindi"):

        prompt = f"""
        Translate the following text into {language}:

        {text}
        """

        response = ask_llm(prompt)

        return response