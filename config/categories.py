FICHA_FINANCEIRA_PROMPT_TEXT_TO_JSON = """
Por favor, extraia um objeto JSON do texto abaixo, contendo as seguintes informações: 
nome e dados pessoais dos compradores e vendedores, 
endereço e dados cadastrais do imóvel, 
e a comissão dividida entre os corretores e agências envolvidos na transação. 
O texto é o conteúdo legível de um arquivo PDF independente que descreve uma transação imobiliária.
"""

documents = {
    "certidao_debitos_tributarios_federais_pf": {
        "name": "PF - Certidão de Débitos Tributários Federais",
        "target": "PF", # PJ, Imóvel
        "type": "text", #image
        "prompt": """Verifique no conteúdo da Certidão de Débitos Tributários a seguir e responda de forma objetiva com apenas 'sim' ou 'não'.""",
        "questions": """Constam débitos ou pendências tributárias em noma da pessoa a qual a certidão se refere?"""
    },
    "certidao_debitos_tributarios_estaduais_sp_pf": {
        "name": "PF - Certidão de Débitos Tributários Estaduais SP",
        "target": "PF",
        "type": "text",
        "prompt": """Verifique no conteúdo da Certidão de Débitos Tributários a seguir e responda de forma objetiva com apenas 'sim' ou 'não'.""",
        "questions": """Constam débitos ou pendências tributárias em noma da pessoa a qual a certidão se refere?"""
    },
    "certidao_debitos_tributarios_estaduais_nao_inscritos_sp_pf": {
        "name": "PF - Certidão de Débitos Tributários Estaduais Não Inscritos SP",
        "target": "PF",
        "type": "text",
        "prompt": """Verifique no conteúdo da Certidão de Débitos Tributários a seguir e responda de forma objetiva com apenas 'sim' ou 'não'.""",
        "questions": """Constam débitos declarados ou apurados pendentes de inscrição na dívida ativa?"""
    },
    "certidao_debitos_trabalhistas_pf": {
        "name": "PF - Certidão de Débitos Trabalhistas",
        "target": "PF",
        "type": "text",
        "prompt": """Verifique no conteúdo da Certidão de Débitos Trabalhistas a seguir e responda de forma objetiva com apenas 'sim' ou 'não'.""",
        "questions": """A pessoa consta como inadimplente no Banco Nacional de Devedores Trabalhistas?"""
    },
    "certidao_conjunta_debitos_tributos_mobiliarios_pf": {
        "name": "PF - Certidão Conjunta de Débitos de Tributos Mobiliários",
        "target": "PF",
        "type": "text",
        "prompt": """Verifique o conteúdo da Certidão Conjunta de Débitos de Tributos Mobiliários a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """Qual a situação fiscal do contribuinte referente aos créditos tributários inscritos e não inscritos em Dívida Ativa?"""
    },
    "serasa_pf": {
        "name": "PF - Serasa",
        "target": "PF",
        "type": "text",
        "prompt": """Verifique o conteúdo do documento extraído do Serasa, sistema de informações de crédito, a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """1- Há anotações negativas?
                    2- Em caso positivo da pergunta 1, qual a ocorrência, quantidade, valor e período?
                    3- O CPF pesquisado possui participação societária em empresa?
                    4- Em caso positivo da pergunta 3, qual a empresa, CNPJ, participação societária e unidade federativa (UF)?
                """
    },
    "cartao_cnpj_pj": {
        "name": "PJ - Cartão CNPJ",
        "target": "PJ",
        "type": "text",
        "prompt": """Verifique o conteúdo do documento extraído do Cartão do CNPJ, cadastro de informações de uma empresa, a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",        
        "questions": """
                    1- Qual o número de inscrição?
                    2- Qual o nome empresarial?
                    3- Qual o código e descrição da natureza jurídica?
                    4- Qual o Município e UF?
                    5- Qual a situação cadastral?
                    6- Qual o motivo da situação cadastral?
                    7- Qual a data da situação cadastral?
                """
    },
    "certidao_estadual_distribuicoes_civeis_falencias_pj": {
        "name": "PJ - Certidão Estadual de Distribuições Cíveis - Falências",
        "target": "PJ",
        "type": "text",
        "prompt": """Verifique o conteúdo do documento extraído da Certidão Estadual de Distribuições Cíveis - Falências a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """Consta como réu, requerido ou interessado nos registros de distribuições de pedidos de falência, concordatas, recuperações judiciais e extrajudiciais?"""
    },
    "certidao_regularidade_fgts_crf_pj": {
        "name": "PJ - Certidão Estadual de Distribuições Cíveis - Falências",
        "target": "PJ",
        "type": "text",
        "prompt": """Verifique o conteúdo do documento extraído da Certidão Estadual de Distribuições Cíveis - Falências a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """
                    1- Qual a situação da empresa identificada perante o Fundo de Garantia de Tempo de Serviço - FGTS e qual o prazo de validade da situação?
                    2- O empregador está cadastrado?
                """
    },
    "certidao_debitos_trabalhistas_sit_pj": {
        "name": "PJ - Certidão Negativa de Débitos Trabalhistas - SIT",
        "target": "PJ",
        "type": "text",
        "prompt": """Verifique o conteúdo do documento extraído da Certidão Negativa de Débitos Trabalhistas a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """Constam débitos decorrentes de autuações em face do empregador?"""
    },
    "matricula_imovel": {
        "name": "Imóvel - Matrícula",
        "target": "Imóvel",
        "type": "image",
        "prompt": """A partir do conteúdo a seguir, extraído de um documento digitalizado via software de OCR, relativo a matrícula de um imóvel, responda de forma extremamente objetiva às seguintes perguntas:""",
        "questions": """
                1- Qual é o número de matrícula do imóvel?
                2- Qual é o cartório de imóveis?
                3- Qual é o endereço do imóvel?
                4- Qual é a área privativa do imóvel?
                5- Qual é a área de uso comum prevista no documento?
                6- Há direito de uso de vaga de garagem?
                7- Qual é o número de contribuinte dos proprietários no documento?
                8- Quem são os proprietários ou adquirentes ou arrematantes ou herdeiros atuais constantes no documento?
                9- Qual o estado civil dos proprietários?
                10- Consta alguma indisponibilidade ou registro de que os bens dos proprietários estão indisponíveis?
                11- Caso positivo na pergunta 11, há cancelamento da indisponibilidade dos bens?
                12- Há usufruto na matrícula ou documento?
                13- Caso positivo na pergunta 12, foi cancelado?
                14- Consta algum processo ou ação de execução de título extrajudicial averbado na matrícula ou documento?
                15- Os proprietários deram o imóvel em alienação fiduciária ou hipoteca?
                16- Caso positivo na pergunta 15, foi autorizado o cancelamento da alienação fiduciária ou hipoteca?
                17- Há algum contrato de locação previsto no documento?
                18- Quais as datas dos registros de compra e venda constantes no documento?
            """
    },
    "certidao_dados_cadastrais_imovel": {
        "name": "Imóvel - Certidão de Dados Cadastrais",
        "target": "Imóvel",
        "type": "text",
        "prompt": """Verifique o conteúdo da Certidão de Dados Cadastrais de Imóvel e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """Qual o cadastro do imóvel?"""
    },
    "certidao_tributos_imobiliarios_imovel": {
        "name": "Imóvel - Certidão de Tributos Imobiliários",
        "target": "Imóvel",
        "type": "text",
        "prompt": """Verifique o conteúdo da Certidão de Tributos Imobiliários a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """Qual a situação fiscal do contribuinte referente aos créditos tributários inscritos e não inscritos em Dívida Ativa?"""
    },
    "consulta_debitos_iptu_imovel": {
        "name": "Imóvel - Consulta de Débitos de IPTU",
        "target": "Imóvel",
        "type": "text",
        "prompt": """Verifique o conteúdo da Consulta de Débitos de IPTU a seguir e responda de maneira extremamente objetiva as seguintes perguntas:""",
        "questions": """
                    1- Constam valores vencidos?
                    2- Quais os valores em aberto?
                    3- Existe alguma dívida de imóvel ascendente?
                """
    },
}