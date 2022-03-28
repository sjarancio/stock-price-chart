import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Stock Price App

Shown is the **closing price** and **volume** of Tesla stock!

""")

tickerSymbol = 'TSLA'
# tickerSymbol2 = 'SQ'

tickerData = yf.Ticker(tickerSymbol)
# tickerZata = yf.Ticker(tickerSymbol2)

tickerDf = tickerData.history(period='1d', start='2012-5-31', end='2020-5-31')
# tickerZf = tickerZata.history(period='1d', start='2012-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)

# st.line_chart(tickerZf.Close)
# st.line_chart(tickerZf.Volume)