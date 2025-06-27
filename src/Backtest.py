from Data_Ingestion import fetch
from Strategy import generate_signal
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def backtest(ticker, initial_cash=10000):

    """
    Backtest based on signals.

    Parameters
    ----------
    ticker: str
        Stock ticker symbol

    initial_cash: int
        Total capital for backtesting.
    
    Returns
    -------
        List :
            containing Dict (Date, Action (str), price (float), shares (int), profit (float))              
    """

    logging.info("Performing Backtesting.")
    data = fetch(ticker)
    signal = generate_signal(data)

    shares = 0
    trades =[]
    cash= initial_cash

    for date, row in signal.iterrows(): #Iterates over each day.
        
        price = row['Close']       

        if (row['signal'] == 1) and (shares == 0):
            buy_price = price
            shares = cash // price
            cash = cash - shares * price
            trades.append({'Date': str(date.date()), 'Action': "BUY", 'Price': price, 'Shares': shares})

        elif shares > 0 and (row['20DMA'] < row['50DMA']):
            cash = cash + shares * price
            trades.append({'Date': str(date.date()), 'Action': "SELL", 'Price': price, 'Shares': shares, 'Profit': (price - buy_price) * shares })
            shares = 0

    return trades


def metric(trades, initial_cash=10000):

    """
    Describes performance of the strategy.

    Parameters
    ----------
    trades: (from backtest() function.)        

    initial_cash: int
        Total capital for backtesting.
    
    Returns
    -------
        Dict :
            containing Total Trades (int), Total Profit (float), Return (float), Winning Ratio (float).             
    """  

    if not trades:
         logging.warning("No trades were executed.")
         return {
            "Total Trades": 0,
            "Total Profit": 0,
            "Return": 0.0,
            "Winning Ratio": 0.0
        }
    
    profits = []

    for trade in trades:
        if 'Profit' in trade:
            profits.append(trade['Profit'])

    if profits:
        total_profit = profits[-1]
    else:
        total_profit = 0

    count = 0
    for i in profits:
        if i > 0:
            count += 1

    if profits:
        winning_trades = (count/len(profits))  * 100
    else:
        winning_trades = 0

    metrics = {
        "Total Trades": len(trades)//2,
        "Total Profit": total_profit,
        "Return": (total_profit/initial_cash)*100,
        "Winning Ratio": winning_trades           
    }    
    
    return metrics 
            
         
        


