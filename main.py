import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from utils.pdf_loader import load_documents
from utils.vector_store import create_vector_store
from utils.rag_pipeline import get_rag_chain

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")  # ✔️ el modelo que realmente estás usando

docs = load_documents("data/")
vectorstore = create_vector_store(docs)
rag_chain = get_rag_chain(vectorstore, model=OLLAMA_MODEL)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: AskRequest):
    response = rag_chain.invoke({
    "question": request.question,
    "chat_history": []
})

    return {"answer": response}

@app.get("/")
def read_root():
    return {"message": "Chatbot RAG Tienda Alemana"}
