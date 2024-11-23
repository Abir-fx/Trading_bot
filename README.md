# Trading_bot

🛠️ Advanced Trading Bot 🚀

This repository contains an Advanced Trading Bot designed to automate cryptocurrency trading using Binance API and Telegram alerts. It fetches real-time market data, calculates indicators (RSI and EMA), generates trade signals, and logs trades into Google Sheets. 📊 The bot also sends trade alerts via Telegram with detailed instructions.


---

📋 Features

Real-Time Data Fetching: Fetches historical market data from Binance.

Technical Indicators: Uses RSI (Relative Strength Index) and EMA (Exponential Moving Average) for signal generation.

Automated Trade Alerts: Sends CALL/PUT signals to a Telegram chat.

Google Sheets Integration: Logs trades directly into a selected Google Sheet.

Risk Management: Calculates risk-based position sizes.

Trade Visualization: Plots trade entry, stop-loss, and take-profit points.

Customizable Configuration: Easily modify risk percentage, trade capital, and alert settings.



---

🛠️ Requirements

Before running the bot, ensure you have the following installed:

Python 3.8+

Required Libraries:

pandas

requests

matplotlib

ta

gspread

binance

python-telegram-bot




---

📦 Installation

Follow these steps to set up and run the trading bot:

1. Clone the Repository:

git clone https://github.com/your-username/advanced-trading-bot.git
cd advanced-trading-bot


2. Install Dependencies: Install the required libraries using pip:

pip install pandas requests matplotlib ta gspread binance python-telegram-bot


3. Set Up Binance API Keys:

Create a Binance account and generate an API key/secret.

Replace BINANCE_API_KEY and BINANCE_API_SECRET in the script with your keys.



4. Set Up Telegram Bot:

Create a Telegram bot using BotFather and copy the token.

Replace TELEGRAM_TOKEN and TELEGRAM_CHAT_ID in the script.



5. Google Sheets Integration:

Enable the Google Sheets API on your Google account.

Download the service account JSON key and replace the path in the script (filename variable) with the correct path.



6. Run the Bot:

python main.py




---

🎯 How It Works

1. The bot fetches real-time market data for the specified symbol (e.g., BTCUSDT) from Binance.


2. It calculates RSI and EMA indicators.


3. It generates CALL or PUT signals based on predefined conditions:

CALL: When EMA(9) > EMA(21) and RSI < 70.

PUT: When EMA(9) < EMA(21) and RSI > 30.



4. Sends trade alerts to your Telegram chat.


5. Logs the trades in a Google Sheet for record-keeping.


6. Visualizes the trade on a plot with entry, stop-loss, and take-profit levels.




---

⚙️ Configuration

You can customize the following parameters in the script:


---

💻 Example Usage

Running the Bot

1. Ensure the market is open for trading. The bot will skip execution during non-market hours.


2. Execute the script:

python main.py



Telegram Alerts

The bot sends real-time alerts for trade signals:

🟩 **Trade Alert**
Signal: CALL
Entry: 45000.00
Stop-Loss: 44100.00
Take-Profit: 45900.00

Google Sheets Logging

The bot logs trade details in a Google Sheet, including:

Timestamp

Signal Type (CALL/PUT)

Entry Price

Stop-Loss

Take-Profit

Profit/Loss


Visualizing Trades

The bot plots the trade setup, including:

Close price

Entry price

Stop-loss and take-profit levels



---

🛡️ Disclaimer

This bot is for educational purposes only. Trading involves risk, and past performance is not indicative of future results. Use this bot at your own discretion, and always conduct thorough research before trading.


---

🔧 Issues and Support

If you encounter any issues or have questions, feel free to create an issue in this repository or reach out to the maintainer.

Happy Trading! 📈✨

