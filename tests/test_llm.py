from app.llm.gpt_handler import ask_llm

response = ask_llm(
    "Explain artificial intelligence simply."
)

print(response)