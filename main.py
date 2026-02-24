import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from  datetime import datetime

st.title("Stock Price comparsion")

st.sidebar.header("Enter the stock symbol")

stock1 = st.sidebar.text_input("Enter stock symbol stock1")

stock2 = st.sidebar.text_input("Enter stock symbol stock 2")

start_year, end_year = st.sidebar.slider("select the start and end year :", min_value=2010, max_value= datetime.now().year , value=(2023, datetime.now().year))





if stock1 and stock2:
    start_year, end_year = f'{start_year}-01-01' , f'{end_year}-12-31'

    stock1_data = yf.download(stock1, start_year, end_year)
    stock2_data = yf.download(stock2, start_year, end_year)

    if not stock1_data.empty and not stock2_data.empty:
        st.write(stock1_data.head())
        st.write(stock2_data.head())

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(stock1_data.index, stock1_data["Close"] , label= f"Share name {stock1}")
        ax.plot(stock2_data.index, stock2_data["Close"] , label= f"Share name {stock2}")
        ax.set_title("Stock Price Comparison")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price(USD)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

    else:
        st.error(f"Stock symbol not found {stock1} or {stock2}")







