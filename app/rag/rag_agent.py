"""from app.rag.retriever import Retriever
from app.llm.gpt_handler import ask_llm


class RAGAgent:

    def __init__(self):

        self.retriever = Retriever()

    def answer_question(self, question):

        docs = self.retriever.retrieve(question)

        context = "\n".join(docs)

        prompt = f'''
        Answer the question using the context below.

        Context:
        {context}

        Question:
        {question}
        '''

        response = ask_llm(prompt)

        return response"""
        
        
from app.rag.retriever import Retriever


class RAGAgent:

    def __init__(self):

        self.retriever = Retriever()

    def answer_question(self, question):

        docs = self.retriever.retrieve(question)

        context = "\n".join(docs)
        #context = "\n".join(docs[:1])[:1500]

        return context