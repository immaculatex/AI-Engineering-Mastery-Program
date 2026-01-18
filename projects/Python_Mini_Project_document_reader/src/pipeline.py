from reader import read_pdf, read_docx
from cleaner import clean_text
from chunker import chunk_text

def process_document(file_path):
    if file_path.endswith(".pdf"):
        raw = read_pdf(file_path)
    elif file_path.endswith(".docx"):
        raw = read_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

    clean = clean_text(raw)
    chunks = chunk_text(clean)
    return chunks
