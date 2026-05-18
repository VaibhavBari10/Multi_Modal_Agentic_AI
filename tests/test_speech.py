from app.speech.speech_to_text import transcribe_audio

text = transcribe_audio("datasets/audio/sample.wav")

print(text)