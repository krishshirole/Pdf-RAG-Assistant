import os
import streamlit as st

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma


load_dotenv()


# --------------------------------------------------
# GET OPENROUTER API KEY
# --------------------------------------------------

def get_api_key():

    # For local development (.env)
    api_key = os.getenv("OPENROUTER_API_KEY")

    # For Streamlit Cloud
    if not api_key:

        try:
            api_key = st.secrets["OPENROUTER_API_KEY"]

        except Exception:
            api_key = None

    if not api_key:

        raise Exception(
            "OPENROUTER_API_KEY is missing. "
            "Add it to your .env file or Streamlit Secrets."
        )

    return api_key


# --------------------------------------------------
# LOAD PDF
# --------------------------------------------------

def load_pdf(pdf_path, filename):

    try:

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        if not documents:
            raise Exception(
                "PDF contains no readable content."
            )

        for document in documents:
            document.metadata["source"] = filename

        return documents

    except Exception as e:

        raise Exception(
            f"PDF loading error for '{filename}': {e}"
        )


# --------------------------------------------------
# SPLIT DOCUMENTS
# --------------------------------------------------

def split_documents(documents):

    try:

        if not documents:
            raise Exception(
                "No documents available for splitting."
            )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(
            documents
        )

        if not chunks:
            raise Exception(
                "No chunks were created from the PDF."
            )

        return chunks

    except Exception as e:

        raise Exception(
            f"Text splitting error: {e}"
        )


# --------------------------------------------------
# CREATE VECTOR DATABASE
# --------------------------------------------------

def create_vectorstore(chunks):

    try:

        api_key = get_api_key()

        embeddings = OpenAIEmbeddings(

            model="openai/text-embedding-3-small",

            openai_api_key=api_key,

            base_url="https://openrouter.ai/api/v1"
        )

        vectorstore = Chroma.from_documents(

            documents=chunks,

            embedding=embeddings,

            persist_directory="./chroma_db"
        )

        return vectorstore

    except Exception as e:

        raise Exception(
            f"Embedding / ChromaDB error: {e}"
        )


# --------------------------------------------------
# SEARCH DOCUMENTS
# --------------------------------------------------

def search_documents(
    vectorstore,
    question,
    selected_pdfs
):

    try:

        if not question.strip():
            raise Exception(
                "Question cannot be empty."
            )

        if not selected_pdfs:
            raise Exception(
                "No PDFs were selected."
            )

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

    except Exception as e:

        raise Exception(
            f"Vector search error: {e}"
        )


# --------------------------------------------------
# GENERATE ANSWER
# --------------------------------------------------

def generate_answer(
    question,
    documents
):

    try:

        api_key = get_api_key()

        if not documents:

            raise Exception(
                "No relevant documents were found."
            )

        llm = ChatOpenAI(

            model="openai/gpt-4o-mini",

            api_key=api_key,

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

        if not response:

            raise Exception(
                "LLM returned an empty response."
            )

        return response.content

    except Exception as e:

        raise Exception(
            f"OpenRouter LLM API error: {e}"
        )