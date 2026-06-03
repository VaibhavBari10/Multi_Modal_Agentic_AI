"""import os

from app.rag.pdf_loader import load_pdf
from app.rag.vector_store import VectorStore

store = VectorStore()

DOCUMENTS_DIR = "documents"

texts = []

for file in os.listdir(DOCUMENTS_DIR):

    if file.endswith(".pdf"):

        path = os.path.join(
            DOCUMENTS_DIR,
            file
        )

        print(f"Loading: {file}")

        text = load_pdf(path)

        texts.append(text)

store.add_documents(texts)

store.save()

print("Vector database created.")"""


"""import os

from app.rag.pdf_loader import load_pdf
from app.rag.vector_store import VectorStore

store = VectorStore()

DOCUMENTS_DIR = "documents"

texts = []


def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunks.append(
            text[i:i + chunk_size]
        )

    return chunks


for file in os.listdir(DOCUMENTS_DIR):

    if file.endswith(".pdf"):

        path = os.path.join(
            DOCUMENTS_DIR,
            file
        )

        print(f"Loading: {file}")

        text = load_pdf(path)

        chunks = chunk_text(text)

        texts.extend(chunks)

store.add_documents(texts)

store.save()

print("Fast vector database created.")"""


import os

from app.rag.pdf_loader import load_pdf
from app.rag.vector_store import VectorStore

store = VectorStore()

DOCUMENTS_DIR = "documents"

all_chunks = []

for file in os.listdir(DOCUMENTS_DIR):

    if file.endswith(".pdf"):

        path = os.path.join(
            DOCUMENTS_DIR,
            file
        )

        print(f"Loading: {file}")

        chunks = load_pdf(path)

        all_chunks.extend(chunks)

print(f"Total chunks: {len(all_chunks)}")

store.add_documents(all_chunks)

store.save("datasets/vector_store.pkl")

print("Vector database created.")