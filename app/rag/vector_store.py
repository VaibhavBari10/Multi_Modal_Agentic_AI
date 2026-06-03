"""from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            'all-MiniLM-L6-v2'
        )

        self.index = faiss.IndexFlatL2(384)

        self.documents = []

    def add_documents(self, texts):

        self.documents.extend(texts)

        embeddings = self.model.encode(texts)

        embeddings = np.array(
            embeddings
        ).astype('float32')

        self.index.add(embeddings)

    def search(self, query, k=3):

        # Safety check
        if len(self.documents) == 0:

            return ["No documents found."]

        query_embedding = self.model.encode([query])

        query_embedding = np.array(
            query_embedding
        ).astype('float32')

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for idx in indices[0]:

            # Prevent invalid FAISS indexes
            if idx == -1:
                continue

            if idx < len(self.documents):

                results.append(
                    self.documents[idx]
                )

        return results

    def save(self, path="datasets/vector_store.pkl"):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        with open(path, "wb") as f:

            pickle.dump(
                self.documents,
                f
            )

    def load(self, path="datasets/vector_store.pkl"):

        with open(path, "rb") as f:

            self.documents = pickle.load(f)

        # Rebuild FAISS index
        embeddings = self.model.encode(
            self.documents
        )

        embeddings = np.array(
            embeddings
        ).astype('float32')

        self.index = faiss.IndexFlatL2(384)

        self.index.add(embeddings)"""
        

"""from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            'all-MiniLM-L6-v2'
        )

        self.index = faiss.IndexFlatL2(384)

        self.documents = []

    def add_documents(self, texts):

        self.documents.extend(texts)

        embeddings = self.model.encode(texts)

        embeddings = np.array(
            embeddings
        ).astype('float32')

        self.index.add(embeddings)

    def search(self, query, k=3):

        if len(self.documents) == 0:

            return ["No documents found."]

        query_embedding = self.model.encode([query])

        query_embedding = np.array(
            query_embedding
        ).astype('float32')

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            if idx < len(self.documents):

                results.append(
                    self.documents[idx]
                )

        return results

    def save(self):

        os.makedirs("datasets", exist_ok=True)

        # Save documents
        with open(
            "datasets/documents.pkl",
            "wb"
        ) as f:

            pickle.dump(
                self.documents,
                f
            )

        # Save FAISS index
        faiss.write_index(
            self.index,
            "datasets/faiss_index.bin"
        )

    def load(self):

        # Load documents
        with open(
            "datasets/documents.pkl",
            "rb"
        ) as f:

            self.documents = pickle.load(f)

        # Load FAISS index
        self.index = faiss.read_index(
            "datasets/faiss_index.bin"
        )"""
        
        
"""from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            'all-MiniLM-L6-v2'
        )

        self.index = faiss.IndexFlatL2(384)

        self.documents = []

    def add_documents(self, texts):

        self.documents.extend(texts)

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        embeddings = np.array(
            embeddings
        ).astype('float32')

        self.index.add(embeddings)

    def search(self, query, k=2):

        query_embedding = self.model.encode([query])

        query_embedding = np.array(
            query_embedding
        ).astype('float32')

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            if idx < len(self.documents):

                results.append(
                    self.documents[idx]
                )

        return results

    def save(self):

        os.makedirs(
            "datasets",
            exist_ok=True
        )

        with open(
            "datasets/documents.pkl",
            "wb"
        ) as f:

            pickle.dump(
                self.documents,
                f
            )

        faiss.write_index(
            self.index,
            "datasets/faiss_index.bin"
        )

    def load(self):

        with open(
            "datasets/documents.pkl",
            "rb"
        ) as f:

            self.documents = pickle.load(f)

        self.index = faiss.read_index(
            "datasets/faiss_index.bin"
        )"""
        
        
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os


class VectorStore:

    def __init__(self):

        self.model = SentenceTransformer(
            'all-MiniLM-L6-v2'
        )

        self.documents = []

        self.index = faiss.IndexFlatL2(384)

    def add_documents(self, texts):

        self.documents = texts

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        embeddings = np.array(
            embeddings
        ).astype('float32')

        self.index.add(embeddings)

    def search(self, query, k=2):

        if len(self.documents) == 0:

            return []

        query_embedding = self.model.encode([query])

        query_embedding = np.array(
            query_embedding
        ).astype('float32')

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for idx in indices[0]:

            if 0 <= idx < len(self.documents):

                results.append(
                    self.documents[idx]
                )

        return results

    def save(self, path):

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        faiss.write_index(
            self.index,
            "datasets/faiss_index.bin"
        )

        with open(path, "wb") as f:

            pickle.dump(
                self.documents,
                f
            )

    def load(self, path):

        self.index = faiss.read_index(
            "datasets/faiss_index.bin"
        )

        with open(path, "rb") as f:

            self.documents = pickle.load(f)