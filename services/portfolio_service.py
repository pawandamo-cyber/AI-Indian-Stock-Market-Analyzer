import os
import pandas as pd
import plotly.express as px
import yfinance as yf

def calculate_portfolio(portfolio):
    """
    Calculate portfolio performance.
    """

    portfolio_data = []

    total_investment = 0
    total_current_value = 0

    for holding in portfolio:

        symbol = holding["Symbol"].upper()
        quantity = holding["Quantity"]
        buy_price = holding["Buy Price"]
        current_price = holding["Current Price"]

        investment = quantity * buy_price
        current_value = quantity * current_price

        profit_loss = current_value - investment

        return_percent = (
            (profit_loss / investment) * 100
            if investment != 0
            else 0
        )

        portfolio_data.append({

            "Stock": symbol,
            "Quantity": quantity,
            "Buy Price": f"₹{buy_price:,.2f}",
            "Current Price": f"₹{current_price:,.2f}",
            "Investment": f"₹{investment:,.2f}",
            "Current Value": f"₹{current_value:,.2f}",
            "Profit/Loss": f"₹{profit_loss:,.2f}",
            "Return %": f"{return_percent:.2f}%"

        })

        total_investment += investment
        total_current_value += current_value

    total_profit = total_current_value - total_investment

    total_return = (
        (total_profit / total_investment) * 100
        if total_investment != 0
        else 0
    )

    summary = {

        "Total Investment": total_investment,
        "Current Value": total_current_value,
        "Total Profit": total_profit,
        "Total Return": round(total_return, 2)

    }

    return pd.DataFrame(portfolio_data), summary

def save_portfolio(portfolio):

    df = pd.DataFrame(portfolio)

    df.to_csv("portfolio.csv", index=False)


def load_portfolio():

    if os.path.exists("portfolio.csv"):

        df = pd.read_csv("portfolio.csv")

        return df.to_dict("records")

    return []
     
# -----------------------
# Portfolio Allocation
# -----------------------

def create_allocation_chart(portfolio):           
        
    allocation = []

    for holding in portfolio:

        allocation.append({

            "Stock": holding["Symbol"],
            "Investment": holding["Quantity"] * holding["Buy Price"]

        })

    allocation_df = pd.DataFrame(allocation)

    fig = px.pie(

        allocation_df,

        names="Stock",

        values="Investment",

        title="📊 Portfolio Allocation"

    )
    
    return fig

def refresh_live_prices(portfolio):

    for holding in portfolio:

        symbol = holding["Symbol"].upper() + ".NS"

        print("=" * 60)
        print(f"Refreshing {symbol}")

        try:

            stock = yf.Ticker(symbol)

            # Get last 5 trading days
            history = stock.history(period="5d")

            if history.empty:
                print("No history returned. Keeping previous price.")
                continue

            # Remove rows with missing Close values
            history = history.dropna(subset=["Close"])

            if history.empty:
                print("No valid closing price found. Keeping previous price.")
                continue

            # Latest available closing price
            latest_price = history["Close"].iloc[-1]

            if pd.isna(latest_price):
                print("Latest price is NaN. Keeping previous price.")
                continue

            holding["Current Price"] = round(float(latest_price), 2)

            print(f"Updated Price: ₹{holding['Current Price']}")

        except Exception as e:

            print(f"Error updating {symbol}: {e}")

    return portfolio

def get_sector_allocation(portfolio):
    """
    Returns sector-wise investment allocation.
    """

    sector_data = {}

    for holding in portfolio:

        symbol = holding["Symbol"] + ".NS"

        try:
            stock = yf.Ticker(symbol)

            info = stock.info

            print(f"Symbol: {symbol}")
            print(info)

            sector = info.get("sector", "Unknown")

        except Exception:
            sector = "Unknown"

        investment = holding["Quantity"] * holding["Current Price"]

        sector_data[sector] = sector_data.get(sector, 0) + investment

    return sector_data

import plotly.express as px


def create_sector_chart(portfolio):

    sector_data = get_sector_allocation(portfolio)

    fig = px.pie(
        names=list(sector_data.keys()),
        values=list(sector_data.values()),
        title="Sector Allocation"
    )

    fig.update_traces(textposition="inside", textinfo="percent+label")

    return fig

def get_sector_summary(portfolio):

    sector_data = get_sector_allocation(portfolio)

    summary = "\n".join(
        f"{sector}: ₹{value:,.2f}"
        for sector, value in sector_data.items()
    )

    return summary