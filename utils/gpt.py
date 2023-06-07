import json
import openai
import streamlit as st

def get_model_list(api_key: str, org_id: str) -> None:
    openai.organization = org_id
    openai.api_key = api_key
    return openai.Model.list()

@st.cache_data
def ask_gpt(api_key: str, org_id: str, prompt: str, text: str) -> str:
    openai.organization = org_id
    openai.api_key = api_key
    response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt + "\n" + f"'''{text}'''",
                    max_tokens=1200,
                    temperature=0
                )
    
    resp_json = json.loads(str(response))
    resp_content = str(resp_json["choices"][0]["text"]).strip()

    return resp_content