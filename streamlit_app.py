from io import StringIO
import json
import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest

from utils.pdf import text_extractor
from utils.gpt import get_model_list, get_json_from_gpt

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1h6G7_T2T88Lh5rottS8DYV-ieqIqHZCbfn3HoW1NTPw"
SHEET_NAME = "Sheet1"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"


@st.experimental_singleton()
def connect_to_gsheet():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )

    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector


def get_data(gsheet_connector) -> pd.DataFrame:
    values = (
        gsheet_connector.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:E",
        )
        .execute()
    )

    df = pd.DataFrame(values["values"])
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def add_row_to_gsheet(gsheet_connector, row) -> None:
    gsheet_connector.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=f"{SHEET_NAME}!A:E",
        body=dict(values=row),
        valueInputOption="USER_ENTERED",
    ).execute()


st.set_page_config(page_title="Cadastro de ficha financeira", page_icon="📄", layout="centered")

st.title("📄 Cadastro de ficha financeira")

gsheet_connector = connect_to_gsheet()

st.sidebar.write(
    f"Este aplicativo recebe uma ficha financeira emitida pelo Vista Office e submete os dados para o Arena."
)

st.sidebar.write(
    f"O projeto faz uso de um leitor de PDFs e do ChatGPT para ler e moldar os dados no formato correto."
)

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
        gsheet_connector,
        [[contract]],
    )
    st.success("Obrigado! A ficha foi recebida.")
    st.balloons()

expander = st.expander("Veja os registros")
with expander:
    st.write(f"Open original [Google Sheet]({GSHEET_URL})")
    st.dataframe(get_data(gsheet_connector))


if file is not None:
    another_expander = st.expander("Veja o texto extraído do PDF")
    with another_expander:
        file_text = text_extractor(file.getvalue())
        st.text(file_text)

    yet_another_expander = st.expander("Veja a estrutura gerada pelo GPT")
    with yet_another_expander:
        #st.text(get_model_list(st.secrets["openai"]["openai_api_key"], st.secrets["openai"]["openai_org_id"]))
        gpt_json = get_json_from_gpt(st.secrets["openai"]["openai_api_key"], 
                                     st.secrets["openai"]["openai_org_id"], 
                                     file_text
        )
        
        st.text(json.dumps(gpt_json, indent=2))
