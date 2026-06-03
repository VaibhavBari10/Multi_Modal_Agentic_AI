from app.tts.text_to_speech import speak


class ResponseAgent:

    def respond(self, text, speak_output=True):

        if speak_output:

            speak(text)

        return {
            "response": text
        }