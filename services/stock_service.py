import streamlit as st
import yfinance as yf

@st.cache_data(ttl=300)
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

            # Fundamental Metrics
            "PE Ratio": info.get("trailingPE"),
            "Forward PE": info.get("forwardPE"),
            "EPS": info.get("trailingEps"),
            "Book Value": info.get("bookValue"),
            "Price to Book": info.get("priceToBook"),
            "Dividend Yield": info.get("dividendYield"),
            "ROE": info.get("returnOnEquity"),
            "Debt to Equity": info.get("debtToEquity"),
            "Profit Margin": info.get("profitMargins"),
            "Revenue Growth": info.get("revenueGrowth"),
        }
    
    except Exception as e:
        return {"Error": str(e)}