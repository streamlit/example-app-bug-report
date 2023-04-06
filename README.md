# 📄 Cadastro de ficha financeira

Um formulário para cadastro da ficha financeira (.pdf) emitida pelo Vista Office, com o intuito de, no futuro, alimentar o Arena e o Pipefy de emissão de boletos.

Usa o ChatGPT (davinci) para formatar os dados obtidos do .pdf por meio do PyPDF2.

### Para rodar local:
instale as dependências com:
```pip install -r requirements.txt```

crie um arquivo `secrets.toml` na pasta `.streamlit` na raiz do projeto e insira suas credenciais lá
remova o versionamento dessa pasta no `.gitignore`

suba o serviço local com:
```streamlit run streamlit_app.py```
