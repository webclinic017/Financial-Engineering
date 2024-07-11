import streamlit as st
import os
import logging
from data.utils import options_data

logger = logging.getLogger(os.path.basename(os.path.dirname(__file__)))

st.title("Hello, World!")
st.write("Welcome to your Streamlit app running in a Docker container.")

with st.sidebar:
    st.sidebar.write("Configuration")
    ticker = st.sidebar.text_input(label="Stock Ticker")
    time_delta = st.sidebar.slider(
        label="Time Period in days", min_value=1, max_value=365 * 5, value=365
    )
    st.write(f"Stock Ticker: {ticker}")
    st.write(f"Time Period: {time_delta} days")
    if st.button("Analyse"):
        data = options_data(ticker, time_delta)
        st.write(data)
