import streamlit as st
import google.generativeai as genai

# Defina a chave de API do Google Generative AI
GENAI_API_KEY = "YOUR_GOOGLE_GENERATIVE_AI_API_KEY"

# Verificar se a chave de API está configurada
if not GENAI_API_KEY:
    st.error("A chave de API do Google Generative AI não está configurada. Por favor, forneça uma chave de API válida.")
else:
    genai.api_key = GENAI_API_KEY

# Função para gerar ideias de projetos de feira de ciências
def gerar_ideias(dados_usuario):
    if dados_usuario['metodologia'] == "Científica":
        prompt = f"""
        Como estudante do ensino {dados_usuario['ano_serie']}, estou empolgado em criar um projeto {dados_usuario['preferencia_projeto']} para participar de uma feira de ciência. Minha experiência com feira de ciência é {dados_usuario['participacao_anterior']}. Meu objetivo é desenvolver um projeto utilizando a metodologia científica para investigar um fenômeno ou problema específico ao longo de um período de 4 meses. Gostaria de abordar uma área que envolva {dados_usuario['area_conhecimento']}, com preferência por temas relacionados à {dados_usuario['tema_especifico']}, pois tenho interesse no {dados_usuario['motivacao']}. Sobre o conhecimento prévio sobre esse tema minha resposta é {dados_usuario['conhecimento_previo']}. Para desenvolver esse projeto pretendo fazer uso das minhas habilidades de {dados_usuario['habilidades']} e dos seguintes recursos {dados_usuario['recursos']}. Espero que ao final do projeto possa {dados_usuario['impacto']}. Gostaria ainda de acrescentar que {dados_usuario['informacao_adicional']}. Poderia me ajudar a criar uma lista contendo 5 ideias de projetos de feira de ciência que sejam interessantes e relevantes. As sugestões devem conter um título, objetivo e materiais e devem ser claras, concisas e adequadas ao {dados_usuario['ano_serie']} e {dados_usuario['tema_especifico']} escolhidos. Ao final ofereça recursos adicionais, como links para artigos científicos ou vídeos explicativos.
        """
    else:
        prompt = f"""
        Como estudante do ensino {dados_usuario['ano_serie']}, estou empolgado em criar um projeto {dados_usuario['preferencia_projeto']} para participar de uma feira de ciência. Minha experiência com feira de ciência é {dados_usuario['participacao_anterior']}. Meu objetivo é desenvolver um projeto utilizando a metodologia de engenharia para criar, construir e encontrar soluções para um problema ao longo de um período de 4 meses. Gostaria de abordar uma área que envolva {dados_usuario['area_conhecimento']}, com preferência por temas relacionados à {dados_usuario['tema_especifico']}, pois tenho interesse no {dados_usuario['motivacao']}. Sobre o conhecimento prévio sobre esse tema minha resposta é {dados_usuario['conhecimento_previo']}. Para desenvolver esse projeto pretendo fazer uso das minhas habilidades de {dados_usuario['habilidades']} e dos seguintes recursos {dados_usuario['recursos']}. Espero que ao final do projeto possa {dados_usuario['impacto']}. Gostaria ainda de acrescentar que {dados_usuario['informacao_adicional']}. Poderia me ajudar a criar uma lista contendo 5 ideias de projetos de feira de ciência que sejam interessantes e relevantes. As sugestões devem conter um título, objetivo e materiais e devem ser claras, concisas e adequadas ao {dados_usuario['ano_serie']} e {dados_usuario['tema_especifico']} escolhidos. Ao final ofereça recursos adicionais, como links para artigos científicos ou vídeos explicativos.
        """
    
    try:
        response = genai.generate_text(prompt=prompt)
        return response['choices'][0]['text'].strip()
    except Exception as e:
        st.error(f"Erro ao tentar gerar ideias: {e}")
        return None

# Configuração da aplicação Streamlit
st.title("Gerador de Ideias para Projetos de Feira de Ciências")

st.write("""
Este aplicativo utiliza a biblioteca Google Generative AI para ajudar a gerar ideias inovadoras para projetos de feira de ciências.
Preencha as informações abaixo para receber uma ideia personalizada!
""")

# Coletando informações do usuário
ano_serie = st.selectbox("Qual ano/série você está cursando?", ["6º Ano", "7º Ano", "8º Ano", "9º Ano", "1º Ano do Ensino Médio", "2º Ano do Ensino Médio", "3º Ano do Ensino Médio"])
preferencia_projeto = st.radio("Prefere realizar o projeto sozinho ou em equipe?", ["Sozinho", "Em equipe"])
participacao_anterior = st.radio("Já participou de outras feiras de ciência anteriormente?", ["Sim", "Não"])
projeto_anterior = st.text_input("Se sim, qual foi o seu projeto?", "") if participacao_anterior == "Sim" else "N/A"
metodologia = st.selectbox("Qual metodologia você pretende utilizar para o seu projeto?", ["Científica", "Engenharia"])
area_conhecimento = st.selectbox("Em qual área do conhecimento você tem mais interesse?", ["Biologia", "Química", "Física", "Matemática", "Ciências Sociais", "Computação", "Engenharia"])
tema_especifico = st.text_input("Dentro dessa área, qual tema específico você gostaria de pesquisar?")
motivacao = st.text_input("O que te motiva a escolher esse tema?")
conhecimento_previo = st.radio("Já possui algum conhecimento prévio sobre esse tema?", ["Sim", "Não"])
habilidades = st.text_input("Quais habilidades você já possui que podem ser úteis para o desenvolvimento do projeto?")
recursos = st.text_input("Existe algum recurso ou material específico que você gostaria de utilizar no desenvolvimento do seu projeto?")
impacto = st.text_input("Qual o impacto que você espera que seu projeto tenha na comunidade ou no mundo?")
informacao_adicional = st.text_area("Existe algo mais que você gostaria de me dizer sobre seu projeto?")

dados_usuario = {
    "ano_serie": ano_serie,
    "preferencia_projeto": preferencia_projeto,
    "participacao_anterior": participacao_anterior,
    "projeto_anterior": projeto_anterior,
    "metodologia": metodologia,
    "area_conhecimento": area_conhecimento,
    "tema_especifico": tema_especifico,
    "motivacao": motivacao,
    "conhecimento_previo": conhecimento_previo,
    "habilidades": habilidades,
    "recursos": recursos,
    "impacto": impacto,
    "informacao_adicional": informacao_adicional
}

if st.button("Gerar Ideia"):
    ideia = gerar_ideias(dados_usuario)
    if ideia:
        st.subheader("Aqui está uma ideia para seu projeto:")
        st.write(ideia)
else:
    st.write("Preencha as informações acima e clique no botão para gerar uma ideia de projeto.")
