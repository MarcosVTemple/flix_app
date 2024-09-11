import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

actors = [{'id':1, 'name':'Lenin'},{'id':2, 'name':'Marx'}]

def show_actors():
    st.write('Lista de Atores/Atrizes:')
    
    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actors_grid',
    )
    
    st.title(body='Cadastrar novo ator/atriz')
    name = st.text_input('Nome do ator/atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{name}" cadastrado com sucesso.')