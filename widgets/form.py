import streamlit as st
from utils.sheets import add_row_to_gsheet

def create(sheets_connector):
    form = st.form(key="annotation")
    with form:
        cols = st.columns((1, 1))
        contract = cols[0].text_input("Número do contrato:")
        cols = st.columns(1)
        file = st.file_uploader(
            label="Enviar a ficha financeira do Vista Office",
            type="pdf",
            help="Precisa ser o arquivo pdf da ficha financeira gerada pelo Vista Office",
        )
        submitted = st.form_submit_button(label="Submit")

    if submitted:
        add_row_to_gsheet(
            sheets_connector,
            [[contract]],
        )
        st.success("Obrigado! A ficha foi recebida.")
        return file