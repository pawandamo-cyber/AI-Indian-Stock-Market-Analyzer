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

        print("=" * 50)
        print("Checking:", symbol)

        try:

            stock = yf.Ticker(symbol)

            print("Fast Info:", stock.fast_info)

            history = stock.history(period="5d")

            print(history.tail())

            if not history.empty:

                latest_price = history["Close"].iloc[-1]

                print("Latest Close:", latest_price)

                holding["Current Price"] = round(float(latest_price), 2)

        except Exception as e:

            print("ERROR:", e)

    return portfolio