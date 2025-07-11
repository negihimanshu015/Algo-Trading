import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def RSI(data, window=14):

    """
    Calculates RSI value.

    Parameters
    ----------
    data : dataframe        

    window : int
        period for RSI calculations.

    Returns
    -------
        series (RSI value)                
    """

    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()

    strength = avg_gain/avg_loss
    scale = 100 - (100/(1 + strength))

    return scale

def MACD(data):

    """
    Calculates macd & singal line.

    Parameters
    ----------
    data : dataframe  

    Returns
    -------
        series (MACD, Signal line)                
    """

    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()

    macd = exp1 - exp2.replace([np.inf, -np.inf], 0)

    signal_line = macd.ewm(span=9, adjust=False).mean()
    return macd, signal_line
    

def moving_averages(data):   

    data['20DMA'] = data['Close'].rolling(20).mean()
    data['50DMA'] = data['Close'].rolling(50).mean()

    return data

def generate_signal(data):

    """
    Genearates buy signal based on the strategy.

    Parameters
    ----------
    data : dataframe   

    Returns
    -------
        Dataframe (updated dataframe with signal column.)               
    """

    logging.info("Generating signals.")
    data["RSI"] = RSI(data)
    data = moving_averages(data)

    data["signal"] = 0

    buy_condition = (data['RSI'] < 30) & (data['20DMA'] > data['50DMA'])
    data.loc[buy_condition, 'signal'] = 1    

    return data

    

 