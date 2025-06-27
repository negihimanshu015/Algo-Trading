from Backtest import backtest, metric
from log import connect, log_trades, summary
import pandas as pd
from Telegram_Alert import Telegram_Alert
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def algo(ticker):
    logging.info("Executing Algo function.")       
    trades = backtest(ticker)
    log_summary = metric(trades)

    message = f" Code executed for {ticker} \n Total Profit: {log_summary['Total Profit']:.2f} \n Winning Ratio: {log_summary['Winning Ratio']:.2f}%"
    Telegram_Alert(message)

    trades_df = pd.DataFrame(trades)
    cred_path = "private//credential.json"
    sheet_name = "ALgo Trading Log"

    sheet = connect(sheet_name, cred_path)

    if trades:                        
        log_trades(sheet, trades_df, ticker)
        summary(sheet, log_summary, ticker)
    else:
        print(f"No trades for {ticker}.")

if __name__ == "__main__":
    for ticker in ["UPL.NS", "JSWSTEEL.NS", "BAJFINANCE.NS"]:
        algo(ticker)