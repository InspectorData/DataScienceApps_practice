import yfinance as yf
import streamlit as st
import pandas as pd

# yfinance for stockprices and crpyto prices. Also offers market news, reports and analysis including options and fundamental data
# streamlit for webapps deployment
#pandas for data manipulation and analysis

st.write(""""
# Simple Stock Price App

Shown are the stock closing price and volume of TESLA
(2011-12-01 To 2021-11-30).

""")

#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

tickerSymbol = 'TSLA'

#get data on this ticker

tickerData =yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf= tickerData.history(period= '1d', start ='2011-12-01', end='2021-11-30')
# Open High Low Close Volume Dividends Stock Splits

st.write(""" ## Closing Price""")
st.line_chart(tickerDf.Close)

st.write(""" ## Volume Price""")
st.line_chart(tickerDf.Volume)
