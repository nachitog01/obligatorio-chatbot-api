import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from utils.pdf_loader import load_documents
from utils.vector_store import create_vector_store
from utils.rag_pipeline import get_rag_chain
from langchain.schema import HumanMessage, AIMessage

load_dotenv()

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")

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

class QuestionRequest(BaseModel):
    question: str
    chat_history: list = []

@app.post("/ask")
async def ask_question(request: QuestionRequest):
    # Convertir el historial al formato que LangChain espera
    formatted_history = []
    for q, a in request.chat_history:
        formatted_history.append(HumanMessage(content=q))
        formatted_history.append(AIMessage(content=a))

    response = rag_chain.invoke({
        "question": request.question,
        "chat_history": formatted_history
    })
    return response

@app.get("/")
def read_root():
    return {"message": "Chatbot RAG Tienda Alemana"}
