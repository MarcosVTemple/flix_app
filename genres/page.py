import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

genres = [{'id':1, 'name':'Ação'},{'id':2, 'name':'Drama'}]

def show_genres():
    st.write('Lista de Gêneros:')
    
    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
    )
    
    st.title(body='Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso.')