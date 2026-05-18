from app.speech.speech_to_text import transcribe_audio


class SpeechAgent:

    def process(self, audio_path):

        text = transcribe_audio(audio_path)

        return {
            "type": "speech_to_text",
            "output": text
        }