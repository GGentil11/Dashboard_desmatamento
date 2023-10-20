import streamlit as st
import pandas as pd
from Graficos.Por_ano import por_ano
from Graficos.Por_estado import por_estado
from Graficos.Por_fenomeno import por_fenomeno

df = pd.read_csv('Datasets/Desmatamento.csv', sep=',')
df_fenomeno = pd.read_csv('Datasets/el_nino_la_nina_1999_2019.csv')
def menu_radio():
    st.sidebar.caption(f'Dados retirados do Dataset: [Brazilian Amazon Rainforest Degradation 1999-2019](https://www.kaggle.com/datasets/mbogernetto/brazilian-amazon-rainforest-degradation)')
    tipo_pesquisa = st.sidebar.radio('Selecione o filtro', ['Por ano', 'Por estado', 'Influência de Fenômenos Climáticos'], 
                            captions=['Demonstra o desmatamento de todos os estados com base no ano', 
                            'Demonstra o desmatamento do estado ao longo dos anos',
                            'Demonstra a ocorrência de fenômenos climáticos e sua itensidade'])
    return escolha_radio(tipo_pesquisa, df, df_fenomeno)

def escolha_radio(tipo_pesquisa, df, df_fenomeno):
    if tipo_pesquisa == 'Por ano':
        st.plotly_chart(por_ano(df))
    elif tipo_pesquisa == 'Por estado':
        st.plotly_chart(por_estado(df))
    elif tipo_pesquisa == 'Influência de Fenômenos Climáticos':
        st.plotly_chart(por_fenomeno(df_fenomeno))
