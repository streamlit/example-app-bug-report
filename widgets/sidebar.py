import streamlit as st

def create():
    st.sidebar.write(
        f"Este aplicativo recebe os documentos da due diligence coletados e retorna uma pre-análise feita por IA."
    )

    st.sidebar.write(
        f"O projeto faz uso de um leitor de PDFs e do ChatGPT para ler e analisar o conteúdo a partir de prompts planejados."
    )