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

def calculate_macd(symbol, period="6mo"):
    """
    Calculate MACD indicator and signal.
    """

    stock = yf.Ticker(symbol + ".NS")
    hist = stock.history(period=period)

    if hist.empty:
        return None

    macd = ta.trend.MACD(close=hist["Close"])

    hist["MACD"] = macd.macd()
    hist["Signal"] = macd.macd_signal()

    latest_macd = round(hist["MACD"].iloc[-1], 2)
    latest_signal = round(hist["Signal"].iloc[-1], 2)

    if latest_macd > latest_signal:
        trend = "🟢 Bullish"
        recommendation = "BUY"

    elif latest_macd < latest_signal:
        trend = "🔴 Bearish"
        recommendation = "SELL"

    else:
        trend = "🟡 Neutral"
        recommendation = "HOLD"

    return {
        "macd": latest_macd,
        "signal": latest_signal,
        "trend": trend,
        "recommendation": recommendation
    }