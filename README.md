# 🧠 Chatbot Inteligente – Tienda Alemana

Este es el backend del proyecto obligatorio de Inteligencia Artificial para la materia, desarrollado con **FastAPI**, **LangChain** y **Ollama**. El sistema implementa una arquitectura **RAG (Retrieval-Augmented Generation)** que responde preguntas frecuentes sobre productos, góndolas y sucursales de la Tienda Alemana, a partir de documentos PDF oficiales.

---

## 🔗 Repositorio GitHub

https://github.com/nachitog01/obligatorio-chatbot

---

## 🚀 ¿Qué hace este proyecto?

Procesa tres documentos PDF:

- Catálogo de productos (precios, stock)
- Ubicación física de productos (secciones y góndolas)
- Información general de las sucursales (horarios, direcciones)

Permite hacer preguntas como:

- ¿Dónde encuentro el arroz de 1kg?
- ¿Cuánto cuesta la leche entera?
- ¿Hasta qué hora abre la sucursal de Carrasco?

---

## ⚙️ Tecnologías utilizadas

- **FastAPI** – Web API backend  
- **LangChain** – Encargado de manejar la arquitectura RAG  
- **ChromaDB** – Vector store local para almacenamiento semántico  
- **Ollama** – Modelo LLM local (`llama3.2`) para embeddings y respuestas  
- **dotenv** – Para manejo de configuración  

---

## 🧵 ¿Cómo se procesaron los PDFs?

- Se utilizó PyPDFLoader desde `langchain_community.document_loaders` para cargar los documentos.
- El contenido fue separado en chunks de tamaño 500 y solapamiento 50 usando RecursiveCharacterTextSplitter.
- Se utilizó Chroma como vector store para almacenar los embeddings.
- Los embeddings se generaron usando OllamaEmbeddings, configurado para usar el modelo local definido por `.env`.
- El pipeline se construyó con ConversationalRetrievalChain y el modelo se ejecuta vía `ollama`.

---

## 📁 Estructura del proyecto

obligatorio-chatbot/  
├── main.py                # API FastAPI  
├── utils/  
│   ├── pdf_loader.py  
│   ├── vector_store.py  
│   └── rag_pipeline.py  
├── data/  
│   ├── Catalogo.pdf  
│   ├── Ubicacion.pdf  
│   └── Locales.pdf  
├── requirements.txt  
├── .env.txt               # Plantilla de entorno  
└── .gitignore  

---

## 📘 Endpoints

### POST /ask

**Input:** JSON con una pregunta.  
Ejemplo:

{ "question": "¿Dónde encuentro el yogur de frutilla?" }

**Output:** Respuesta generada por el modelo basada en los documentos cargados.

---

## 🧪 Cómo correr el proyecto localmente

1. Instalar dependencias:

    pip install -r requirements.txt

2. Crear el archivo `.env`:

    cp .env.txt .env

3. Revisar el contenido de `.env`:

    OLLAMA_MODEL=llama3.2  
    OLLAMA_URL=http://localhost:11434  
    CHUNK_SIZE=500  
    CHUNK_OVERLAP=50  

4. Correr Ollama con el modelo:

    ollama pull llama3.2  
    ollama run llama3.2  

5. Levantar el backend:

    python3 -m uvicorn main:app --reload

6. Probar desde Swagger:

    Visitar http://localhost:8000/docs

---

## 📌 Notas

- El campo `chat_history` se pasa vacío, pero permite escalabilidad para mantener contexto en futuras versiones.
- El archivo `.env` real no se sube. Solo se entrega `.env.txt` como plantilla.
- El modelo debe estar corriendo localmente antes de iniciar la API.

---

## ✍️ Autores

- Ignacio García – 255389  
- Violeta Clerc – 233379  
- Ignacio Azaretto – 243242
