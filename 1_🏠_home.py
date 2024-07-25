import streamlit as st
import webbrowser as link
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="FIFA 2023",
    page_icon="🏠",
    layout="wide"
)

if "data" not in st.session_state: # ainda não temos a variavel data na sessão
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=1)
    df_data = df_data[df_data["Contract Valid Until"]>= datetime.today().year] # filtrando só os jogadores que contract valid until >= ano atual
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Douglas Vizzacchi](https://www.vizzacchi.com.br)")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    link.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    """
    O conjunto de dados contém *+17 mil jogadores* únicos e mais de 60 colunas, informações gerais e todos os KPIs que o famoso videogame oferece. Como a cena de esports continua crescendo espacialmente no FIFA, achei que poderia ser útil para a comunidade (kagglers e/ou jogadores).
    """
)

st.subheader("Contexto")
st.markdown(
    """
    Os dados foram recuperados graças a um rastreador que implementei para recuperar:
    - Dados agregados, como nome dos jogadores, idade, país
    - Dados detalhados como potencial ofensivo, defesa, aceleração

    Gosto muito de futebol e este conjunto de dados é para mim a oportunidade de trazer minha contribuição para a realização de projetos que podem ir desde a simples análise até a elaboração de estratégias de composição ótima sob restrições...
"""
)