# import streamlit as st
# import threading

# from app.voice_assistant.assistant_loop import start_voice_assistant


# def app():

#     st.title("🎙️ Voice Assistant")

#     st.markdown("""
#     ### Features

#     ✅ Wake Word Detection

#     ✅ Continuous Listening

#     ✅ Planner Agent Routing

#     ✅ Speech Responses

#     Wake Word: **Nova**
#     """)

#     if "voice_running" not in st.session_state:
#         st.session_state.voice_running = False

#     if st.button("▶ Start Voice Assistant"):

#         if not st.session_state.voice_running:

#             thread = threading.Thread(
#                 target=start_voice_assistant,
#                 daemon=True
#             )

#             thread.start()

#             st.session_state.voice_running = True

#             st.success(
#                 "Voice Assistant Started"
#             )

#     if st.session_state.voice_running:

#         st.info(
#             "Listening for wake word: Nova"
#         )


# import streamlit as st
# import threading
# from datetime import datetime

# from app.voice_assistant.assistant_loop import start_voice_assistant


# def app():

#     st.title("🤖 NOVA Voice Assistant")

#     # Session State
#     if "voice_running" not in st.session_state:
#         st.session_state.voice_running = False

#     if "last_query" not in st.session_state:
#         st.session_state.last_query = ""

#     if "last_command" not in st.session_state:
#         st.session_state.last_command = ""

#     if "last_agent" not in st.session_state:
#         st.session_state.last_agent = ""

#     if "last_response" not in st.session_state:
#         st.session_state.last_response = ""

#     if "voice_history" not in st.session_state:
#         st.session_state.voice_history = []

#     # Header Metrics
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.metric("Wake Word", "Nova")

#     with col2:
#         status = "🟢 Active" if st.session_state.voice_running else "🔴 Stopped"
#         st.metric("Status", status)

#     with col3:
#         st.metric(
#             "Time",
#             datetime.now().strftime("%H:%M:%S")
#         )

#     st.divider()

#     # Start Button
#     if st.button("🎤 Start Voice Assistant"):

#         if not st.session_state.voice_running:

#             thread = threading.Thread(
#                 target=start_voice_assistant,
#                 daemon=True
#             )

#             thread.start()

#             st.session_state.voice_running = True

#             st.success(
#                 "🚀 Voice Assistant Started"
#             )

#     # Live Status
#     if st.session_state.voice_running:

#         st.info(
#             "🎧 Listening for wake word: Nova"
#         )

#     st.divider()

#     # Live Conversation Panel
#     st.subheader("🗣 Live Conversation")

#     st.markdown(
#         f"""
#         **🎤 You Said**

#         {st.session_state.last_query}
#         """
#     )

#     st.markdown(
#         f"""
#         **📌 Command**

#         {st.session_state.last_command}
#         """
#     )

#     st.markdown(
#         f"""
#         **🧠 Selected Agent**

#         {st.session_state.last_agent}
#         """
#     )

#     st.markdown(
#         f"""
#         **🤖 Response**

#         {st.session_state.last_response}
#         """
#     )

#     st.divider()

#     st.subheader("📜 Recent Commands")

#     if st.session_state.voice_history:

#         for item in reversed(
#             st.session_state.voice_history[-10:]
#         ):
#             st.write("•", item)

#     else:
#         st.caption("No commands yet.")



import streamlit as st
import threading
import time

from app.voice_assistant.assistant_loop import (
    start_voice_assistant
)

import app.voice_assistant.voice_state as state


def app():

    st.title("🎙 Nova AI Assistant")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Wake Word",
            "Nova"
        )

    with col2:
        st.metric(
            "Status",
            "Active"
            if st.session_state.get(
                "voice_running",
                False
            )
            else "Stopped"
        )

    with col3:
        st.metric(
            "Mode",
            "Continuous"
        )

    st.markdown("---")

    if "voice_running" not in st.session_state:
        st.session_state.voice_running = False

    if st.button(
        "🚀 Start Assistant",
        use_container_width=True
    ):

        if not st.session_state.voice_running:

            threading.Thread(
                target=start_voice_assistant,
                daemon=True
            ).start()

            st.session_state.voice_running = True

    st.markdown("## 🎤 Live Conversation")

    heard = (
        state.last_heard
        if state.last_heard
        else "Waiting..."
    )

    command = (
        state.last_command
        if state.last_command
        else "Waiting..."
    )

    response = (
        state.last_response
        if state.last_response
        else "Waiting..."
    )

    tool = (
        state.last_tool
        if state.last_tool
        else "Waiting..."
    )

    st.info(
        f"🗣 You Said: {heard}"
    )

    st.warning(
        f"📌 Command: {command}"
    )

    st.success(
        f"🤖 AI Response: {response}"
    )

    st.caption(
        f"🧠 Planner Tool: {tool}"
    )

    st.markdown("---")

    st.markdown(
        "## 📜 Activity Feed"
    )

    log_box = st.container()

    with log_box:

        for log in state.voice_logs:

            st.markdown(log)

    time.sleep(1)

    st.rerun()