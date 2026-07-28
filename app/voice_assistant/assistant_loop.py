# from app.voice_assistant.listener import (
#     VoiceListener
# )

# from app.voice_assistant.wake_word import (
#     is_wake_word
# )

# from app.agents.router import AIRouter

# from app.tts.text_to_speech import speak


# listener = VoiceListener()

# router = AIRouter()

# print("Voice Assistant Started")

# while True:

#     try:

#         heard_text = listener.listen()

#         if not heard_text:
#             continue

#         if is_wake_word(heard_text):

#             speak("Yes, I am listening")

#             command = listener.listen()

#             if not command:
#                 continue

#             response = router.route(
#                 "text",
#                 command
#             )

#             answer = response["response"]

#             print("\nAI:", answer)

#             speak(answer)

#     except KeyboardInterrupt:

#         print("Stopping assistant...")

#         break

#     except Exception as e:

#         print("Error:", e)


from app.voice_assistant.voice_state import (
    add_log,
    last_heard,
    last_command,
    last_response,
    last_tool
)

import app.voice_assistant.voice_state as state

from app.voice_assistant.listener import (
    VoiceListener
)

from app.voice_assistant.wake_word import (
    is_wake_word,
    remove_wake_word
)

from app.agents.router import AIRouter

from tts.text_to_speech import speak


listener = VoiceListener()

router = AIRouter()


def start_voice_assistant():

    add_log("🚀 Voice Assistant Started")
    print("Wake Word:", "Nova")

    while True:

        try:
            add_log("🎤 Listening...")
            heard_text = listener.listen()

            if not heard_text:
                add_log("❌ Could not understand audio.")
                continue

            if is_wake_word(heard_text):
                state.last_heard = heard_text
                add_log(
                    f"🗣 You Said: {heard_text}"
                )

                command = remove_wake_word(
                    heard_text
                )

                # User said:
                # "Nova open youtube"

                if command:

                    state.last_command = command

                    add_log(
                        f"📌 Command: {command}"
                    )

                else:

                    speak(
                        "Yes, I am listening"
                    )

                    command = listener.listen()

                    if not command:

                        print(
                            "⏰ No command received."
                        )

                        speak(
                            "I did not hear any command."
                        )

                        continue

                result = router.route(
                    "text",
                    command
                )

                answer = result["response"]

                state.last_response = answer

                add_log(
                    f"🤖 AI: {answer}"
                )

                speak(
                    str(answer)
                )

        except KeyboardInterrupt:

            print(
                "\n🛑 Voice Assistant Stopped"
            )

            break

        except Exception as e:

            print(
                "Voice Assistant Error:",
                e
            )