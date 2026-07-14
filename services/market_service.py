import yfinance as yf


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