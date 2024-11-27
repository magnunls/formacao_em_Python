import streamlit as st
import pandas as pd
import plotly.express as px
def main():
    st.set_page_config(
        page_title = "Gráficos interativos",
        page_icon = "📊",
        layout = "wide"
    )
    st.title("Gráficos interativos")
    df = pd.read_csv("http://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")
    st.write("dados utilizados")
    st.dataframe(df)

    #gráfico de dispersão
    st.subheader("Gráfico de dispersão")
    fig= px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", log_x=True, size_max=60)
    st.plotly_chart(fig)

    #gráfico de linha
    st.subheader("Gráfico de Linhas")
    fig2=px.line(df, x="year", y="lifeExp", color="continent", line_group="country", title="Expectativa de vida por ano e continente")
    st.plotly_chart(fig2)

    st.subheader("Gráficos de Linhas")
    df_continente=df.groupby(['continent', 'year'])['lifeExp'].mean().reset_index()
    fig3=px.line(df_continente, x="year", y="lifeExp", color="continent", line_group="continent", title="Expectativa de vida por ano e continente")
    st.plotly_chart(fig3)

    #gráfico de barras
    st.subheader("Gráfico de barras")
    fig5=px.bar(df, x="continent", y="pop", color="continent", barmode="group", title="População por continente")
    st.plotly_chart(fig5)
main()