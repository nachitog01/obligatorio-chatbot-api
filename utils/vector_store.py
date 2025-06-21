import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

def create_vector_store(documents):
    ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")

    embeddings = OllamaEmbeddings(
        base_url=ollama_url,
        model=ollama_model
    )

    vectorstore = Chroma.from_documents(documents, embedding=embeddings)
    return vectorstore
