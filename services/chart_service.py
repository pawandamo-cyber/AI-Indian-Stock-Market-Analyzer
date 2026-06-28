import yfinance as yf
import plotly.graph_objects as go

def get_stock_chart(symbol, period="6mo"):

    stock = yf.Ticker(symbol + ".NS")
    hist = stock.history(period=period)

    # Make sure we have data
    if hist.empty:
        fig = go.Figure()
        fig.update_layout(title="No data found")
        return fig

    fig = go.Figure()

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
        )
    )

    fig.update_layout(
        title=f"{symbol} Candlestick Chart",
        xaxis_title="Date",
        yaxis_title="Price (₹)",
        template="plotly_white",
        height=650,
        xaxis_rangeslider_visible=False
    )

    return fig