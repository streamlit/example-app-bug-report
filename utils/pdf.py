from io import BytesIO
from PyPDF2 import PdfReader
from datetime import datetime
import pandas as pd
import pdfkit as pdf

def text_extractor(file: bytes) -> str:
    # TODO read all the pages
    file_stream = BytesIO(file)
    pdf = PdfReader(file_stream)
    page = pdf.pages[0]
    text = page.extract_text()
    return str(text)


def generate_pdf_from_df(contract_id: str, df: pd.DataFrame) -> bytes:
    table = df.to_html(classes='mystyle').replace("\\n", "<br />")
        
    with open('df_style.css') as f:
        css = f.read()

    html_string = f"""
    <html>
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-type" content="text/html; charset=UTF-8">
    <title>Relatório da DD - {contract_id}</title>
    </head>
    <style>
        {css}
    </style>
    <body>
    <h1>Relatório informativo de due diligence</h1>
    <h2>Contrato - {contract_id}</h2>
    <p>Emitido em: {datetime.today().strftime('%Y-%m-%d %H:%M')}</p>
    <p>Versão: Gepeto v0.1</p>
        {table}
    </body>
    </html>
    """

    pdf_file = pdf.from_string(html_string)

    return pdf_file
