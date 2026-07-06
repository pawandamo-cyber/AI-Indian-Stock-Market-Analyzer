import streamlit as st
from services.stock_service import get_stock_info
from services.chart_service import get_stock_chart
from services.technical_service import calculate_rsi
from services.technical_service import calculate_macd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Indian Stock Market Analyzer",
    page_icon="📈",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📊 Navigation")

menu = st.sidebar.radio(
    "Choose a Module",
    [
        "Home",
        "Market Analysis",
        "Technical Analysis",
        "Fundamental Analysis",
        "Compare Stocks",
        "News",
        "Portfolio"
    ]
)

# ----------------------------
# Home Page
# ----------------------------
if menu == "Home":

    st.title("📈 AI Indian Stock Market Analyzer")

    st.write(
        "Welcome! This application helps analyze Indian stocks using "
        "technical indicators, fundamentals, news, and AI."
    )

    stock = st.text_input(
        "🔍 Enter NSE Stock Symbol",
        placeholder="Example: RELIANCE, TCS, HDFCBANK"
    )

    period = st.selectbox(
    "Select Chart Duration",
    [
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "5y"
    ]
)
    if st.button("Analyze Stock"):

        if stock:

            data = get_stock_info(stock.upper())

            if "Error" in data:
                st.error(data["Error"])

            else:

                st.success(f"Analysis for {stock.upper()}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Current Price", data["Current Price"])
                    st.metric("Open", data["Open"])
                    st.metric("Previous Close", data["Previous Close"])
                    st.metric("Day High", data["Day High"])
                    st.metric("Day Low", data["Day Low"])

                with col2:
                    st.metric("52 Week High", data["52 Week High"])
                    st.metric("52 Week Low", data["52 Week Low"])
                    st.metric("Volume", data["Volume"])
                    st.metric("Market Cap", data["Market Cap"])

                st.write("### Company Information")

                st.write("**Sector:**", data["Sector"])
                st.write("**Industry:**", data["Industry"])

                rsi = calculate_rsi(stock.upper(), period)

                macd = calculate_macd(stock.upper(), period)

                st.subheader("📊 Technical Analysis")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("RSI (14)", rsi["value"])

                with col2:
                    st.write("### RSI Signal")

                if "Oversold" in rsi["signal"]:
                    st.success(rsi["signal"])

                elif "Overbought" in rsi["signal"]:
                    st.error(rsi["signal"])

                else:
                    st.warning(rsi["signal"])

                with col3:

                    st.write("### Recommendation")

                if rsi["recommendation"] == "Potential BUY":
                    st.success("🟢 BUY")

                elif rsi["recommendation"] == "Potential SELL":
                    st.error("🔴 SELL")

                else:
                    st.warning("🟡 HOLD")

                    if rsi["recommendation"] == "Potential BUY":
                        st.info("📈 RSI is below 30, indicating the stock may be oversold and could present a buying opportunity.")

                    elif rsi["recommendation"] == "Potential SELL":
                        st.info("📉 RSI is above 70, indicating the stock may be overbought and could face selling pressure.")

                    else:
                        st.info("⚖️ RSI is between 30 and 70, suggesting neutral market momentum.")

                st.subheader("📈 MACD Analysis")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("MACD", macd["macd"])

                with col2:
                    st.metric("Signal Line", macd["signal"])

                with col3:

                    if macd["recommendation"] == "BUY":
                        st.success("🟢 BUY")

                    elif macd["recommendation"] == "SELL":
                        st.error("🔴 SELL")

                    else:
                        st.warning("🟡 HOLD")        

                st.write("## 📈 Stock Price Chart")

                fig = get_stock_chart(stock.upper(), period)

                st.plotly_chart(
                    fig,
                    width="stretch"
                )

        else:
            st.warning("Please enter a stock symbol.")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("NIFTY 50", "--")

    with col2:
        st.metric("SENSEX", "--")

    with col3:
        st.metric("BANK NIFTY", "--")