import yfinance as yf

df = yf.download(
    "TMCV.NS",
    period="1y",
    progress=False,
    auto_adjust=True
)

print(df.tail())