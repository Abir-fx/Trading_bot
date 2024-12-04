# 📈 **Intraday Trading Telegram Bot**

This is a fully automated intraday trading assistant that analyzes stocks based on your predefined strategy and sends daily recommendations to your Telegram account. The bot selects 2 stocks daily, analyzes them using technical indicators (VWAP, EMA, RSI), and provides buy/sell signals. 

### 🛠️ **Technologies Used:**
- **Python** 🐍
- **Telegram Bot API** 🤖
- **Alpha Vantage API** 📊
- **NSE Tools** 📉
- **Matplotlib** 🖼️
- **Pandas** 🧑‍💻
- **Numpy** 🔢
- **Schedule** ⏰

### 📜 **Table of Contents**
- [📝 Project Overview](#project-overview)
- [⚙️ Setup and Installation](#setup-and-installation)
- [🚀 Usage Instructions](#usage-instructions)
- [💡 Configuration](#configuration)
- [🛠️ Troubleshooting](#troubleshooting)

---

## 📝 **Project Overview**

The bot fetches live data from the NSE (National Stock Exchange of India) using the `nsetools` library and applies technical analysis indicators, including:

- **VWAP** (Volume Weighted Average Price)
- **EMA** (Exponential Moving Average) – for trend analysis
- **RSI** (Relative Strength Index) – for overbought/oversold conditions

The bot automatically sends buy/sell signals based on this analysis to your Telegram account. 

---

## ⚙️ **Setup and Installation**

Follow these steps to get your intraday trading assistant up and running:

### 1. **Clone the Repository** 📥
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/intraday-telegram-trader.git
```

### 2. **Install Dependencies** 📦
Navigate to the project directory and install all the required dependencies:

```bash
cd intraday-telegram-trader
pip install -r requirements.txt
```

### 3. **Create an Alpha Vantage Account** 🔑
- Visit [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and sign up for a free API key.
- Replace the placeholder `"WHSH8F7FEJ4O6FZB"` with your own API key in `config.py`.

### 4. **Create a Telegram Bot** 🤖
- Go to [@BotFather](https://core.telegram.org/bots#botfather) on Telegram and create a new bot.
- Copy the API token and replace the placeholder `"your_telegram_bot_token"` in `config.py` with your bot’s token.

### 5. **Configure Telegram Chat ID** 💬
- To get your **chat ID**, use the following URL:
  ```
  https://api.telegram.org/bot<your_bot_token>/getUpdates
  ```
  Look for the `chat.id` value in the response.
- Replace the placeholder `"your_telegram_chat_id"` in `config.py` with your actual chat ID.

### 6. **Set Up the Stock Watchlist** 📈
- Modify the `stock_symbols` list in `main.py` with the stock symbols of your choice (for example, stocks from the NSE).
- By default, the bot will analyze stocks like `RELIANCE`, `TCS`, `INFY`, etc.

---

## 🚀 **Usage Instructions**

### 1. **Run the Bot** ▶️
To start the bot, simply run the following command:

```bash
python main.py
```

The bot will automatically:
- Fetch data for 2 randomly selected stocks.
- Perform technical analysis based on your strategy (VWAP, EMA, RSI).
- Send the **buy/sell signal** along with a chart to your Telegram account.

### 2. **Scheduling** 🕒
The bot is scheduled to send updates daily at 9:00 AM by default. You can change the timing in the code if needed.

### 3. **Check for Updates** 🔄
The bot will continuously run in the background, sending daily stock analysis. You can stop it anytime by pressing `CTRL+C`.

---

## 💡 **Configuration**

Here are the key parameters you need to configure:

1. **Alpha Vantage API Key**:
   - Obtain your API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key) and paste it in `config.py`.

2. **Telegram Bot Token**:
   - Get your bot token from [@BotFather](https://core.telegram.org/bots#botfather) on Telegram and paste it in `config.py`.

3. **Telegram Chat ID**:
   - Find your chat ID by visiting [this link](https://api.telegram.org/bot<your_bot_token>/getUpdates) and update `config.py`.

4. **Stock Symbols**:
   - Update the `stock_symbols` list in `main.py` with the stocks you want the bot to analyze. Example:
     ```python
     stock_symbols = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "BAJFINANCE"]
     ```

---

## 🛠️ **Troubleshooting**

Here are a few common errors and how to resolve them:

### 1. **Error: `ModuleNotFoundError`**
- Make sure you have installed all the required packages listed in `requirements.txt`.
- Run `pip install -r requirements.txt` to install missing libraries.

### 2. **Error: `Invalid API Key`**
- Double-check your **Alpha Vantage API Key** in `config.py`.
- Ensure the key is entered correctly.

### 3. **Telegram Error: `Chat not found`**
- Verify the **Telegram Chat ID** in `config.py`.
- Use [this link](https://api.telegram.org/bot<your_bot_token>/getUpdates) to check the chat ID.

---

## 🤝 **Contributing**

If you’d like to contribute to this project, feel free to fork the repository and create a pull request with your improvements or bug fixes!

---

## ✨ **License**

This project is licensed under the MIT License.

---

### Emojis Legend:

- 📈 **Intraday Trading Bot**
- 🛠️ **Installation**
- 🚀 **Usage**
- 💡 **Configuration**
- 🔧 **Troubleshooting**
- 🤖 **Telegram Bot**
- 📊 **Stock Data Analysis**
- 🖼️ **Chart Generation**

---

By following these steps, you should be able to set up your own **Intraday Trading Telegram Bot** and start receiving automated stock recommendations. If you have any questions or issues, feel free to open an issue in the repository!
