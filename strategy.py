# strategy.py
from indicators import calculate_vwap, calculate_ema, calculate_rsi
import mplfinance as mpf
from config import CHART_PATH

def apply_strategy(df, symbol):
    # Calculate indicators
    df = calculate_vwap(df)
    df = calculate_ema(df, 9)
    df = calculate_ema(df, 21)
    df = calculate_rsi(df)

    # Generate signals
    signals = []
    for i in range(1, len(df)):
        if df["close"].iloc[i] > df["ema_9"].iloc[i] > df["ema_21"].iloc[i] and df["rsi"].iloc[i] < 70:
            signals.append("🟩 BUY")
        elif df["close"].iloc[i] < df["ema_9"].iloc[i] < df["ema_21"].iloc[i] and df["rsi"].iloc[i] > 30:
            signals.append("🟥 SELL")
        else:
            signals.append(None)
    df["signals"] = signals

    # Save chart
    save_chart(df, symbol)
    return df

def save_chart(df, symbol):
    mpf.plot(df.tail(50), type="candle", mav=(9, 21), volume=True, savefig=f"{CHART_PATH}{symbol}.png")
