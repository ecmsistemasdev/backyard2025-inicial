import streamlit as st
from datetime import date

#st.markdown("### 🔒Inscrições Encerradas")
from PIL import Image
img = Image.open('02.png')
st.image(img)
st.markdown("### Macaxeira Backyard Ultra - 2ª Edição")
st.write("")
#st.markdown("### 🔒Inscrições Encerradas")

st.link_button(label="Clique aqui para realizar sua inscrição",url="https://macaxeirabackyard-inscricao-6ae3f0f0b354.herokuapp.com/",type="primary")

with st.form("Informativo", border=False):
    st.markdown("##### Informativo da Corrida")
    with open('Informativo.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            st.write(line)

    #st.write("📅 Dia 22 de fevereiro de 2025")
    #st.write("🏃🏻 Largada às 08hs 🕗")
    #st.caption("")
    #st.write("💲 Valor da Inscrição: 279,00 reais para prova Principal; 179,00 para prova de três voltas")
    #st.write("💲 Atleta com 60 ou mais, paga 50% do valor integral")
    
    #st.write("Forma de Pagamento: ")
    #st.write("  Pix kelioesteves@hotmail.com - Kélio Esteves Xavier - Mercado pago.")
    #st.write("📱 Mais informações: (69) 99925-9005")
    #st.caption("")
    #st.write("INSCRIÇÕES:")
    #st.write("✍️ Período de inscrição:")
    #st.write("  Início: 10 de novembro de 2024")
    #st.write("  Término: 06 de janeiro 2025 ou até o limite das vagas")
    
    st.form_submit_button("",disabled=True)

with st.form("Regulamento"):
    st.markdown("##### Regulamento")
    with open('Regulamento.txt', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            st.write(line)
    st.link_button(label="Clique aqui para realizar sua inscrição",url="https://macaxeirabackyard-inscricao-6ae3f0f0b354.herokuapp.com/",type="primary")
    #st.link_button(label="Clique aqui para realizar sua inscrição",url="http://191.217.246.233:8501/",type="primary")
    st.form_submit_button("",disabled=True)

from PIL import Image
img = Image.open('003.png')
st.image(img)
