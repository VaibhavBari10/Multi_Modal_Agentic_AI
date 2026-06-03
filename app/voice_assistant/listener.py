# import speech_recognition as sr

# from app.voice_assistant.config import (
#     LISTEN_TIMEOUT,
#     PHRASE_TIME_LIMIT
# )


# class VoiceListener:

#     def __init__(self):

#         self.recognizer = sr.Recognizer()
        
#         # Improve microphone sensitivity
#         self.recognizer.energy_threshold = 300

#         # Wait slightly longer before considering speech finished
#         self.recognizer.pause_threshold = 0.8

#         # Dynamic adjustment for different environments
#         self.recognizer.dynamic_energy_threshold = True

#     def listen(self):

#         with sr.Microphone() as source:

#             print("Listening...")

#             self.recognizer.adjust_for_ambient_noise(
#                 source,
#                 duration=1
#             )

#             audio = self.recognizer.listen(
#                 source,
#                 timeout=LISTEN_TIMEOUT,
#                 phrase_time_limit=PHRASE_TIME_LIMIT
#             )

#         try:

#             text = self.recognizer.recognize_google(
#                 audio
#             )

#             print(f"You Said: {text}")

#             return text

#         except Exception:

#             return ""


import speech_recognition as sr

from app.voice_assistant.config import (
    LISTEN_TIMEOUT,
    PHRASE_TIME_LIMIT
)


class VoiceListener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300

        self.recognizer.pause_threshold = 0.8

        self.recognizer.dynamic_energy_threshold = True

    def listen(self):

        try:

            with sr.Microphone() as source:

                print("\n🎤 Start Speaking...")

                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=LISTEN_TIMEOUT,
                    phrase_time_limit=PHRASE_TIME_LIMIT
                )

            text = self.recognizer.recognize_google(
                audio
            )

            print(f"🗣 You Said: {text}")

            return text

        except sr.WaitTimeoutError:

            print("⏰ Timeout: No speech detected.")

            return ""

        except sr.UnknownValueError:

            print("❌ Could not understand audio.")

            return ""

        except Exception as e:

            print("Voice Error:", e)

            return ""