"""from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.store = VectorStore()

    def retrieve(self, query):

        return self.store.search(query)"""
        

"""from app.rag.vector_store import VectorStore

class Retriever:

    def __init__(self):

        self.store = VectorStore()

        self.store.load()

    def retrieve(self, query):

        return self.store.search(query)"""
        
        
"""from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.store = VectorStore()

        self.store.load()

    def retrieve(self, query):

        return self.store.search(query)"""
        
        
from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.store = VectorStore()

        self.store.load(
            "datasets/vector_store.pkl"
        )

    def retrieve(self, query):

        return self.store.search(query)