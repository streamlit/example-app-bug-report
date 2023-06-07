import streamlit as st
from datetime import datetime
from utils.dd_file import dd_contract
from utils.pdf import generate_pdf_from_df

import pdfkit as pdf

def create_table_view(contract: dd_contract) -> None:
    
    with st.expander("Veja o resultado da análise do Gepeto:"):
       
        df = contract.files_to_pandas()
        
        st.dataframe(df)

        st.download_button(
            label="Download do relatório",
            data=generate_pdf_from_df(contract.id, df),
            file_name=f"relatorio_dd_{contract.id}_{datetime.today().strftime('%Y%m%d%H%M')}.pdf"
        )
