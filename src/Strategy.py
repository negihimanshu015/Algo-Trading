from Data_Ingestion import fetch
import ta

def RSI(data, window=14):
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    strength = avg_gain/avg_loss
    scale = 100 - (100/(1 + strength))

    return scale

def moving_averages(data):
    data['20DMA'] = data['Close'].rolling(20).mean()
    data['50DMA'] = data['Close'].rolling(50).mean()

    return data

def generate_signal(data):
    data["RSI"] = RSI(data)
    data = moving_averages(data)

    data["signal"] = 0

    buy_condition = (data['RSI'] < 30) & (data['20DMA'] > data['50DMA'])
    data.loc[buy_condition, 'signal'] = 1    

    return data

if __name__ == "__main__":
    data = fetch("HDFCBANK.NS")
    signals = generate_signal(data)

    print(signals[['Close', 'RSI', '20DMA', '50DMA', 'signal']].tail())
    

 