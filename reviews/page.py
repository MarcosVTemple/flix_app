import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

reviews = [{'id':1, 'stars': 4}, {'id':2, 'stars':5}]

def show_reviews():
    st.write('Lista de avaliações:')
    
    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
    )
