from Data.nifty50 import NIFTY50
import yfinance as yf
import pandas as pd

def get_market_indices():
    """
    Returns major Indian market indices.
    """

    indices = {
        "NIFTY 50": "^NSEI",
        "SENSEX": "^BSESN",
        "BANK NIFTY": "^NSEBANK"
    }

    market_data = {}

    for name, symbol in indices.items():

        try:

            ticker = yf.Ticker(symbol)

            info = ticker.history(period="2d")

            current = info["Close"].iloc[-1]
            previous = info["Close"].iloc[-2]

            change = current - previous
            change_percent = (change / previous) * 100

            market_data[name] = {
                "current": round(current, 2),
                "change": round(change, 2),
                "change_percent": round(change_percent, 2)
            }

        except Exception:

            market_data[name] = {
                "current": "N/A",
                "change": "N/A",
                "change_percent": "N/A"
            }

    return market_data

def get_market_mood(indices):
    """
    Determine overall market mood based on index movements.
    """

    positive = 0

    for data in indices.values():

        if (
            isinstance(data["change_percent"], (int, float))
            and data["change_percent"] > 0
        ):
            positive += 1

    if positive >= 2:
        return {
            "mood": "🟢 Bullish",
            "message": "Most major indices are trading in positive territory."
        }

    elif positive == 1:
        return {
            "mood": "🟡 Neutral",
            "message": "Market is showing mixed signals."
        }

    return {
        "mood": "🔴 Bearish",
        "message": "Most major indices are trading lower today."
    }
def get_top_gainers(limit=5):
    """
    Returns top gaining stocks from NIFTY50 using a single Yahoo Finance download.
    """

    tickers = [symbol + ".NS" for symbol in NIFTY50]

    data = yf.download(
        tickers=tickers,
        period="2d",
        group_by="ticker",
        progress=False,
        auto_adjust=True
    )

    gainers = []

    for symbol in NIFTY50:

        ticker = symbol + ".NS"

        try:

            df = data[ticker]

            if len(df) < 2:
                continue

            previous = df["Close"].iloc[-2]
            current = df["Close"].iloc[-1]

            change = current - previous
            percent = (change / previous) * 100

            gainers.append({
                "symbol": symbol,
                "price": round(current, 2),
                "change": round(change, 2),
                "percent": round(percent, 2)
            })

        except Exception:
            continue

    gainers.sort(
        key=lambda x: x["percent"],
        reverse=True
    )

    return gainers[:limit]

def get_top_losers(limit=5):
    """
    Returns top losing stocks from NIFTY50 using a single Yahoo Finance download.
    """

    tickers = [symbol + ".NS" for symbol in NIFTY50]

    data = yf.download(
        tickers=tickers,
        period="2d",
        group_by="ticker",
        progress=False,
        auto_adjust=True
    )

    losers = []

    for symbol in NIFTY50:

        ticker = symbol + ".NS"

        try:

            df = data[ticker]

            if len(df) < 2:
                continue

            previous = df["Close"].iloc[-2]
            current = df["Close"].iloc[-1]

            change = current - previous
            percent = (change / previous) * 100

            losers.append({
                "symbol": symbol,
                "price": round(current, 2),
                "change": round(change, 2),
                "percent": round(percent, 2)
            })

        except Exception:
            continue

    losers.sort(
        key=lambda x: x["percent"]
    )

    return losers[:limit]

def get_most_active(limit=5):
    """
    Returns the most active NIFTY50 stocks based on today's trading volume.
    """

    tickers = [symbol + ".NS" for symbol in NIFTY50]

    data = yf.download(
        tickers=tickers,
        period="2d",
        group_by="ticker",
        progress=False,
        auto_adjust=True
    )

    active = []

    for symbol in NIFTY50:

        ticker = symbol + ".NS"

        try:

            df = data[ticker]

            if len(df) < 1:
                continue

            current = df["Close"].iloc[-1]
            volume = int(df["Volume"].iloc[-1])

            active.append({
                "symbol": symbol,
                "price": round(current, 2),
                "volume": volume
            })

        except Exception:
            continue

    active.sort(
        key=lambda x: x["volume"],
        reverse=True
    )

    return active[:limit]

def get_52_week_breakouts(limit=5):
    """
    Returns stocks trading at or very near their 52-week high.
    """

    tickers = [symbol + ".NS" for symbol in NIFTY50]

    data = yf.download(
        tickers=tickers,
        period="1y",
        group_by="ticker",
        progress=False,
        auto_adjust=True
    )
    
    print("Downloaded tickers:", list(data.columns.levels[0]))    # for testing purposes, to see which tickers were successfully downloaded

    breakouts = []

    for symbol in NIFTY50:

        ticker = symbol + ".NS"
        
        if ticker not in data.columns.levels[0]:
            print(f"Missing ticker: {ticker}")
            continue

        try:

            df = data[ticker]
            
            print(f"{ticker}: {len(df)} rows")
            print(df.tail(2))

            if len(df) < 2:
                continue

            current = df["Close"].iloc[-1]
            high_52 = df["High"].max()

            distance = ((high_52 - current) / high_52) * 100
            
            breakouts.append({
                "symbol": symbol,
                "price": round(current, 2),
                "52_week_high": round(high_52, 2),
                "distance": round(distance, 2)
            })

        except Exception:
            continue

    breakouts.sort(
        key=lambda x: x["distance"]
    )

    return breakouts[:limit]