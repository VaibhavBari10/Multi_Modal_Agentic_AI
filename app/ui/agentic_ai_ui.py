# import streamlit as st

# from app.agents.router import AIRouter
# from tts.text_to_speech import speak

# router = AIRouter()


# def app():

#     st.title("🤖 Agentic AI Assistant")

#     st.markdown(
#         """
#         Ask anything and the Planner Agent will
#         automatically select the best tool.
#         """
#     )

#     # Chat History
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display Previous Messages
#     for message in st.session_state.messages:

#         with st.chat_message(message["role"]):

#             st.write(message["content"])

#     # User Input
#     query = st.chat_input(
#         "Ask me anything..."
#     )

#     if query:

#         # Show User Message
#         st.session_state.messages.append(
#             {
#                 "role": "user",
#                 "content": query
#             }
#         )

#         with st.chat_message("user"):

#             st.write(query)

#         # AI Response
#         with st.spinner("Thinking..."):

#             result = router.route(
#                 input_type="text",
#                 data=query
#             )

#             response = result["response"]

#         with st.chat_message("assistant"):

#             st.write(response)

#         st.session_state.messages.append(
#             {
#                 "role": "assistant",
#                 "content": response
#             }
#         )

#         # Optional TTS
#         try:
#             speak(str(response))
#         except Exception:
#             pass




import streamlit as st
import threading

from app.agents.router import AIRouter
from app.voice_assistant.assistant_loop import (
    start_voice_assistant
)

router = AIRouter()


def app():

    st.title("🤖 Agentic AI Assistant")

    st.subheader("Chat with AI")

    query = st.text_input(
        "Enter your message"
    )

    if st.button("Send"):

        if query:

            result = router.route(
                "text",
                query
            )

            st.success(
                result["response"]
            )

    st.divider()

    st.subheader(
        "🎤 Continuous Voice Assistant"
    )

    st.info(
        """
Wake Word: Nova

Examples:
- Nova open YouTube
- Nova latest AI news
- Nova explain neural networks
"""
    )

    if st.button(
        "Start Voice Assistant"
    ):

        thread = threading.Thread(
            target=start_voice_assistant,
            daemon=True
        )

        thread.start()

        st.success(
            "Voice Assistant Started"
        )