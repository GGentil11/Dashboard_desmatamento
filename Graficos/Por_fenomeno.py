import streamlit as st
import pandas as pd
import plotly.express as px

def por_fenomeno(df_fenomeno):
    anos_desejados = range(df_fenomeno['start year'].min(), df_fenomeno['start year'].max() + 1)

    # Reindexe o DataFrame com os anos desejados e preencha os valores ausentes na coluna Severidade com "Não houve"
    df_fenomeno = df_fenomeno.set_index('start year').reindex(anos_desejados).fillna('Não houve').reset_index()

    # Renomeie a coluna Ano de volta
    df_fenomeno = df_fenomeno.rename(columns={'index': 'start year'})

    df_fenomeno['severity']=pd.Categorical(df_fenomeno['severity'], 
                      ordered=True, 
                      categories=['Não houve', 'Weak', 'Moderate', 'Strong', 'Very Strong'])
    df_fenomeno['start year'] = pd.to_datetime(df_fenomeno['start year'], format='%Y')

    fig_date = px.bar(df_fenomeno.sort_values(by='severity'), 
                      x='start year', 
                      y='severity',
                      color='phenomenon',
                      title='Severidade dos Fenômenos Climáticos',
                      labels={
                          'start year': 'Início do Fenômeno',
                          'severity': 'Severidade', 
                          'phenomenon': 'Fenômeno Climático'
                      })
    fig_date.add_annotation(
        text = ('Fonte: Golden Gate Weather Services'), 
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
    fig_date.update_layout(
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=1.05
        )
    )
    return fig_date
