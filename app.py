import streamlit as st
import plotly.express as px
import services.portfolio_service as portfolio_service
from streamlit_autorefresh import st_autorefresh
from services.news_service import (get_stock_news, format_news_for_ai)
from services.stock_service import get_stock_info
from services.chart_service import get_stock_chart
from services.market_service import (get_market_indices, get_market_mood, get_top_gainers, get_top_losers, get_most_active, get_52_week_breakouts)
from services.market_ticker_service import (get_live_indices, render_market_ticker)
from services.ai_service import (generate_ai_summary, generate_portfolio_ai_summary)
from services.technical_service import (calculate_rsi, calculate_macd, calculate_bollinger, calculate_overall_score)
from services.compare_service import compare_stocks

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

    # -------------------------------
    # Remember selected stock
    # -------------------------------

    if "stock" not in st.session_state:
        st.session_state.stock = ""

    stock = st.text_input(
        "🔍 Enter NSE Stock Symbol",
        value=st.session_state.stock,
        placeholder="Example: RELIANCE, TCS, HDFCBANK"
    )

    st.session_state.stock = stock

    # -------------------------------
    # Remember selected period
    # -------------------------------

    periods = [
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "5y"
    ]

    if "period" not in st.session_state:
        st.session_state.period = "6mo"

    period = st.selectbox(
        "Select Chart Duration",
        periods,
        index=periods.index(st.session_state.period)
    )

    st.session_state.period = period

    if "analyze_clicked" not in st.session_state:
        st.session_state.analyze_clicked = False

    if st.button("Analyze Stock"):
        st.session_state.analyze_clicked = True

    if st.session_state.analyze_clicked and stock:

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
                        
            # MACD Analysis    
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
                    
            # Bollinger Bands Analysis        
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

    st.subheader("🚀 52 Week High Breakouts")

    breakouts = get_52_week_breakouts()

    st.dataframe(breakouts, width="stretch")


# ==========================================
# Compare Stocks
# ==========================================

elif menu == "Compare Stocks":

    st.title("📊 Compare Stocks")

    col1, col2 = st.columns(2)

    # Remember selected stocks
    if "compare_stock1" not in st.session_state:
        st.session_state.compare_stock1 = ""

    if "compare_stock2" not in st.session_state:
        st.session_state.compare_stock2 = ""

    with col1:
        stock1 = st.text_input(
            "Stock 1",
            value=st.session_state.compare_stock1,
            placeholder="Example: HDFCBANK"
        )

    with col2:
        stock2 = st.text_input(
            "Stock 2",
            value=st.session_state.compare_stock2,
            placeholder="Example: ICICIBANK"
        )

    # Save user selections
    st.session_state.compare_stock1 = stock1
    st.session_state.compare_stock2 = stock2
    
    # Current stock pair
    current_pair = (
        stock1.upper(),
        stock2.upper()
    )

    # Remember last compared pair
    if "last_compare_pair" not in st.session_state:
        st.session_state.last_compare_pair = current_pair

    # Remember button state
    if "compare_clicked" not in st.session_state:
        st.session_state.compare_clicked = False
        
    # If user changes either stock,
    # hide the old comparison
    if current_pair != st.session_state.last_compare_pair:
        st.session_state.compare_clicked = False
        
    # Compare button
    if st.button("Compare Stocks"):
        st.session_state.compare_clicked = True
        st.session_state.last_compare_pair = current_pair

    #Keep showing comparison after refresh
    if st.session_state.compare_clicked and stock1 and stock2:

            with st.spinner("Comparing Stocks..."):

                comparison, score1, score2 = compare_stocks(
                    stock1,
                    stock2
            )

            st.success("Comparison Completed")
            
            comparison["Metric"] = comparison["Metric"].replace({
                "Current Price": "💰 Current Price",
                "Market Cap": "🏦 Market Cap",
                "P/E Ratio": "📈 P/E Ratio",
                "EPS": "💵 EPS",
                "ROE": "📊 ROE",
                "Dividend Yield": "💎 Dividend Yield",
                "52 Week High": "🚀 52 Week High",
                "52 Week Low": "📉 52 Week Low"
            })

            st.dataframe(
                comparison,
                width="stretch",
                hide_index=True
            )
            
            st.markdown("---")
            st.subheader("🏆 Overall Score")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(stock1.upper(), score1)

            with col2:
                st.metric(stock2.upper(), score2)

            if score1 > score2:

                st.success(
                    f"🥇 Overall Winner : {stock1.upper()}"
                )

            elif score2 > score1:

                st.success(
                    f"🥇 Overall Winner : {stock2.upper()}"
                )

            else:

                st.info("🤝 Overall Result : Tie")

    else:
        st.warning("Enter both stock symbols.")
        
# ==========================================
# Portfolio 
# ==========================================

elif menu == "Portfolio":
    
    st.title("💼 Portfolio Analysis")

    st.markdown("---")

    if "portfolio" not in st.session_state:
        st.session_state.portfolio = portfolio_service.load_portfolio()

    st.subheader("➕ Add Holding")

    col1, col2 = st.columns(2)

    with col1:
        symbol = st.text_input(
            "Stock Symbol",
            placeholder="Example: TCS"
        )

    with col2:
        quantity = st.number_input(
            "Quantity",
            min_value=1,
            step=1
        )

    col3, col4 = st.columns(2)

    with col3:
        buy_price = st.number_input(
            "Buy Price (₹)",
            min_value=0.0,
            step=0.01
        )

    with col4:
        current_price = st.number_input(
            "Current Price (₹)",
            min_value=0.0,
            step=0.01
        )

    if st.button("➕ Add Holding"):

        st.session_state.portfolio.append({

            "Symbol": symbol.upper(),
            "Quantity": quantity,
            "Buy Price": buy_price,
            "Current Price": current_price

        })

        st.success("Holding Added Successfully!")

        st.rerun()
        
    if st.session_state.portfolio:

        df, summary = portfolio_service.calculate_portfolio(
            st.session_state.portfolio
        )

        st.markdown("---")

        st.subheader("📋 Holdings")

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )
        
        # ==========================================
        # Edit Holding
        # ==========================================

        st.markdown("---")

        st.subheader("✏ Edit Holding")

        stock_to_edit = st.selectbox(
            "Select Stock to Edit",
            df["Stock"],
            key="edit_stock"
        )

        selected_holding = next(
            (
                holding
                for holding in st.session_state.portfolio
                if holding["Symbol"] == stock_to_edit
            ),
            None
        )

        if selected_holding:

            col1, col2 = st.columns(2)

            with col1:

                new_quantity = st.number_input(
                    "Quantity",
                    min_value=1,
                    value=selected_holding["Quantity"],
                    step=1,
                    key="edit_quantity"
                )

                new_buy_price = st.number_input(
                    "Buy Price (₹)",
                    min_value=0.0,
                    value=float(selected_holding["Buy Price"]),
                    step=0.01,
                    key="edit_buy"
                )

            with col2:

                new_current_price = st.number_input(
                    "Current Price (₹)",
                    min_value=0.0,
                    value=float(selected_holding["Current Price"]),
                    step=0.01,
                    key="edit_current"
                )

            if st.button("💾 Update Holding"):

                selected_holding["Quantity"] = new_quantity
                selected_holding["Buy Price"] = new_buy_price
                selected_holding["Current Price"] = new_current_price

                st.success(f"{stock_to_edit} updated successfully!")

                st.rerun()
        
        st.markdown("---")

        st.subheader("💰 Portfolio Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total Investment",
                f"₹{summary['Total Investment']:,.2f}"
            )

            st.metric(
                "Total Profit",
                f"₹{summary['Total Profit']:,.2f}"
            )

        with col2:

            st.metric(
                "Current Value",
                f"₹{summary['Current Value']:,.2f}"
            )

            st.metric(
                "Return",
                f"{summary['Total Return']:.2f}%"
            )
            
        # ==========================================
        # Portfolio Allocation
        # ==========================================

        st.markdown("---")
        st.subheader("📊 Portfolio Allocation")

        fig = portfolio_service.create_allocation_chart(
            st.session_state.portfolio
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
      
        st.markdown("---")

        st.subheader("🗑 Remove Holding")

        stock_to_delete = st.selectbox(
            "Select Stock",
            df["Stock"]
        )

        if st.button("Delete Holding"):

            st.session_state.portfolio = [
                holding
                for holding in st.session_state.portfolio
                if holding["Symbol"] != stock_to_delete
            ]

            st.success(f"{stock_to_delete} removed successfully.")

            st.rerun()

        
# ============================
# Save & Load Portfolio
# ============================
        st.markdown("---")

        st.subheader("Portfolio Actions")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("💾 Save Portfolio"):

                portfolio_service.save_portfolio(
                    st.session_state.portfolio
                )

                st.success("Portfolio saved successfully!")

        with col2:

            if st.button("📂 Load Portfolio"):

                st.session_state.portfolio = portfolio_service.load_portfolio()

                st.success("Portfolio loaded successfully!")

                st.rerun()
                
# ============================
# AI Advisor
# ============================            
                
        st.markdown("---")
        st.subheader("🤖 AI Portfolio Advisor")
        if st.button("Generate AI Portfolio Analysis"):
            with st.spinner("Analyzing Portfolio..."):
                ai_response = generate_portfolio_ai_summary(
                    st.session_state.portfolio,
                    summary
                )
            st.success("Analysis Complete")
            st.markdown(ai_response)
            
    # ============================
    # Refresh Live Prices
    # ============================            
                
        st.markdown("---")

        st.subheader("🔄 Live Market")

        if st.button("🔄 Refresh Live Prices"):

            st.session_state.portfolio = portfolio_service.refresh_live_prices(
                st.session_state.portfolio
            )

            st.success("Latest market prices updated!")

            st.rerun()