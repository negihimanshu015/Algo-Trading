import pandas as pd
import yfinance as yf
import os
import logging

stocks = ["RELIANCE.NS", "HDFCBANK.NS", "INFY.NS"]
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def fetch(ticker, csv=False):
     
    """
    Fetches historical stock data.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol.

    csv : bool
        Saves the data as a CSV file.

    Returns
    -------
        DataFrame
        Contains stock data.
    """

    try:
        logging.info(f"Fetching data for {ticker}")
        data = yf.download(ticker, period="6mo", auto_adjust=True)
        
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        data.columns.name = None


        if csv:
            os.makedirs("data", exist_ok=True)            
            data.to_csv(f"data/{ticker.replace('.','_')}.csv")
        
        return data

    except Exception as e:
        logging.error("Error occurred for {ticker}: {e}")