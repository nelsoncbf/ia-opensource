import os
import requests
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    UnstructuredMarkdownLoader
)

# 🔧 Configurações
DATA_PATH = "./data"
CHROMA_PATH = "./chroma"

# 🔮 Inicializa o modelo LLM via Ollama
llm = OllamaLLM(
    model="mistral",
    temperature=0.2,
    base_url="http://ollama:11434",  # Altere para "http://ollama:11434" se estiver em Docker
    system="Responda de forma direta e concisa.",
    streaming=True
)

# 🧠 Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 🗂️ Carregamento de documentos
def carregar_documentos(path):
    documentos = []
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)

        if filename.endswith(".txt"):
            documentos += TextLoader(filepath).load()
        elif filename.endswith(".pdf"):
            documentos += PyPDFLoader(filepath).load()
        elif filename.endswith(".csv"):
            documentos += CSVLoader(filepath).load()
        elif filename.endswith(".md"):
            documentos += UnstructuredMarkdownLoader(filepath).load()
    return documentos

# 📚 Processamento inicial
documentos = carregar_documentos(DATA_PATH)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documentos)

# 🧱 Criação do banco vetorial
vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
if chunks:
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
else:
    print("Nenhum chunk gerado. Verifique os documentos ou o splitter.")


# 🔍 Função de consulta
def responder(prompt):
    resultados = vectordb.similarity_search(prompt, k=3)
    contexto = "\n".join([doc.page_content for doc in resultados])
    resposta = llm.invoke(f"Com base no contexto:\n{contexto}\n\nPergunta: {prompt}")
    return resposta, contexto

# deixando modelo ativo antes de subir o app
# def modelo_ativo():
#     try:
#         res = requests.get("http://localhost:11434")
#         return res.status_code == 200
#     except:
#         return False

# if not modelo_ativo():
#     st.error("O modelo ainda está carregando. Tente novamente em alguns segundos.")
#     st.stop()


# 🌐 Interface Streamlit
st.set_page_config(page_title="Chat com Mistral", layout="centered")
st.title("🔎 Chat com Mistral via Ollama")

prompt = st.text_area("Digite sua pergunta:", height=150)

if st.button("Enviar"):
    with st.spinner("Consultando o modelo..."):
        resposta, contexto = responder(prompt)
        st.subheader("🧠 Resposta:")
        st.write(resposta)

        st.subheader("📄 Contexto usado:")
        st.write(contexto)