# utils/pdf_parser.py
import fitz  # PyMuPDF

def extract_pages_from_pdf(filepath):
    doc = fitz.open(filepath)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append({
            "page_number": i + 1,
            "text": text.strip()
        })
    doc.close()
    return pages
