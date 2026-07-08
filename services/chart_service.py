import yfinance as yf
import plotly.graph_objects as go
import ta
from plotly.subplots import make_subplots


def get_stock_chart(symbol, period="6mo"):

    stock = yf.Ticker(symbol + ".NS")
    hist = stock.history(period=period)

    if hist.empty:
        return go.Figure()

    # Moving averages
    hist["SMA20"] = hist["Close"].rolling(20).mean()
    hist["SMA50"] = hist["Close"].rolling(50).mean()

    # Bollinger Bands
    bb = ta.volatility.BollingerBands(
        close=hist["Close"],
        window=20,
        window_dev=2
    )

    hist["BB_UPPER"] = bb.bollinger_hband()
    hist["BB_MIDDLE"] = bb.bollinger_mavg()
    hist["BB_LOWER"] = bb.bollinger_lband()

    macd = ta.trend.MACD(close=hist["Close"])

    hist["MACD"] = macd.macd()
    hist["MACD_SIGNAL"] = macd.macd_signal()
    hist["MACD_HIST"] = macd.macd_diff()

    # Create two-row layout
    fig = make_subplots(
        rows=3,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.04,
        row_heights=[0.55, 0.15, 0.30],
        subplot_titles=(
            "Price",
            "Volume",
            "MACD"
        ),
         specs=[
            [{"type": "candlestick"}],
            [{"type": "bar"}],
            [{"type": "xy"}]
        ]
    )

    # Candlestick
    fig.add_trace(
        go.Candlestick(
            x=hist.index,
            open=hist["Open"],
            high=hist["High"],
            low=hist["Low"],
            close=hist["Close"],
            name="Price",
            increasing_line_color="green",
            decreasing_line_color="red"
        ),
        row=1,
        col=1
    )

    # SMA20
    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["SMA20"],
            mode="lines",
            name="20 SMA",
            line=dict(color="#2962FF", width=2)
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["BB_LOWER"],
            mode="lines",
            name="Lower Band",
            line=dict(color="gray", dash="dash", width=1)
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["BB_UPPER"],
            mode="lines",
            name="Upper Band",
            line=dict(color="gray", dash="dash", width=1)
        ),
        row=1,
        col=1
    )

    # SMA50
    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["SMA50"],
            mode="lines",
            name="50 SMA",
            line=dict(color="#FF9800", width=2)
        ),
        row=1,
        col=1
    )

    # Volume
    colors = [
        "green" if c >= o else "red"
        for o, c in zip(hist["Open"], hist["Close"])
    ]

    fig.add_trace(
        go.Bar(
            x=hist.index,
            y=hist["Volume"],
            marker_color=colors,
            name="Volume"
        ),
        row=2,
        col=1
    )

    # MACD Line
    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["MACD"],
            mode="lines",
            name="MACD",
            line=dict(color="blue", width=2)
        ),
        row=3,
        col=1
    )

    # Signal Line
    fig.add_trace(
        go.Scatter(
            x=hist.index,
            y=hist["MACD_SIGNAL"],
            mode="lines",
            name="Signal",
            line=dict(color="orange", width=2)
        ),
        row=3,
        col=1
    )

    # MACD Histogram

    colors = [
    "green" if value >= 0 else "red"
    for value in hist["MACD_HIST"]
    ]

    fig.add_trace(
        go.Bar(
            x=hist.index,
            y=hist["MACD_HIST"],
            marker_color=colors,
            name="Histogram"
        ),
        row=3,
        col=1
    )

    fig.update_layout(
        title=f"{symbol} Technical Chart",
        template="plotly_white",
        height=1600,
        xaxis_rangeslider_visible=False,
        legend=dict(
            orientation="h",
            y=1.02,
            x=0
        )
    )

    fig.update_yaxes(title_text="Price (₹)", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)
    fig.update_yaxes(title_text="MACD", row=3, col=1)

    return fig