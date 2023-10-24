import streamlit as st
from Interface.Menu_dropdown import menu_radio

if __name__=='__main__':
    st.set_page_config(layout='wide', page_title='Dashboard Desmatamento na Amazônia', 
                       initial_sidebar_state='expanded')
    st.sidebar.title('Análise Desmatamento na Amazônia')
    menu_radio()