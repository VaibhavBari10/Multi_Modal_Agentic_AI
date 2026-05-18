from app.tts.text_to_speech import speak


class TTSAgent:

    def process(self, text):

        speak(text)

        return {
            "type": "text_to_speech",
            "output": text
        }