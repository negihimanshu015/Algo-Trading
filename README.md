# Algo-Trading

A Python-based algorithmic trading system that leverages the Relative Strength Index and Double Moving Average strategies. The project includes modules for data ingestion, backtesting, model development, strategy implementation, and Telegram alerts.

## Features

- **Data Ingestion**: Fetch and preprocess data for analysis and trading.
- **Strategy Implementation**: Apply RSI and DMA-based trading strategies.
- **Backtesting**: Evaluate strategy performance on historical data.
- **Modeling**: Build and test predictive models for trading signals.
- **Logging**: Track system events and errors.
- **Telegram Alerts**: Receive real-time trading alerts via Telegram.

## Project Structure

```
src/
│
├── Backtest.py         # Backtesting engine for trading strategies
├── Data_Ingestion.py   # Data fetching and preprocessing
├── log.py              # Logging to google sheets.
├── main.py             # Main entry point for running the system
├── Model.py            # Machine Learning (Decision Tree)
├── Strategy.py         # RSI and DMA strategy logic
└── Telegram_Alert.py   # Telegram alert integration
private/
└── credential.json     # API keys
```

## Getting Started

### Prerequisites

- Python 3.8+
- Required Python packages (see below)

### Installation

1. Clone the repository:
   ```powershell
   git clone https://github.com/negihimanshu015/Algo-Trading.git
   cd Algo-Trading
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Add your API credentials to `private/credential.json`.

### Usage

Run the main script to start the trading system:
```powershell
python src/main.py
```

## Configuration

- Edit `private/credential.json` with your API keys and secrets.
- Adjust strategy parameters in `src/Strategy.py` as needed.

## Alerts

- Set up your Telegram bot and chat ID in `.env` to receive trading alerts.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.