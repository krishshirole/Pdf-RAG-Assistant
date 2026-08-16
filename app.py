import streamlit as st
import tempfile

from rag import (
    load_pdf,
    split_documents,
    create_vectorstore,
    search_documents,
    generate_answer
)


st.title("📚 PDF RAG Assistant")

st.write(
    "Upload PDFs and ask questions about them."
)


uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)


if uploaded_files:

    pdf_names = [
        file.name
        for file in uploaded_files
    ]

    selected_pdfs = st.multiselect(
        "Choose PDFs to search",
        pdf_names
    )


    if st.button("Build Knowledge Base"):

        all_chunks = []

        for file in uploaded_files:

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".pdf"
            )

            temp_file.write(
                file.getvalue()
            )

            temp_file.close()


            documents = load_pdf(
                temp_file.name,
                file.name
            )

            chunks = split_documents(
                documents
            )

            all_chunks.extend(chunks)


        with st.spinner(
            "Creating knowledge base..."
        ):

            vectorstore = create_vectorstore(
                all_chunks
            )

            st.session_state.vectorstore = vectorstore


        st.success(
            "Knowledge base created!"
        )


if "vectorstore" in st.session_state:

    st.divider()

    st.subheader("🔎 Ask your PDFs")

    question = st.text_input(
        "Ask a question"
    )


    if question:

        if not selected_pdfs:

            st.warning(
                "Please select at least one PDF."
            )

        else:

            with st.spinner(
                "Searching PDFs..."
            ):

                documents = search_documents(
                    st.session_state.vectorstore,
                    question,
                    selected_pdfs
                )


            if not documents:

                st.warning(
                    "No relevant information found."
                )

            else:

                with st.spinner(
                    "Generating answer..."
                ):

                    answer = generate_answer(
                        question,
                        documents
                    )


                st.subheader("💡 Answer")

                st.write(answer)


                st.divider()

                st.subheader("📚 Sources")

                for document in documents:

                    source = document.metadata.get(
                        "source",
                        "Unknown"
                    )

                    page = document.metadata.get(
                        "page",
                        0
                    ) + 1

                    st.write(
                        f"📄 {source} — Page {page}"
                    )