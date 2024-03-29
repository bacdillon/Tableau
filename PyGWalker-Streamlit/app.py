import streamlit as st
import pandas as pd
import pygwalker as pyg

# Set page configuration
st.set_page_config(
    page_title="Streamlit - PyGWalker Python Library",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load Data
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df
df = load_data("data/bike_sharing_dc.csv")

# Set title and subtitle
st.title('Streamlit - PyGWalker Python Library')

# Display PyGWalker
def load_config(file_path):
    with open(file_path, 'r') as config_file:
        config_str = config_file.read()
    return config_str
config = load_config('config.json')
pyg.walk(df, env='Streamlit', dark='dark', spec=config)