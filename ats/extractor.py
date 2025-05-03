import pymupdf
import logging


def extract_text_from_pdf(pdf_file):
    try:
        text = ""
        doc = pymupdf.open(stream=pdf_file.read(), filetype = "pdf")
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        logging.error(f"Failed to extract text from the PDF: {e}")
        return ""
    
