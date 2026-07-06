import yfinance as yf
import ta


def calculate_rsi(symbol, period="6mo"):
    """
    Calculate the latest RSI (14) value.
    """

    stock = yf.Ticker(symbol + ".NS")
    hist = stock.history(period=period)

    if hist.empty:
        return None

    # Calculate RSI
    hist["RSI"] = ta.momentum.RSIIndicator(
        close=hist["Close"],
        window=14
    ).rsi()

    return round(hist["RSI"].iloc[-1], 2)