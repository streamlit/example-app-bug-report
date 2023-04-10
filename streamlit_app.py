import streamlit as st

from utils.sheets import connect_to_gsheet
from widgets import sidebar, form, expander

st.set_page_config(page_title="Cadastro de ficha financeira", page_icon="📄", layout="centered")
st.title("📄 Cadastro de ficha financeira")

gsheet_connector = connect_to_gsheet()

sidebar.create()
file = form.create(gsheet_connector)
expander.create_sheets_view(gsheet_connector)
expander.create_extraction_views(file)