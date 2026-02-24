import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime


st.title("Stock Price Analysis")

st.sidebar.header("Stock Price Analysis")


stock1 = st.sidebar.text_input("Enter the stock 1 ")

stock2 = st.sidebar.text_input("Enter the stock 2 ")

start_date, end_date= st.sidebar.slider("Select the time period", min_value= 2010, max_value= datetime.now().year , value = (2015, datetime.now().year))


if st.sidebar.button("submit") and  stock1  and stock2 :
    st_date= f'{start_date}-01-01'
    en_date= f"{end_date}-12-31"

    stock1_data = yf.download(stock1, st_date, en_date)

    stock2_data = yf.download(stock2, st_date, en_date)

    if not stock1_data.empty and not stock2_data.empty:
        st.write(stock1_data.sort_values(by=["Date"], ascending= False).head())
        st.write(stock2_data.sort_values(by=["Date"], ascending=False).head())


        fig, ax = plt.subplots(figsize=(10,6))
        ax.plot(stock1_data.index,stock1_data["Close"], label= f"{stock1}" )
        ax.plot(stock2_data.index,stock2_data["Close"], label= f"{stock2}" )
        ax.set_title("Stock Price Analysis")
        ax.set_xlabel("Date")
        ax.set_ylabel("Stock Price (USD)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)
    else:
        st.error(f"check the stocks name {stock1} and {stock2}")