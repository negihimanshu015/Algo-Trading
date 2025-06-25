from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from Data_Ingestion import fetch
from Strategy import RSI, MACD
import pandas as pd
import numpy as np

def data_process(ticker):
    data = fetch(ticker)
    data['RSI'] = RSI(data).clip(0,100)
    data['MACD'], data['Signal_Line'] = MACD(data)
    data['Volume_diff'] = data['Volume'].pct_change().replace([np.inf, -np.inf], 0).fillna(0)

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

    data.replace([np.inf, -np.inf], np.nan, inplace=True)
    data = data.dropna()

    return data


def logistic_model(data):
    feature = data[['RSI', 'MACD', 'Volume_diff']]
    target = data['Target']

    X_train, X_test, Y_train, Y_test = train_test_split(feature,target, test_size=0.2, shuffle=False)

    model = LogisticRegression()
    model.fit(X_train,Y_train)

    prediction = model.predict(X_test)
    accuracy = accuracy_score(Y_test, prediction)

    return model, accuracy, feature


if __name__ == "__main__":
    ticker = "UPL.NS"
    data = data_process(ticker)
    model, accuracy, feature = logistic_model(data)

    print(f"Accuracy:{accuracy:.2%}")
    print("Predictions:")
    print(pd.DataFrame({'Actual': data['Target'][-5:], 'Predicted': model.predict(feature[-5:])}))