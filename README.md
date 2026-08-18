Absolutely. Below is the **complete `README.md` in one single block**. You can copy everything inside the block and paste it directly into your `README.md`.

````markdown
# 📚 PDF RAG Assistant

A beginner-friendly **Retrieval-Augmented Generation (RAG)** application built with **Python, Streamlit, LangChain, ChromaDB, and OpenRouter**.

This project allows users to upload multiple PDF files, select which PDFs they want to search, and ask questions about their documents using a RAG pipeline.

The project is intentionally kept small and simple so beginners can understand how a basic RAG system works.

---

## ✨ Features

- 📄 Upload multiple PDF files
- 🔎 Select which PDFs should be searched
- 🧠 Generate embeddings from PDF content
- 🗄️ Store embeddings in ChromaDB
- 🔍 Perform semantic search
- 🤖 Generate answers using an LLM
- 📚 Display source PDF and page number
- 🔐 API key stored securely using `.env`
- 🌐 Uses OpenRouter API
- 🐍 Python backend
- 🎨 Streamlit interface

---

# 🧠 How RAG Works

The application follows this pipeline:

```text
                         PDF FILES
                             │
                             ▼
                    PDF Text Extraction
                             │
                             ▼
                          Chunking
                             │
                             ▼
                         Embeddings
                             │
                             ▼
                      ChromaDB
                   Vector Database
                             │
                             │
                   User selects PDFs
                             │
                             ▼
                       User Question
                             │
                             ▼
                      Query Embedding
                             │
                             ▼
                     Semantic Search
                             │
                             ▼
                    Relevant PDF Chunks
                             │
                             ▼
                            LLM
                             │
                             ▼
                       Final Answer
                             │
                             ▼
                         Sources
````

---

# 🛠️ Technologies Used

| Technology                     | Purpose               |
| ------------------------------ | --------------------- |
| Python                         | Backend               |
| Streamlit                      | User Interface        |
| LangChain                      | RAG framework         |
| PyPDF                          | PDF text extraction   |
| RecursiveCharacterTextSplitter | Text chunking         |
| OpenRouter                     | LLM and embedding API |
| ChromaDB                       | Vector database       |
| python-dotenv                  | Environment variables |

---

# 📋 Requirements

Before starting, make sure you have:

* Python 3.10 or newer
* Git
* An OpenRouter API key
* Internet connection

Check Python:

```bash
python --version
```

Check Git:

```bash
git --version
```

---

# 🚀 Use This Project Directly

You can copy this project and use it as your own local RAG application.

## 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/krishshirole/pdf-rag-assistant.git
```


Then move into the project:

```bash
cd pdf-rag-assistant
```

---

# 🐍 2. Create a Virtual Environment

Creating a virtual environment is recommended so that the project's dependencies don't interfere with other Python projects.

## Windows

Create the environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

at the beginning of your terminal.

## macOS / Linux

Create the environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# 📦 3. Install Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

The project uses packages such as:

```text
streamlit
langchain
langchain-community
langchain-openai
langchain-chroma
langchain-text-splitters
pypdf
python-dotenv
```

---

# 🔑 4. Configure OpenRouter API

The OpenRouter API key is **NOT included in this repository** for security reasons.

You need to create your own `.env` file.

Inside the project directory, create:

```text
.env
```

Your project should look like:

```text
pdf-rag-assistant/
│
├── .env
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

Inside `.env`, add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Replace:

```text
your_openrouter_api_key_here
```

with your actual OpenRouter API key.

---

# 🌐 5. Get an OpenRouter API Key

Go to:

[https://openrouter.ai/](https://openrouter.ai/)

Create an account and generate an API key.

Your key will look similar to:

```text
sk-or-v1-xxxxxxxxxxxxxxxx
```

Put the key inside:

```text
.env
```

Example:

```env
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxx
```

## ⚠️ Important

Never share your API key.

Never put your API key directly inside Python code.

Do NOT do this:

```python
OPENROUTER_API_KEY = "sk-or-v1-xxxxxxxx"
```

Instead, store it in `.env`.

The application reads the key using:

```python
os.getenv("OPENROUTER_API_KEY")
```

---

# 🔐 6. Files Not Included in GitHub

Some files are intentionally not included in this repository.

They are:

```text
.env
venv/
chroma_db/
__pycache__/
```

These files are either sensitive, generated automatically, or unnecessary to upload.

---

## `.env`

Contains your private OpenRouter API key.

Example:

```env
OPENROUTER_API_KEY=your_api_key
```

This file must remain local.

It should never be pushed to GitHub.

---

## `venv/`

This contains your local Python virtual environment and installed packages.

It is not necessary to upload it.

Every user can create their own environment using:

```bash
python -m venv venv
```

and install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## `chroma_db/`

This is the local ChromaDB vector database.

It is generated automatically when you build the knowledge base.

You do NOT need to download or create it manually.

The application will create it automatically.

---

## `__pycache__/`

Python automatically creates this directory when running Python programs.

It is not required by the project.

---

# 📄 7. Add Your PDFs

You don't need to place your PDFs inside the project directory.

The application allows you to upload them directly through the Streamlit interface.

For example:

```text
AI.pdf
Machine_Learning.pdf
Python.pdf
Cybersecurity.pdf
```

You can upload multiple PDFs at the same time.

---

# ▶️ 8. Run the Application

After creating `.env` and installing the dependencies, run:

```bash
streamlit run app.py
```

Streamlit will start a local web server.

You should see something similar to:

```text
Local URL: http://localhost:8501
```

Open that URL in your browser.

---

# 📚 9. How to Use the Application

## Step 1 — Upload PDFs

Upload one or multiple PDF files.

For example:

```text
AI.pdf
ML.pdf
Python.pdf
Cybersecurity.pdf
```

---

## Step 2 — Select PDFs

Choose which PDFs you want the RAG system to search.

Example:

```text
☑ AI.pdf
☑ ML.pdf
☐ Python.pdf
☐ Cybersecurity.pdf
```

The system will search only the selected PDFs.

---

## Step 3 — Build Knowledge Base

Click:

```text
Build Knowledge Base
```

The application will process the PDFs:

```text
PDF
 ↓
Extract Text
 ↓
Split Text Into Chunks
 ↓
Generate Embeddings
 ↓
Store Embeddings
 ↓
ChromaDB
```

A `chroma_db` directory will automatically be created.

---

## Step 4 — Ask a Question

Enter a question such as:

```text
What is supervised learning?
```

The RAG system will:

```text
Question
   ↓
Query Embedding
   ↓
ChromaDB
   ↓
Semantic Search
   ↓
Relevant PDF Chunks
   ↓
LLM
   ↓
Answer
```

---

# 🔎 10. Example

Suppose you upload:

```text
AI.pdf
Python.pdf
Cybersecurity.pdf
```

Then select:

```text
☑ AI.pdf
☐ Python.pdf
☐ Cybersecurity.pdf
```

Ask:

```text
What is artificial intelligence?
```

The system will search only:

```text
AI.pdf
```

It will retrieve relevant chunks and send them to the LLM.

The result will contain an answer along with the source.

Example:

```text
Answer:

Artificial intelligence is...

Sources:

📄 AI.pdf — Page 5
📄 AI.pdf — Page 12
```

---

# 📁 11. Project Structure

After cloning the repository, the project initially looks like:

```text
pdf-rag-assistant/
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

After you create your environment and run the application:

```text
pdf-rag-assistant/
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── .env
├── venv/
│
└── chroma_db/
```

Remember:

```text
.env          → Local only
venv/         → Local only
chroma_db/    → Generated locally
```

---

# 📄 12. File Explanation

## `app.py`

Contains the Streamlit frontend.

It handles:

* PDF upload
* PDF selection
* Knowledge base creation
* User questions
* Displaying answers
* Displaying sources

---

## `rag.py`

Contains the main RAG backend.

It handles:

```text
PDF Loading
     ↓
Text Chunking
     ↓
Embeddings
     ↓
ChromaDB
     ↓
Semantic Search
     ↓
LLM Generation
```

---

## `requirements.txt`

Contains all required Python dependencies.

Install them using:

```bash
pip install -r requirements.txt
```

---

## `.env`

Stores your private OpenRouter API key.

Example:

```env
OPENROUTER_API_KEY=your_api_key
```

This file is intentionally excluded from GitHub.

---

## `.gitignore`

Prevents sensitive and unnecessary files from being uploaded to GitHub.

Example:

```text
venv/
.env
__pycache__/
chroma_db/
```

---

# 🧠 13. RAG Concepts Demonstrated

This project demonstrates the fundamental components of Retrieval-Augmented Generation.

## 1. Document Loading

```text
PDF → Text
```

The PDF loader extracts text from PDF files.

---

## 2. Text Chunking

Large documents are divided into smaller pieces.

```text
Large Document
      ↓
Chunk 1
Chunk 2
Chunk 3
...
```

---

## 3. Embeddings

Text is converted into numerical vectors.

```text
Text
 ↓
Embedding Model
 ↓
Vector
```

These vectors represent the semantic meaning of the text.

---

## 4. Vector Database

The vectors are stored in ChromaDB.

```text
Chunk
 ↓
Embedding
 ↓
ChromaDB
```

---

## 5. Retrieval

When the user asks a question:

```text
Question
 ↓
Query Embedding
 ↓
Similarity Search
 ↓
Relevant Chunks
```

---

## 6. Augmentation

The retrieved chunks are added to the user's question.

```text
Question
+
Retrieved Context
```

---

## 7. Generation

The LLM receives the context and question and generates the final response.

```text
Context + Question
        ↓
       LLM
        ↓
     Answer
```

---

# 🏗️ 14. Complete RAG Architecture

```text
                    ┌──────────────┐
                    │  PDF Files   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │ PDF Loader   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │   Chunking   │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Embeddings  │
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  ChromaDB    │
                    └──────┬───────┘
                           │
                           │
                    User Question
                           │
                           ▼
                    ┌──────────────┐
                    │   Retrieval  │
                    └──────┬───────┘
                           │
                           ▼
                  Relevant PDF Chunks
                           │
                           ▼
                    ┌──────────────┐
                    │     LLM      │
                    └──────┬───────┘
                           │
                           ▼
                    Generated Answer
                           │
                           ▼
                       Sources
```

---

# 🔐 15. Security

Never commit API keys to GitHub.

If you accidentally expose your OpenRouter API key:

1. Immediately revoke the exposed key.
2. Generate a new API key.
3. Update your `.env`.
4. Make sure the old key is removed from the repository history if it was committed.

Deleting the `.env` file in a new commit is not enough if the key already exists in Git history.

---

# 🧹 16. Reset the Vector Database

If you want to completely rebuild the knowledge base, stop the application and delete:

```text
chroma_db/
```

Then start the application again:

```bash
streamlit run app.py
```

Build the knowledge base again.

---

# 🔄 17. Complete Setup From Scratch

Anyone can reproduce this project using the following commands.

```bash
git clone https://github.com/YOUR_USERNAME/pdf-rag-assistant.git

cd pdf-rag-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create:

```text
.env
```

Add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Run:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

# 🚀 18. Possible Future Improvements

This project can be extended with:

* 💬 Chat history
* 🧠 Conversation memory
* 🎯 Better retrieval
* 🔎 MMR retrieval
* 📊 Similarity scores
* 📚 Better source citations
* 🗑️ Add/remove documents
* ⚡ Avoid duplicate embeddings
* 📈 Retrieval evaluation
* 🌐 Web search
* 🕸️ LangGraph
* 🤖 Agentic RAG
* 🔐 RAG security
* 📈 RAG evaluation
* 🚀 Cloud deployment
* 👥 Multi-user support

---

# 🤝 19. Contributing

Feel free to fork this repository and experiment with the project.

You can improve:

* Retrieval
* Chunking
* Prompt engineering
* UI
* Document processing
* Vector database
* LLM integration
* Source citations
* Performance

Pull requests and improvements are welcome.

---

# ⭐ 20. Support

If this project helped you understand how RAG works, consider giving the repository a ⭐ on GitHub.

---

# 📜 License

This project is intended for educational purposes.

If you plan to distribute this project publicly, add an appropriate open-source license such as MIT.

---

# 👨‍💻 Author

Built as a beginner-friendly implementation of a Retrieval-Augmented Generation system using Python and LangChain.

---

## ⭐ Quick Start

If you already have Python and Git installed:

```bash
git clone https://github.com/YOUR_USERNAME/pdf-rag-assistant.git

cd pdf-rag-assistant

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env`:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Then:

```bash
streamlit run app.py
```

Upload PDFs → Select PDFs → Build Knowledge Base → Ask Questions 🚀

````

### After pasting it

Just change this wherever it appears:

```text
https://github.com/YOUR_USERNAME/pdf-rag-assistant.git
````

to your actual repository URL.

Then:

```bash
git add README.md
git commit -m "Add README documentation"
git push
```

Your GitHub repo will then be usable by someone else with essentially:

```bash
git clone YOUR_REPO_URL
cd pdf-rag-assistant
pip install -r requirements.txt
```

create `.env`, and run:

```bash
streamlit run app.py
```
