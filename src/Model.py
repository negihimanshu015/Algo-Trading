from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from Data_Ingestion import fetch
from Strategy import RSI, MACD
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def data_process(ticker):
    """
    Preprocesses the data for machine learning.

    Parameters
    ----------
    ticker: str
        Stock ticker symbol.   

    Returns
    -------
        Dataframe (updated dataframe with target column.)
    """
   
    data = fetch(ticker)
    data['RSI'] = RSI(data).clip(0,100)
    data['MACD'], data['Signal_Line'] = MACD(data)
    data['Volume_diff'] = data['Volume'].pct_change().replace([np.inf, -np.inf], 0).fillna(0) # Percentage change in volume.

    target = []

    for i in range(len(data) - 1):
        today_price = data['Close'].iloc[i]
        tomorrow_price = data['Close'].iloc[i+1]

        if tomorrow_price > today_price:
            target.append(1)
        else:
            target.append(0)

    target.append(0)  # For the last day
    data['Target'] = target

    data.replace([np.inf, -np.inf], np.nan, inplace=True) # Replace inf and -inf.
    data = data.dropna()

    return data


def Decision_tree(data):

    """
    Parameters
    ----------
    data: Dataframe
        (From data_preprocess() function.)   

    Returns
    -------
        model: DecisionTreeClassifier,
        accuracy: float,
        feature: DataFrame
    """  

    logging.info("Machine Learning (Decision-Tree).")
    feature = data[['RSI', 'MACD', 'Volume_diff']]
    target = data['Target']

    X_train, X_test, Y_train, Y_test = train_test_split(feature,target, test_size=0.2, shuffle=False)

    model = DecisionTreeClassifier(max_depth=2, random_state=42)
    model.fit(X_train,Y_train)

    prediction = model.predict(X_test)
    accuracy = accuracy_score(Y_test, prediction)
    
    logging.info(f"Decision Tree accuracy:{accuracy:.2%}")
    return model, accuracy, feature