import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Painel de Controle de Atividades")

# Upload do arquivo CSV
df = st.sidebar.file_uploader("Upload arquivo csv", type=['csv'])

if df:
    df = pd.read_csv(df)
    df["data"] = df["data"].str.upper()
    df["atividades"] = df["atividades"].str.upper()
    df["data"] = pd.to_datetime(df["data"])
    df = df.sort_values("data")

    # Torna o mês único
    df["Month"] = df["data"].apply(lambda x: f"{x.month}-{x.year}")

    # Dropdowns para seleção de mês e atividade
    st.sidebar.header("Filtros")
    month = st.sidebar.selectbox('Escolha o Mês', ['Todos'] + list(df["Month"].unique()))
    atividade = st.sidebar.selectbox('Escolha a Atividade', ['Todas'] + list(df["atividades"].unique()))

    # Filtragem dos dados
    if month != 'Todos':
        df = df[df["Month"] == month]
    if atividade != 'Todas':
        df = df[df["atividades"] == atividade]

    # Criação dos gráficos
    st.subheader("Quantidade de Peças por Atividade")
    fig = st.bar(df, x="data", y="unidades", color="atividades", title="Atividades ao Longo do Tempo")
    fig.update_layout(xaxis_title='Data', yaxis_title='Unidades')
    st.plotly_chart(fig)

else:
    st.write("Aguardando o upload de um arquivo CSV.")
