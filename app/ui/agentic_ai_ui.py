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




# import streamlit as st
# import threading

# from app.agents.router import AIRouter
# from app.voice_assistant.assistant_loop import (
#     start_voice_assistant
# )

# router = AIRouter()


# def app():

#     st.title("🤖 Agentic AI Assistant")

#     st.subheader("Chat with AI")

#     query = st.text_input(
#         "Enter your message"
#     )

#     if st.button("Send"):

#         if query:

#             result = router.route(
#                 "text",
#                 query
#             )

#             st.success(
#                 result["response"]
#             )

#     st.divider()

#     st.subheader(
#         "🎤 Continuous Voice Assistant"
#     )

#     st.info(
#         """
# Wake Word: Nova

# Examples:
# - Nova open YouTube
# - Nova latest AI news
# - Nova explain neural networks
# """
#     )

#     if st.button(
#         "Start Voice Assistant"
#     ):

#         thread = threading.Thread(
#             target=start_voice_assistant,
#             daemon=True
#         )

#         thread.start()

#         st.success(
#             "Voice Assistant Started"
#         )






import streamlit as st
import threading

from app.agents.router import AIRouter

from app.voice_assistant.assistant_loop import (
    start_voice_assistant
)

import app.voice_assistant.voice_state as state


router = AIRouter()


def run_voice_assistant():

    result = start_voice_assistant()

    state.last_command = result.get(
        "input",
        ""
    )

    state.last_tool = result.get(
        "action",
        ""
    )

    state.last_response = result.get(
        "response",
        ""
    )


def app():

    st.title("🤖 Nova Agentic AI Assistant")

    st.markdown("---")

    # ======================================
    # TEXT CHAT SECTION
    # ======================================

    st.subheader("💬 Chat Assistant")

    query = st.text_input(
        "Enter your message"
    )

    if st.button(
        "Send",
        use_container_width=True
    ):

        if query:

            result = router.route(
                "text",
                query
            )

            st.success(
                result["response"]
            )

    st.markdown("---")

    # ======================================
    # VOICE ASSISTANT SECTION
    # ======================================

    st.subheader("🎤 Voice Assistant")

    col1, col2 = st.columns(
        [1, 4]
    )

    with col1:

        if st.button(
            "🎤",
            use_container_width=True
        ):

            # Reset previous state
            state.last_heard = ""
            state.last_command = ""
            state.last_response = ""
            state.last_tool = ""

            thread = threading.Thread(
                target=run_voice_assistant,
                daemon=True
            )

            thread.start()

    with col2:

        st.info(
            f"Status : {state.status}"
        )

    st.markdown("---")

    # ======================================
    # LIVE RESULTS
    # ======================================

    st.subheader("📝 Voice Session")

    st.markdown("### Input")

    st.success(
        state.last_heard
        if state.last_heard
        else "-"
    )

    st.markdown("### Action Taken")

    st.warning(
        state.last_tool
        if state.last_tool
        else "-"
    )

    st.markdown("### AI Response")

    st.info(
        state.last_response
        if state.last_response
        else "-"
    )

    st.markdown("---")

    st.caption(
        "Click the microphone and speak your command."
    )

    st.caption(
        "Example: Nova open YouTube"
    )

    st.caption(
        "Example: Nova latest AI news"
    )

    st.caption(
        "Example: Nova explain neural networks"
    )

    # Auto-refresh every second
    if state.status in [
        "Speak Now",
        "Completed",
        "Time Out"
    ]:

        st.rerun()