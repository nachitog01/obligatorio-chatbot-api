import os
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import Ollama

def get_rag_chain(vectorstore, model=None):
    if model is None:
        model = os.getenv("OLLAMA_MODEL", "llama3.2")

    llm = Ollama(model=model)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=False
    )
    return chain
