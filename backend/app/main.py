import streamlit as st
from core import text_utils
from services import theme_service
from services.qa_service import QASystem  # Import QA system

st.set_page_config(page_title="Document Theme Identifier", page_icon="📄")
#setting the title of the page in streamlit
st.title("Document Research & Theme Identification Chatbot")

#to upload various types of files 
#allows users to upload files 
#PDF readers and OCR is used to convert these into texts 
uploaded_files = st.file_uploader(
    "Upload PDF or scanned image files (png, jpg, jpeg)",
    type=['pdf', 'png', 'jpg', 'jpeg'],
    accept_multiple_files=True
)
#extracting the texts from the file
all_texts = []
if uploaded_files:
    st.info(f"Extracting text from {len(uploaded_files)} files...")
    for file in uploaded_files:
        file_bytes = file.read()
        if file.type == "application/pdf":
            text = text_utils.extract_text_from_pdf(file_bytes)
        else:
            text = text_utils.extract_text_from_image(file_bytes)
        cleaned = text_utils.clean_text(text)
        all_texts.append(cleaned)
    st.success("Text extraction complete!")
#long texts are broken down into chunks for text cleaning and chunking
chunks = []
if all_texts:
    for text in all_texts:
        chunks.extend(text_utils.chunk_text(text))
    st.write(f"Total chunks created: {len(chunks)}")
#K-Means clustering is used to group similar chunks and each group is treated as a theme
if chunks:
    if st.button("Identify Themes Across Documents"):
        themes, _ = theme_service.identify_themes(chunks)
        st.markdown("### Identified Themes:")
        for idx, theme_chunks in enumerate(themes):
            st.markdown(f"### Theme {idx + 1}")
            for chunk in theme_chunks:
                st.write("- " + chunk)

    #questions can be asked from the uploaded documents
    #chunks are converted into embeddings
    #Stored in a searchable index
    # === Q&A FEATURE START ===
    qa_system = QASystem()
    qa_system.build_index(chunks)

    question = st.text_input("Ask a question about the uploaded documents:")
    if question:
        answers = qa_system.query(question)
        if answers:
            st.markdown("### Answers:")
            for ans in answers:
                st.write("- " + ans)
        else:
            st.write("No relevant answers found.")
    # === Q&A FEATURE END ===


