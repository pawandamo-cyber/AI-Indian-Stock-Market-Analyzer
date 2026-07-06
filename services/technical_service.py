import yfinance as yf
import ta


def calculate_rsi(symbol, period="6mo"):
    """
    Calculate the latest RSI (14) value and its interpretation.
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

    latest_rsi = round(hist["RSI"].iloc[-1], 2)

    if latest_rsi < 30:
        signal = "🟢 Oversold"
        recommendation = "BUY"

    elif latest_rsi > 70:
        signal = "🔴 Overbought"
        recommendation = "SELL"

    else:
        signal = "🟡 Neutral"
        recommendation = "HOLD"

    return {
        "value": latest_rsi,
        "signal": signal,
        "recommendation": recommendation
    }