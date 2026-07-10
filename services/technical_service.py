import streamlit as st
import yfinance as yf
import ta

@st.cache_data(ttl=300)
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

@st.cache_data(ttl=300)
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

import ta
import yfinance as yf


@st.cache_data(ttl=300)
def calculate_bollinger(symbol, period="6mo"):

    stock = yf.Ticker(symbol + ".NS")
    hist = stock.history(period=period)

    # Remove rows where Close is missing
    hist = hist.dropna(subset=["Close"])

    if hist.empty:
        return None

    bb = ta.volatility.BollingerBands(
        close=hist["Close"],
        window=20,
        window_dev=2
    )

    upper = bb.bollinger_hband().iloc[-1]
    middle = bb.bollinger_mavg().iloc[-1]
    lower = bb.bollinger_lband().iloc[-1]
    price = hist["Close"].iloc[-1]

    if price >= upper:
        status = "Above Upper Band"
        recommendation = "SELL"
        interpretation = (
            "Price is trading above the upper Bollinger Band. "
            "This may indicate an overextended move. "
            "Watch for a pullback or breakout confirmation."
        )

    elif price <= lower:
        status = "Below Lower Band"
        recommendation = "BUY"
        interpretation = (
            "Price is trading below the lower Bollinger Band. "
            "The stock may be oversold and could rebound."
        )

    elif price > middle:
        status = "Near Upper Band"
        recommendation = "HOLD"
        interpretation = (
            "Price is above the middle band and showing bullish momentum."
        )

    else:
        status = "Near Lower Band"
        recommendation = "HOLD"
        interpretation = (
            "Price is below the middle band and showing weaker momentum."
        )

        upper = round(bb.bollinger_hband().iloc[-1], 2)
        middle = round(bb.bollinger_mavg().iloc[-1], 2)
        lower = round(bb.bollinger_lband().iloc[-1], 2)

    return {
        "price": round(price, 2),
        "upper": round(upper, 2),
        "middle": round(middle, 2),
        "lower": round(lower, 2),
        "status": status,
        "recommendation": recommendation,
        "interpretation": interpretation
    }

def calculate_overall_score(rsi, macd, bollinger):

    score = 0

    # RSI
    if rsi["recommendation"] == "BUY":
        score += 2
    elif rsi["recommendation"] == "HOLD":
        score += 1

    # MACD
    if macd["recommendation"] == "BUY":
        score += 2
    elif macd["recommendation"] == "HOLD":
        score += 1

    # Bollinger
    if bollinger["recommendation"] == "BUY":
        score += 2
    elif bollinger["recommendation"] == "HOLD":
        score += 1

    # Overall Recommendation
    if score >= 5:
        recommendation = "BUY"
        color = "green"

    elif score >= 3:
        recommendation = "HOLD"
        color = "orange"

    else:
        recommendation = "SELL"
        color = "red"

    confidence = round((score / 6) * 100)
    stars = "⭐" * score + "☆" * (6 - score)

    return {
        "score": score,
        "confidence": confidence,
        "recommendation": recommendation,
        "color": color,
        "stars": stars
    }