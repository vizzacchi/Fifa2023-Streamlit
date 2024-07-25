import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_players.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Joined"] # lista com as colunas que quero filtrar

st.dataframe(df_players[columns],
             column_config={
                "Overall": st.column_config.ProgressColumn(
                    "Overall", format="%d", min_value=0, max_value=100
                ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("País")
             }) # exibindo um dataframe só com as colunas da lista anterior
