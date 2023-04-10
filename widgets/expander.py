import streamlit as st
import json

from utils.pdf import text_extractor
from utils.sheets import get_data, GSHEET_URL
from utils.gpt import get_json_from_gpt

def create_sheets_view(sheets_connector):
    expander = st.expander("Veja os registros")
    with expander:
        st.write(f"Open original [Google Sheet]({GSHEET_URL})")
        st.dataframe(get_data(sheets_connector))

def create_extraction_views(file):

    if file is not None:
        another_expander = st.expander("Veja o texto extraído do PDF")
        with another_expander:
            file_text = text_extractor(file.getvalue())
            st.text(file_text)

        yet_another_expander = st.expander("Veja a estrutura gerada pelo GPT")
        with yet_another_expander:
            gpt_json = get_json_from_gpt(st.secrets["openai"]["openai_api_key"], 
                                        st.secrets["openai"]["openai_org_id"], 
                                        file_text
            )
            st.text(json.dumps(gpt_json, indent=2))