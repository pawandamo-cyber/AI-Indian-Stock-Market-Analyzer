import streamlit as st
from streamlit_autorefresh import st_autorefresh
from services.news_service import (get_stock_news, format_news_for_ai)
from services.stock_service import get_stock_info
from services.chart_service import get_stock_chart
from services.market_service import (get_market_indices, get_market_mood)
from services.market_ticker_service import (get_live_indices, render_market_ticker)
from services.ai_service import generate_ai_summary
from services.technical_service import (calculate_rsi, calculate_macd, calculate_bollinger, calculate_overall_score)  

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Indian Stock Market Analyzer",
    page_icon="📈",
    layout="wide"
)

st_autorefresh(
    interval=60000,   # Refresh every 60 seconds
    key="market_refresh"
)

market_indices = get_live_indices()

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📊 Navigation")

menu = st.sidebar.radio(
    "Choose a Module",
    [
        "Home",
        "Market Analysis",
        "Compare Stocks",
        "News",
        "Portfolio"
    ]
)

# ----------------------------
# Home Page
# ----------------------------
if menu == "Home":

    if market_indices:

        cols = st.columns(len(market_indices))

        for col, (name, data) in zip(cols, market_indices.items()):

            with col:

                delta = f"{data['change']} ({data['percent']}%)"

                st.metric(
                    label=name,
                    value=data["price"],
                    delta=delta
                )

        st.divider()

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

            #st.write(data)      # Temporary for testing

            news = get_stock_news(stock.upper())

            formatted_news = format_news_for_ai(news)

            if "Error" in data:
                st.error(data["Error"])

            else:

                st.success(f"Analysis for {stock.upper()}")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Current Price", f"₹{data['Current Price']:.2f}")
                    st.metric("Open", f"₹{data['Open']:.2f}")
                    st.metric("Previous Close", f"₹{data['Previous Close']:.2f}")
                    st.metric("Day High", f"₹{data['Day High']:.2f}")
                    st.metric("Day Low", f"₹{data['Day Low']:.2f}")

                with col2:
                    st.metric("52 Week High", f"₹{data['52 Week High']:.2f}")
                    st.metric("52 Week Low", f"₹{data['52 Week Low']:.2f}")

                    st.metric("Volume", f"{data['Volume']:,}")

                    market_cap = data["Market Cap"]

                    if market_cap:
                        market_cap = market_cap / 1e12
                        market_cap = f"₹{market_cap:.2f} Trillion"

                    st.metric("Market Cap", market_cap)

                st.write("### Company Information")

                st.write("**Sector:**", data["Sector"])
                st.write("**Industry:**", data["Industry"])

                # ==========================================
                # Fundamental Analysis
                # ==========================================

                st.subheader("📊 Fundamental Analysis")

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "PE Ratio",
                        f"{data['PE Ratio']:.2f}" if data["PE Ratio"] is not None else "N/A"
                    )

                    st.metric(
                        "EPS",
                        f"{data['EPS']:.2f}" if data["EPS"] is not None else "N/A"
                    )

                    st.metric(
                        "Book Value",
                        f"{data['Book Value']:.2f}" if data["Book Value"] is not None else "N/A"
                    )

                    st.metric(
                        "Price / Book",
                        f"{data['Price to Book']:.2f}" if data["Price to Book"] is not None else "N/A"
                    )

                    st.metric(
                        "Dividend Yield",
                        f"{data['Dividend Yield']:.2f}%"
                        if data["Dividend Yield"] is not None else "N/A"
                    )

                with col2:

                    st.metric(
                        "Forward PE",
                        f"{data['Forward PE']:.2f}" if data["Forward PE"] is not None else "N/A"
                    )

                    st.metric(
                        "ROE",
                        f"{data['ROE']*100:.2f}%"
                        if data["ROE"] is not None else "N/A"
                    )

                    st.metric(
                        "Debt to Equity",
                        f"{data['Debt to Equity']:.2f}"
                        if data["Debt to Equity"] is not None else "N/A"
                    )

                    st.metric(
                        "Profit Margin",
                        f"{data['Profit Margin']*100:.2f}%"
                        if data["Profit Margin"] is not None else "N/A"
                    )

                    st.metric(
                        "Revenue Growth",
                        f"{data['Revenue Growth']*100:.2f}%"
                        if data["Revenue Growth"] is not None else "N/A"
                    )

                st.divider()

                rsi = calculate_rsi(stock.upper(), period)
                macd = calculate_macd(stock.upper(), period)
                bollinger = calculate_bollinger(stock.upper(), period)

                overall = calculate_overall_score(
                    rsi,
                    macd,
                    bollinger
                )

                ai_summary = generate_ai_summary(
                    stock=stock.upper(),
                    company=data["Company Name"],
                    rsi=rsi,
                    macd=macd,
                    bollinger=bollinger,
                    overall=overall,
                    news=formatted_news
                )

                st.divider()

                st.subheader("🤖 AI Verdict")

                col1, col2 = st.columns([1, 2])

                with col1:

                    if overall["recommendation"] == "BUY":
                        st.success("🟢 BUY")

                    elif overall["recommendation"] == "SELL":
                        st.error("🔴 SELL")

                    else:
                        st.warning("🟡 HOLD")

                    st.metric(
                        "Confidence",
                        f"{overall['confidence']}%"
                    )

                    st.metric(
                        "Technical Score",
                        overall["stars"]
                    )

                with col2:

                    st.info(
                        f"""
                ### AI Recommendation

                **Recommendation:** {overall['recommendation']}

                **Confidence:** {overall['confidence']}%

                The recommendation is based on the combined analysis of
                RSI, MACD, and Bollinger Bands.

                *A more detailed AI explanation is available below.*
                """
                    )

                # Star Rating
               
                st.subheader("📊 Technical Analysis")

                st.write("## 📈 Stock Price Chart")

                fig = get_stock_chart(stock.upper(), period)

                st.plotly_chart(fig, width="stretch")

                st.subheader("🧠 AI Technical Score")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Technical Score", overall["stars"])

                with col2:
                    st.metric("Confidence", f"{overall['confidence']}%")
                    st.progress(overall["confidence"] / 100)

                with col3:
                    st.metric("Recommendation", overall["recommendation"])

                if overall["recommendation"] == "BUY":
                    st.success("🟢 Overall Recommendation: BUY")

                elif overall["recommendation"] == "SELL":
                    st.error("🔴 Overall Recommendation: SELL")

                else:
                    st.warning("🟡 Overall Recommendation: HOLD")

                if overall["recommendation"] == "BUY":
                    st.info(
                        "📈 Technical indicators are mostly bullish. "
                        "The stock is showing positive momentum."
                    )

                elif overall["recommendation"] == "SELL":
                    st.info(
                        "📉 Technical indicators suggest weakness. "
                        "Consider waiting for confirmation."
            )

                else:
                    st.info(
                        "⚖️ Technical indicators are mixed. "
                        "Wait for stronger confirmation before taking action."
                    )

                st.subheader("📰 Latest News")

                for article in news:

                    with st.container():

                        st.markdown(f"### 📰 {article['title']}")

                        st.caption(
                            f"{article['source']} • {article['published']}"
                        )

                        st.link_button(
                            "🔗 Read Full Article",
                            article["link"]
                        )

                        st.divider()

                st.subheader("🤖 AI Stock Advisor")

                with st.spinner("🤖 Gemini is analyzing the stock..."):
                    st.markdown(ai_summary)    
                    
                st.subheader("📈 RSI Analysis")    

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

                if rsi["recommendation"] == "BUY":
                    st.success("🟢 BUY")

                elif rsi["recommendation"] == "SELL":
                    st.error("🔴 SELL")

                else:
                    st.warning("🟡 HOLD")

                    if rsi["recommendation"] == "BUY":
                        st.info("📈 RSI is below 30, indicating the stock may be oversold and could present a buying opportunity.")

                    elif rsi["recommendation"] == "SELL":
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

                st.write("## 📊 Bollinger Bands Analysis")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric("Current Price", f"₹{bollinger['price']:.2f}")

                with col2:
                    st.metric("Upper Band", f"₹{bollinger['upper']:.2f}")

                with col3:
                    st.metric("Middle Band", f"₹{bollinger['middle']:.2f}")

                with col4:
                    st.metric("Lower Band", f"₹{bollinger['lower']:.2f}")

                # Status
                st.metric("Status", bollinger["status"])

                # Recommendation
                if bollinger["recommendation"] == "BUY":
                        st.success("🟢 BUY")

                elif bollinger["recommendation"] == "SELL":
                    st.error("🔴 SELL")

                else:
                    st.warning("🟡 HOLD")

                # Interpretation
                st.info(bollinger["interpretation"])

        else:
            st.warning("Please enter a stock symbol.")

# =====================================================
# END OF HOME PAGE
# =====================================================

# ==========================================
# Market Analysis
# ==========================================

elif menu == "Market Analysis":

    st.title("📈 Indian Market Analysis")

    st.write("DEBUG: Market Analysis Page Loaded")

    market = get_market_indices()

    col1, col2, col3 = st.columns(3)

    with col1:

            nifty = market["NIFTY 50"]

            st.metric(
                "NIFTY 50",
                nifty["current"],
                f"{nifty['change']} ({nifty['change_percent']}%)"
        )

            with col2:

                sensex = market["SENSEX"]

                st.metric(
                "SENSEX",
                sensex["current"],
                f"{sensex['change']} ({sensex['change_percent']}%)"
            )

            with col3:

                bank = market["BANK NIFTY"]

                st.metric(
                "BANK NIFTY",
                bank["current"],
                f"{bank['change']} ({bank['change_percent']}%)"
        )

# ==========================================
# Compare Stocks
# ==========================================

elif menu == "Compare Stocks":

    st.title("📊 Compare Two Stocks")

    col1, col2 = st.columns(2)

    with col1:
        stock1 = st.text_input(
            "Stock 1",
            placeholder="Example: TCS"
        )

    with col2:
        stock2 = st.text_input(
            "Stock 2",
            placeholder="Example: INFY"
        )

    if st.button("Compare"):

        if stock1 and stock2:

            data1 = get_stock_info(stock1.upper())
            data2 = get_stock_info(stock2.upper())

            st.subheader("Comparison")

        else:
            st.warning("Please enter both stock symbols.")
