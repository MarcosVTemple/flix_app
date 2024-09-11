import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

movies = [{'id':1, 'name':'Titanic'},{'id':2, 'name':'RRR'}]

def show_movies():
    st.write('Lista de filmes:')
    
    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
    )
