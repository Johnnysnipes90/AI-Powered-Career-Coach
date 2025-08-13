# app/utils/parser.py
import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file.file)
    text_chunks = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_chunks.append(page_text)
    return "\n".join(text_chunks).strip()
