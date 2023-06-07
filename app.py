import streamlit as st
import time

from widgets import form, sidebar, expander

from utils.dd_file import dd_contract, dd_file
from utils import pdf, gpt

from config.categories import documents


files = []
categories = []

st.set_page_config(page_title="Gepeto", page_icon="👴🏽", layout="centered")
st.title("👴🏽 Gepeto: pre-análise da DD")

sidebar.create()

files = form.create_upload()

if ('codigo_contrato' in st.session_state) and (len(st.session_state['arquivos_dd']) > 0):
    contrato = dd_contract(st.session_state['codigo_contrato'])
    contrato.set_files(st.session_state['arquivos_dd'])

if st.session_state['arquivos_dd']:
    form.create_categorize(st.session_state['arquivos_dd'])

if ('codigo_contrato' in st.session_state) and (len(st.session_state['arquivos_dd']) > 0):
    for filename in contrato.files.keys():
        contrato.files[filename].set_category(st.session_state[f"category-{filename.lower()}"])

if ('categories' in st.session_state) and (st.session_state['categories']):
    with st.spinner("Extraindo texto dos arquivos..."):
        time.sleep(2)
        for filename in contrato.files.keys():
            file = contrato.files[filename]
            readable_content = pdf.text_extractor(file.content)
            file.set_readable_content(readable_content)
            # st.text(file.extracted_content)

    with st.spinner("Coletando opinião do Gepeto..."):
        for filename in contrato.files.keys():
            time.sleep(2)
            # file = contrato.files[filename]
            
            prompt = documents[contrato.files[filename].category]['prompt'] + "\n" + documents[contrato.files[filename].category]['questions']

            output_key = f'output-{filename.lower()}'
            if output_key not in st.session_state:
                st.session_state[output_key] = gpt.ask_gpt(
                    api_key=st.secrets['openai']['openai_api_key'],
                    org_id=st.secrets['openai']['openai_org_id'],
                    prompt=prompt,
                    text=file.extracted_content
                )
            
            contrato.files[filename].set_ai_output(st.session_state[output_key])

            # st.text(f"{file.category} ({file.name}): {file.ai_output}")

    expander.create_table_view(contrato)
    