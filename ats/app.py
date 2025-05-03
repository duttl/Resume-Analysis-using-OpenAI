from extractor import extract_text_from_pdf
from llm_chatgpt import analyze_resume
from utils import setup_logging
import streamlit as st

def main():
    setup_logging()

    st.title("Resume analyzer for Job Description with OpenAI")

    job_description = st.text_area("Paste the Job Description")

    uploaded_files = st.file_uploader(
        "Upload one or more PDF resumes", accept_multiple_files=True, type=["pdf"]
    )

    if st.button("Analyze"):
        if not job_description:
            st.warning("Enter a job description")
        elif not uploaded_files:
            st.warning("Upload at least one resume.")
        else:
            for file in uploaded_files:
                st.subheader(f"Result for {file.name}")
                text = extract_text_from_pdf(file)
                if not text.strip():
                    st.error("Could not extract text from PDF.")
                    continue
                result = analyze_resume(text, job_description)
                st.write(result)

if __name__ == "__main__":
    main()