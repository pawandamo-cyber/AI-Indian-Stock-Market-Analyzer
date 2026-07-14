import yfinance as yf

INDICES = {
    "NIFTY 50": "^NSEI",
    "SENSEX": "^BSESN",
    "BANK NIFTY": "^NSEBANK",
    "NIFTY IT": "^CNXIT",
    "NIFTY AUTO": "^CNXAUTO"
}


def get_live_indices():

    market = {}

    for name, symbol in INDICES.items():

        try:

            ticker = yf.Ticker(symbol)

            hist = ticker.history(period="2d")

            if len(hist) < 2:
                continue

            current = hist["Close"].iloc[-1]
            previous = hist["Close"].iloc[-2]

            change = current - previous

            percent = (change / previous) * 100

            market[name] = {
                "price": round(current, 2),
                "change": round(change, 2),
                "percent": round(percent, 2)
            }

        except Exception:
            continue

    return market

def render_market_ticker(market):

    html = """
    <style>

    .ticker-container{
        display:flex;
        justify-content:space-around;
        align-items:center;
        background:#f5f5f5;
        padding:12px;
        border-radius:10px;
        margin-bottom:20px;
        border:1px solid #ddd;
    }

    .ticker-item{
        text-align:center;
        font-family:Arial;
    }

    .ticker-name{
        font-weight:bold;
        font-size:15px;
    }

    .ticker-price{
        font-size:18px;
        margin-top:4px;
    }

    .positive{
        color:green;
        font-weight:bold;
    }

    .negative{
        color:red;
        font-weight:bold;
    }

    </style>

    <div class="ticker-container">
    """

    for name, data in market.items():

        color = "positive"

        arrow = "▲"

        if data["change"] < 0:
            color = "negative"
            arrow = "▼"

        html += f"""

        <div class="ticker-item">

            <div class="ticker-name">
                {name}
            </div>

            <div class="ticker-price">
                {data['price']}
            </div>

            <div class="{color}">
                {arrow} {data['change']} ({data['percent']}%)
            </div>

        </div>

        """

    html += "</div>"

    return html