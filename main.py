import os
import pandas as pd
from nseapi import fetch_nse_data
from strategy import apply_strategy
from telegram.ext import Application
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, CHART_PATH
import random
import schedule
import time

# Set up Telegram bot
application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

async def send_telegram_message(message, photo_path=None):
    """
    Sends message to telegram with optional photo (chart)
    """
    chat_id = TELEGRAM_CHAT_ID
    if photo_path:
        await application.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
    await application.bot.send_message(chat_id=chat_id, text=message)

def fetch_and_analyze():
    # Get a list of stock symbols (you can manually define or fetch from a source)
    stock_symbols = [
        "RELIANCE", "TCS", "INFY", "BAJFINANCE", "HDFCBANK", "SBIN", "LT",
        "ITC", "HCLTECH", "M&M", "TATAMOTORS", "RELIANCE POWER", "ADANIGREEN",
        "MARUTI", "BAJAJ-AUTO", "DRREDDY", "TATAPOWER", "EICHERMOT", "SUNPHARMA",
        "WIPRO"
    ]

    # Randomly select 2 stocks for analysis
    selected_stocks = random.sample(stock_symbols, 2)

    for symbol in selected_stocks:
        # Fetch stock data
        stock_data = fetch_nse_data(symbol)

        if stock_data is not None:
            # Apply the trading strategy
            df = apply_strategy(stock_data, symbol)

            # Get the last signal
            last_signal = df["signals"].iloc[-1]

            # Prepare the message with the recommendation
            message = f"Stock: {symbol}\nSignal: {last_signal}\n\nAnalysis based on strategy."

            # Path to saved chart
            photo_path = f"{CHART_PATH}{symbol}.png"  

            # Send message and chart to Telegram
            send_telegram_message(message, photo_path)

async def job():
    await fetch_and_analyze()

# Schedule the task to run daily at a specific time (e.g., 9 AM)
schedule.every().day.at("09:00").do(job)

# Keep the bot running and execute the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(60)
