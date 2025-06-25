from Data_Ingestion import fetch
from Strategy import generate_signal

def backtest(ticker, initial_cash=10000):
    data = fetch(ticker)
    signal = generate_signal(data)

    shares = 0
    trades =[]
    cash= initial_cash

    for date, row in signal.iterrows():
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
    if not trades:
        return "No Trades"
    
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
            "Winning Trades": winning_trades           
        }

    return metrics 
            
         
        


