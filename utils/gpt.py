import json
import openai

def get_model_list(api_key: str, org_id: str) -> None:
    openai.organization = org_id
    openai.api_key = api_key
    return openai.Model.list()


def get_json_from_gpt(api_key: str, org_id: str, text: str) -> json:
    openai.organization = org_id
    openai.api_key = api_key
    response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt="Return a json from the text below.\n" +
                    f"'''{text}'''",
                    max_tokens=1200,
                    temperature=0
                )
    
    resp_json = json.loads(str(response))
    gpt_text = resp_json["choices"][0]["text"]
    gpt_json = json.loads("{" + gpt_text.split("{",1)[1]) #removes

    return gpt_json