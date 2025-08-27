Claro, Nelson! Aqui está o conteúdo completo em **Markdown**, pronto para copiar e colar no seu repositório como `README.md`:

---

```markdown
# 🧠 RAG Open Source com Ollama, ChromaDB e LangChain

Este projeto implementa um pipeline de Recuperação Aumentada por Geração (RAG) utilizando tecnologias open source para criar uma aplicação de IA local, privada e extensível. Ele integra:

- **Ollama** para execução de modelos LLM localmente
- **ChromaDB** como banco vetorial para armazenamento e busca semântica
- **LangChain** para orquestração da lógica de RAG
- **Streamlit** como interface web interativa

Claro, Nelson! Aqui vai uma explicação mais acessível e didática de cada componente do seu projeto, ideal para quem não tem familiaridade com IA ou desenvolvimento:

---

## 🧠 Componentes do Projeto RAG

### 1. **Ollama – Motor de Inteligência Artificial Local**

O Ollama é como o "cérebro pensante" do sistema.  
Ele roda modelos de linguagem (LLMs) diretamente no seu computador, sem depender da internet ou de servidores externos. Esses modelos são capazes de entender perguntas, gerar respostas, resumir textos e muito mais — tudo de forma privada e rápida.

🔧 Exemplo de modelos que você pode usar: `llama2`, `mistral`, `gemma`.

---

### 2. **ChromaDB – Banco de Dados Inteligente**

O ChromaDB é um banco de dados especializado em lidar com **textos e significados**.  
Ao invés de guardar informações como uma planilha, ele transforma os textos em vetores (números que representam o sentido das palavras) e permite fazer buscas por **similaridade de conteúdo**.

💡 Isso significa que, mesmo que você não use as palavras exatas, ele entende o que você quer dizer e encontra os documentos mais relevantes.

---

### 3. **LangChain – Orquestrador da IA**

O LangChain é como o maestro da orquestra.  
Ele conecta todas as partes: pega os documentos, transforma em vetores, consulta o banco ChromaDB, envia a pergunta para o modelo do Ollama e junta tudo para gerar uma resposta inteligente.

🎯 Ele permite criar fluxos de raciocínio complexos, como:  
“Busque os documentos mais parecidos com a pergunta → envie para o modelo → gere uma resposta baseada nesses documentos.”

---

### 4. **Streamlit – Interface Visual para o Usuário**

O Streamlit é a "cara" do projeto — a interface que você vê no navegador.  
Ele transforma o código Python em uma página web interativa, onde você pode:

- Fazer perguntas
- Ver os documentos carregados
- Acompanhar as respostas da IA em tempo real

🌐 Tudo isso acessando [http://localhost:8501](http://localhost:8501) no seu navegador.

---

## 🚀 Como subir a aplicação

Certifique-se de ter o Docker e Docker Compose instalados.  
Depois, basta executar:

```bash
docker-compose up --build
```

Isso irá subir os três serviços principais:

| Serviço   | Porta | Descrição |
|-----------|-------|-----------|
| `ollama`  | 11434 | Servidor local de modelos LLM via Ollama |
| `chromadb`| 8000  | Banco vetorial para armazenamento de embeddings |
| `app`     | 8501  | Interface web via Streamlit + lógica RAG |

Acesse a aplicação em: [http://localhost:8501](http://localhost:8501)

---

## 🧩 Estrutura dos serviços

### 1. `ollama`

- **Imagem:** `ollama/ollama:latest`
- **Função:** Executa modelos LLM localmente (ex: `llama2`, `mistral`, `gemma`)
- **Porta:** `11434`
- **Persistência:** Volume `ollama_data` para armazenar os modelos baixados

### 2. `chromadb`

- **Imagem:** `chromadb/chroma:latest`
- **Função:** Armazena vetores de embeddings e realiza buscas semânticas
- **Porta:** `8000`
- **Persistência:** Volume local `./chroma`

### 3. `app`

- **Build local:** Usa o Dockerfile do projeto
- **Função:** Carrega documentos, gera embeddings, consulta o banco vetorial e interage com o modelo LLM
- **Porta:** `8501`
- **Volumes:**
  - `./data` → pasta onde os documentos devem ser inseridos
  - `./chroma` → compartilhamento com o banco vetorial

---

## 📂 Inserção de documentos

Coloque seus arquivos na pasta `./data`.  
Por padrão, o sistema carrega arquivos `.txt`, mas você pode adicionar suporte a:

- `.pdf` → via `PyPDFLoader`
- `.docx` → via `UnstructuredWordDocumentLoader`
- `.csv` → via `CSVLoader`
- `.md` → via `TextLoader`

Exemplo de instalação de dependências no `requirements.txt`:

```
langchain
chromadb
pypdf        # dependência .pdf
unstructured # dependencia .docx
streamlit
```

---

## 🛠️ Personalização

Você pode editar o `app.py` para:

- Escolher o modelo do Ollama (`llama2`, `mistral`, etc.)
- Ajustar o tipo de loader para suportar mais formatos
- Customizar o prompt de consulta
- Alterar o comportamento da interface Streamlit

---

## 📌 Requisitos

- Docker + Docker Compose
- Modelos Ollama já baixados (ou serão baixados na primeira execução)
- Documentos na pasta `data/` para alimentar o pipeline RAG

---

## 📞 Suporte

Se tiver dúvidas ou quiser expandir o projeto, sinta-se à vontade para abrir uma issue ou contribuir com melhorias!
```
