import yfinance as yf

def get_stock_info(symbol):

    try:
        stock = yf.Ticker(symbol + ".NS")

        info = stock.info

        return {
            "Company Name": info.get("longName", symbol),
            "Current Price": info.get("currentPrice"),
            "Open": info.get("open"),
            "Previous Close": info.get("previousClose"),
            "Day High": info.get("dayHigh"),
            "Day Low": info.get("dayLow"),
            "52 Week High": info.get("fiftyTwoWeekHigh"),
            "52 Week Low": info.get("fiftyTwoWeekLow"),
            "Market Cap": info.get("marketCap"),
            "Volume": info.get("volume"),
            "Sector": info.get("sector"),
            "Industry": info.get("industry"),
    }

    except Exception as e:
        return {"Error": str(e)}