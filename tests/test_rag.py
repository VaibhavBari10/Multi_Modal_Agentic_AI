from app.rag.rag_agent import RAGAgent

rag = RAGAgent()

question = input("Ask question: ")

response = rag.answer_question(question)

print("\nAI Answer:\n")

print(response)