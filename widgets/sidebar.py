import streamlit as st

def create():
    st.sidebar.write(
        f"Este aplicativo recebe uma ficha financeira emitida pelo Vista Office e submete os dados para o Arena."
    )

    st.sidebar.write(
        f"O projeto faz uso de um leitor de PDFs e do ChatGPT para ler e moldar os dados no formato correto."
    )