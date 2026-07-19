import yfinance as yf
import pandas as pd


HIGHER_IS_BETTER = {
    "Current Price": False,
    "Market Cap": True,
    "P/E Ratio": False,
    "EPS": True,
    "ROE": True,
    "Dividend Yield": True,
    "52 Week High": False,
    "52 Week Low": False,
}

def format_currency(value):
    """Format currency with ₹ symbol."""

    if value is None:
        return "-"

    return f"₹{value:,.2f}"


def format_market_cap(value):
    """Convert Market Cap to Crores/Lakh Crores."""

    if value is None:
        return "-"

    crore = value / 10000000  # 1 Crore = 10,000,000

    if crore >= 100000:
        return f"₹{crore / 100000:.2f} L Cr"

    return f"₹{crore:,.2f} Cr"


def format_percentage(value):
    """Convert decimal to percentage."""

    if value is None:
        return "-"

    return f"{value * 100:.2f}%"

def get_stock_metrics(symbol):

    ticker = yf.Ticker(symbol + ".NS")
    info = ticker.info

    return {
        "Current Price": info.get("currentPrice"),
        "Market Cap": info.get("marketCap"),
        "P/E Ratio": info.get("trailingPE"),
        "EPS": info.get("trailingEps"),
        "ROE": info.get("returnOnEquity"),
        "Dividend Yield": info.get("dividendYield"),
        "52 Week High": info.get("fiftyTwoWeekHigh"),
        "52 Week Low": info.get("fiftyTwoWeekLow"),
    }

def compare_stocks(stock1, stock2):

    data1 = get_stock_metrics(stock1)
    data2 = get_stock_metrics(stock2)
    
    formatted_data1 = data1.copy()
    formatted_data2 = data2.copy()

    formatted_data1["Current Price"] = format_currency(data1["Current Price"])
    formatted_data2["Current Price"] = format_currency(data2["Current Price"])

    formatted_data1["Market Cap"] = format_market_cap(data1["Market Cap"])
    formatted_data2["Market Cap"] = format_market_cap(data2["Market Cap"])

    formatted_data1["EPS"] = format_currency(data1["EPS"])
    formatted_data2["EPS"] = format_currency(data2["EPS"])

    formatted_data1["ROE"] = format_percentage(data1["ROE"])
    formatted_data2["ROE"] = format_percentage(data2["ROE"])

    formatted_data1["Dividend Yield"] = format_percentage(data1["Dividend Yield"])
    formatted_data2["Dividend Yield"] = format_percentage(data2["Dividend Yield"])
    
    formatted_data1["52 Week High"] = format_currency(data1["52 Week High"])
    formatted_data2["52 Week High"] = format_currency(data2["52 Week High"])

    formatted_data1["52 Week Low"] = format_currency(data1["52 Week Low"])
    formatted_data2["52 Week Low"] = format_currency(data2["52 Week Low"])

    winners = []

    for metric in data1.keys():

        value1 = data1[metric]
        value2 = data2[metric]

        if value1 is None or value2 is None:
            winners.append("-")
            continue

        if HIGHER_IS_BETTER[metric]:

            if value1 > value2:
                winners.append(stock1.upper())

            elif value2 > value1:
                winners.append(stock2.upper())

            else:
                winners.append("Tie")

        else:

            if value1 < value2:
                winners.append(stock1.upper())

            elif value2 < value1:
                winners.append(stock2.upper())

            else:
                winners.append("Tie")
                
    score1 = winners.count(stock1.upper())
    score2 = winners.count(stock2.upper())

    comparison = pd.DataFrame({
        "Metric": list(data1.keys()),
        stock1.upper(): list(formatted_data1.values()),
        stock2.upper(): list(formatted_data2.values()),
        "🏆 Winner": winners
    })
    
    return comparison, score1, score2