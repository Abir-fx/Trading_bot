# nseapi.py
from nsepy import get_history
from datetime import datetime

def fetch_nse_data(symbol, start_date="2022-01-01", end_date=datetime.today().strftime('%Y-%m-%d')):
    """
    Fetch historical stock data from NSE for a given symbol.
    """
    try:
        df = get_history(symbol=symbol, start=start_date, end=end_date)
        df.reset_index(inplace=True)  # Reset index to get the date column
        return df
    except Exception as e:
        print(f"Error fetching data from NSE: {e}")
        return None
