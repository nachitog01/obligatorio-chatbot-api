import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(folder_path: str):
    all_docs = []
    chunk_size = int(os.getenv("CHUNK_SIZE", "500"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "50"))
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            docs = loader.load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap)
            chunks = splitter.split_documents(docs)
            all_docs.extend(chunks)
    return all_docs
