from ats.extractor import extract_text_from_pdf
import io

def test_extract_text_from_pdf_handles_empty_file():
    fake_pdf = io.BytesIO(b"%PDF-1.4\n%EOF")
    result = extract_text_from_pdf(fake_pdf)
    assert isinstance(result, str)