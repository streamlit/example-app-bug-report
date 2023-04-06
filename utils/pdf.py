from io import BytesIO
from PyPDF2 import PdfReader

def text_extractor(file: bytes) -> str:
    file_stream = BytesIO(file)
    pdf = PdfReader(file_stream)
    page = pdf.pages[0]
    text = page.extract_text()
    return str(text)