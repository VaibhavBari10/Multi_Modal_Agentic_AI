voice_logs = []

last_heard = ""
last_command = ""
last_response = ""
last_tool = ""

# Voice Assistant Status
# Possible values:
# Idle
# Speak Now
# Completed
# Time Out
# Error
status = "Idle"


def add_log(message):
    global voice_logs

    voice_logs.insert(0, message)

    # Keep only latest 30 logs
    if len(voice_logs) > 30:
        voice_logs.pop()