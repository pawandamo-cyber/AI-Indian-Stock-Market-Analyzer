import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_stock_chart(symbol, period="6mo"):

    stock = yf.Ticker(symbol + ".NS")
    hist = stock.history(period=period)

    if hist.empty:
        return go.Figure()

    # Moving averages
    hist["SMA20"] = hist["Close"].rolling(20).mean()
    hist["SMA50"] = hist["Close"].rolling(50).mean()

    # Create two-row layout
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[0.75, 0.25]
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

    fig.update_layout(
        title=f"{symbol} Technical Chart",
        template="plotly_white",
        height=900,
        xaxis_rangeslider_visible=False,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_yaxes(title_text="Price (₹)", row=1, col=1)
    fig.update_yaxes(title_text="Volume", row=2, col=1)

    return fig