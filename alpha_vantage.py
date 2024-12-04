# alpha_vantage.py

import requests
import pandas as pd
from config import ALPHA_VANTAGE_API_KEY

BASE_URL = "https://www.alphavantage.co/query"

def get_intraday_data(symbol, interval="5min"):
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": ALPHA_VANTAGE_API_KEY,
        "outputsize": "full"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Time Series" not in data:
        raise Exception("Error fetching data for symbol: " + symbol)

    time_series_key = f"Time Series ({interval})"
    df = pd.DataFrame(data[time_series_key]).T
    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    }).astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df
