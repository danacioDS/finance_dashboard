import streamlit as st
import yfinance as yf
import pandas as pd


st.write("Hola BOOTCAMP MOJIX")


st.title("Comportamiento Activos Financieros Importantes (en tasa de crecimiento)")

st.write("Descripcion tickers: ")
st.write("^GSPC es S&P 500, CL=F es WTI , GC=F es el Oro, ZW=F es trigo, TSLA es Tesla,  AAPL es Apple, MSFI es Microsoft,  BTC-USD es Bitcoin")


tickers = ('^GSPC', 'CL=F', 'GC=F', 'ZW=F', 'TSLA', 'AAPL', 'MSFI', 'BTC-USD')

dropdown = st.multiselect("Pick your assets", tickers)

start = st.date_input('Start', value = pd.to_datetime('2014-01-01'))
end = st.date_input('End', value=pd.to_datetime('today'))


st.write("Precio del activo (En USD)")

if len(dropdown) > 0:
    df = yf.download(dropdown, start, end)['Adj Close']
    st.line_chart(df)

def relative_ret(df):
    rel = df.pct_change()
    cum_rel = (1+rel).cumprod()-1
    cum_rel = cum_rel.fillna(0)
    return cum_rel

st.write("Retorno del activo (En Porcentajes)")    

if len(dropdown) > 0:
    #df = yf.download(dropdown, start, end)['Adj Close']
    df = relative_ret(yf.download(dropdown, start, end)['Adj Close'])
    st.line_chart(df)
    
