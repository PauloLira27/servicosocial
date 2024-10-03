import streamlit as st
import pandas as pd
import locale
from datetime import datetime, timedelta
import plotly.express as px

# Dados
dados = {
    "Contato telefônico": 10,
    "Articulação em rede": 65,
    "Atendimento leito": 55,
    "Acolhimento": 50,
    "Relatório social": 10,
    "Atendimento externo": 0,
    "Reuniões externas": 2,
    "Busca ativa": 45,
    "Visita multiprofissional": 5,
    "Visita beira leito": 466,
    "Orientações de óbito": 0,
    "Orientações políticas de assistência": 65,
    "Matriciamento": 20
}

# Converter os dados para DataFrame e ordenar
df = pd.DataFrame(list(dados.items()), columns=['Atividade', 'Quantidade'])
df = df.sort_values(by='Quantidade', ascending=True)

fig = px.bar(df, y='Atividade', x='Quantidade', title='SERVIÇO SOCIAL - SETEMBRO 2024',
             labels={'Atividade': 'Atividade', 'Quantidade': 'Quantidade'},
             text_auto=True)  # Adicionar os valores nas barras

# Ajustar a largura das barras e o tamanho da figura
fig.update_layout(bargap=0.1) 
fig.update_layout(width=1000, height=500)

# Exibir no Streamlit
st.markdown(
    f"""
    <h1 style="text-align: center;">PRODUÇÃO - SERVIÇO SOCIAL SETEMBRO 2024</h1>
    """, unsafe_allow_html=True
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)