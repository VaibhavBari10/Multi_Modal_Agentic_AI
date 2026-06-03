# from app.voice_assistant.config import WAKE_WORD


# def is_wake_word(text: str) -> bool:

#     if not text:
#         return False

#     return WAKE_WORD.lower() in text.lower()


from app.voice_assistant.config import WAKE_WORD


def is_wake_word(text):

    if not text:
        return False

    return text.lower().startswith(
        WAKE_WORD.lower()
    )


def remove_wake_word(text):

    return text.lower().replace(
        WAKE_WORD.lower(),
        "",
        1
    ).strip()