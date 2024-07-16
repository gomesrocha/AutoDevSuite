import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv  

load_dotenv()
g_api_key = os.getenv("GOOGLE_API_KEY")

# Substitua pela importação correta da biblioteca que você está usando
# Exemplo fictício:
from google.generativeai.client import GoogleGenerativeAIClient

# Inicialize a classe correta com a chave da API
llm = GoogleGenerativeAIClient(api_key=g_api_key)

prompt_template_br = "Você é um analista de teste, responsável pela criação de testes unitários, com base na história de usuário {us} \
 e nos critérios de aceites {ca} baseados no gherkin, crie os testes unitários para a linguagem de programação {lp} \
 baseados no framework {fw} \
 e explique como usar o código."

# Interface do Streamlit
st.title("AutoDevSuite : BDD-based Test Generator")
us = st.text_area("Enter US:")
ca = st.text_area("Enter your gherkin-based acceptance criteria:")
lp = st.text_input("Enter the programming language:")
fw = st.text_input("Enter the framework:")

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
