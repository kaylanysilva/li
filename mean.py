import streamlit as st

st.title('oi mundo')

#carregar dados
df_dados = pd.read_excel(r"C:\Users\kaylany\Downloads\volumetrafegomensal.xlsx")

#codificar

st.header('volume de trafego - Fortaleza-CE')
st.markdown(' informações de todos os trafegos ocorridos em Fortaleza-CE no ano de 2023')


