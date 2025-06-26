from Data_Ingestion import fetch
from Strategy import generate_signal
from Backtest import backtest, metric
from log import connect, log_trades, summary
import pandas as pd

def algo(ticker):
    data = fetch(ticker)
    signals = generate_signal(data)
    trades = backtest(ticker)
    log_summary = metric(trades)

    trades_df = pd.DataFrame(trades)
    cred_path = "private//credential.json"
    sheet_name = "ALgo Trading Log"

    sheet = connect(sheet_name, cred_path)

    if trades:
        log_summary = metric(trades)
        trades_df = pd.DataFrame(trades)

        sheet = connect(sheet_name, cred_path)
        log_trades(sheet, trades_df, ticker)
        summary(sheet, log_summary, ticker)
    else:
        print(f"No trades for {ticker}.")

if __name__ == "__main__":
    for ticker in ["UPL.NS", "JSWSTEEL.NS", "BAJFINANCE.NS"]:
        algo(ticker)