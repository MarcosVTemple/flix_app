import streamlit as st
from api.service import Auth


def login(username, password):
    auth_service = Auth()
    response = auth_service.get_token(
        username=username,
        password=password,
    )
