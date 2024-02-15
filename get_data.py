import pandas as pd
from config import DATA_URL
import streamlit as st


@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
