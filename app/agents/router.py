from app.agents.speech_agent import SpeechAgent
from app.agents.tts_agent import TTSAgent
from app.agents.vision_agent import VisionAgent


class AIRouter:

    def __init__(self):

        self.speech_agent = SpeechAgent()
        self.tts_agent = TTSAgent()
        self.vision_agent = VisionAgent()

    def route(self, input_type, data=None):

        # Speech Input
        if input_type == "audio":

            return self.speech_agent.process(data)

        # Text Input
        elif input_type == "text":

            return self.tts_agent.process(data)

        # Vision Input
        elif input_type == "vision":

            return self.vision_agent.process()

        else:

            return {
                "type": "error",
                "output": "Unsupported input type"
            }