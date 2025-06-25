import pandas as pd
import yfinance as yf
import os

stocks = ["RELIANCE.NS", "HDFCBANK.NS", "INFY.NS"]

def fetch(ticker, csv=False):
    try:        

        data = yf.download(ticker, period="6mo", auto_adjust=True)
        
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        data.columns.name = None


        if csv:
            os.makedirs("data", exist_ok=True)            
            data.to_csv(f"data/{ticker.replace('.','_')}.csv")
        
        return data

    except Exception as e:
        print(f"Fetching error{e}")