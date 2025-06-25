import pandas as pd
import yfinance as yf
import os
from datetime import datetime, timedelta

stocks = ["RELIANCE.NS", "HDFCBANK.NS", "INFY.NS"]

def fetch(ticker, csv=False):
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        data = yf.download(ticker, start=start_date, end=end_date, period="6mo", auto_adjust=True)

        if csv:
            os.makedirs("data", exist_ok=True)            
            data.to_csv(f"data/{ticker.replace('.','_')}_{end_date.date()}.csv")
        
        return data

    except Exception as e:
        print(f"Fetching error{e}")

if __name__ == "__main__":
    for stock in stocks:
        df = fetch(stock, csv=True)
        print(f"Downloaded {stock} | {len(df)} records")
