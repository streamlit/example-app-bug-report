import streamlit as st
from utils.sheets import add_row_to_gsheet
from config.categories import documents

def create_upload():
    form = st.form(key="files_upload")
    with form:
        cols = st.columns((1, 1))
        contract = cols[0].text_input("Código do contrato:", key="codigo_contrato")
        cols = st.columns(1)
        
        files = st.file_uploader(
            label="Enviar todos os documentos de uma vez",
            type="pdf",
            help="Todos os arquivos precisam ser PDF. No próximo passo, deve categorizar os arquivos.",
            accept_multiple_files=True,
            key="arquivos_dd"
        )

        submitted = st.form_submit_button(label="Enviar arquivos")

    if submitted:
        st.success("Documentos recebidos! Agora diga que documentos são esses:")
        return files
    

def create_categorize(files):
    form = st.form(key="files_categorize")
    with form:

        st.text(f"Preencha as categorias dos {len(files)} arquivos:")
        
        categories = []
        option_list = ["Escolha..."]
        option_list.extend([documents[doc]['name'] for doc in documents.keys()])
        new_option_list = [k for k in documents.keys()]

        for file in files:
            category = st.selectbox(
                label=f"{file.name}",
                # options=["Escolha...", "Certidão negativa PF", "Matrícula do imóvel", "Débitos trabalhistas"],
                options=new_option_list,
                format_func=(lambda o: documents[o]['name']),
                key=f"category-{file.name.lower()}",
            )
            categories.append(category)

        submitted = st.form_submit_button(label="Categorizar e inicar processamento")

    if submitted:
        st.success("Categorias registradas. Iniciando processamento...")
        if 'categories' not in st.session_state:
            st.session_state['categories'] = categories
        return categories