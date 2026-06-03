from app.rag.rag_agent import RAGAgent


class KnowledgeAgent:

    def __init__(self):

        self.rag = RAGAgent()

    def answer(self, question):

        response = self.rag.answer_question(
            question
        )

        return response