import pandas as pd
import streamlit as st
import yfinance as yf

st.set_page_config(layout='wide')

st.write(
    """
# Визуализация котеровок компании **Apple** с начала выхода компании на **IPO**
    """
)

tick = yf.Ticker('AAPL')

df_history = tick.history(period='1m', start='1980-12-12')

st.line_chart(df_history['Close'])

# Зависимость между котировками Google и Apple

st.write("""
# Корреляция между котировками акций ***Google*** и ***Apple***
"""
)

new_df = pd.DataFrame({
    "GOOGLE": yf.Ticker('GOOGL').history(period='1m', start='1980-12-12')['Close'],
    'APPLE': df_history['Close']
})

st.scatter_chart(data=new_df, x='GOOGLE', y='APPLE')
st.info('Как видим из графика, есть достаточная четкая корреляция, \
которая сопровождается изменением котировок Apple на аналогичные изменения котировок Google.')