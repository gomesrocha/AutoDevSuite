import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv  

load_dotenv()
g_api_key = os.getenv("GOOGLE_API_KEY")


# Inicialize a classe correta com a chave da API
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", google_api_key=g_api_key)

prompt_template_br = "Você é um analista de teste, responsável pela criação de testes unitários, com base na história de usuário {us} \
 e nos critérios de aceites {ca} baseados no gherkin, crie os testes unitários para a linguagem de programação {lp} \
 baseados no framework {fw} \
 e explique como usar o código."

# Interface do Streamlit
st.title("AutoDevSuite : Gerador de testes baseados no BDD")
us = st.text_area("Entre com sua históriade usuário:")
ca = st.text_area("Entre com o seu teste de aceitação no formato gherkin:")
lp = st.text_input("Qual a linguagem de programação você vai usar:")
fw = st.text_input("Entre com o framework preferido:")

prompt = PromptTemplate(
    input_variables=["us", "ca", "lp", "fw"],
    template=prompt_template_br
)
chain_1 = LLMChain(llm=llm, prompt=prompt)

if st.button("Generate Unit Tests"):
    # Gera o resultado usando os valores de entrada
    inputs = {"us": us, "ca": ca, "lp": lp, "fw": fw}
    result = chain_1.run(inputs)
    
    # Exibe o resultado
    st.write("Results:")
    st.write(result)
