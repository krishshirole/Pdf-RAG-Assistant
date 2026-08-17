import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")

load_dotenv()


def load_pdf(pdf_path, filename):

    try:

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        for document in documents:
            document.metadata["source"] = filename

        return documents

    except FileNotFoundError:
        logger.error("Respective file not found")
        raise
    except ValueError:
        logger.error("Invalid file type")
        raise
    except Exception:
        logger.exception("Failed to load PDF: %s", pdf_path)
        raise


def split_documents(documents):

    try:

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        return splitter.split_documents(documents)

    except Exception:
        logger.exception("Failed to split documents")
        raise

def create_vectorstore(chunks):

    try:

        embeddings = OpenAIEmbeddings(
            model="openai/text-embedding-3-small",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )

        return vectorstore

    except Exception:
        logger.exception("Failed to create vectorstore")        
        raise


def search_documents(
    vectorstore,
    question,
    selected_pdfs
):

    try:
        results = vectorstore.similarity_search(
            question,
            k=4,
            filter={
                "source": {
                    "$in": selected_pdfs
                }
            }
        )

        return results

    except Exception:
        logger.exception("Failed to conduct similarity search")
        raise


def generate_answer(
    question,
    documents
):

 try:
    llm = ChatOpenAI(
        model="openai/gpt-4o-mini",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
Answer the user's question using only
the provided PDF context.

If the answer is not present in the context,
say that you could not find the answer
in the selected PDFs.

Context:

{context}

Question:

{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content

 except Exception:
     logger.exception("Failed to generate answer")
     raise