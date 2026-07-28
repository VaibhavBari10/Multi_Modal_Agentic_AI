voice_logs = []

last_heard = ""
last_command = ""
last_response = ""
last_tool = ""


def add_log(message):
    global voice_logs

    voice_logs.insert(0, message)

    if len(voice_logs) > 30:
        voice_logs.pop()