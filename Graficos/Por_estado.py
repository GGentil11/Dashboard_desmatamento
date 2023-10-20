import streamlit as st
import pandas as pd
import plotly.express as px

def por_estado(df):
    estado = st.sidebar.selectbox("Selecione o estado", df['Estados'].unique())
    df_filtrado = df[df['Estados'] == estado]

    fig_date = px.bar(df_filtrado, x='Ano', y='Área Desmatada', title=f'Desmatamento em {estado}',
                    labels={
                        'Área Desmatada': 'Área desmatada(km^2)'
                    })
    fig_date.add_annotation(
        text = ('Fonte: INPE - Instituto Nacional de Pesquisas Espaciais'), 
        showarrow=False, 
        x = 0, 
        y = -0.15, 
        xref='paper', 
        yref='paper' , 
        xanchor='left', 
        yanchor='bottom', 
        xshift=-1, 
        yshift=-5, 
        font=dict(size=10, color="grey"), 
        align="left"
    )
    return fig_date