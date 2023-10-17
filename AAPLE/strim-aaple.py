import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(layout='wide')

st.write(
    """
# Визуализация котеровок компании **APPLE** с начала выхода компании на **IPO**
    """
)

tick = yf.Ticker('AAPL')

df_history = tick.history(period='1m', start='1980-12-12')

st.line_chart(df_history['Close'])
