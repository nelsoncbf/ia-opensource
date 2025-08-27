import os
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

# Configurações
DATA_PATH = "./data"
CHROMA_PATH = "./chroma"

# LLM local
llm = OllamaLLM(model="llama3", base_url="http://ollama:11434")

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
embedding = embeddings.embed_query("Teste de embedding")
print(embedding[:5])  # Mostra os primeiros valores do vetor


# Vector store
vectordb = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

# Carregar documentos
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
        # Ignora .docx e outros formatos não contemplados
    return documentos

docs = carregar_documentos(DATA_PATH)
print(f"Documentos carregados: {len(docs)}")

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)
vectordb.add_documents(chunks)

if chunks:
    vectordb.add_documents(chunks)
else:
    print("Nenhum chunk gerado. Verifique os documentos ou o splitter.")

# Consulta
query = "Explique o conteúdo dos documentos"
results = vectordb.similarity_search(query, k=3)
context = "\n".join([doc.page_content for doc in results])
answer = llm(f"Com base no contexto: {context}\n\nPergunta: {query}")
print(answer)