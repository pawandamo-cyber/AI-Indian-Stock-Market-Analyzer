# AI Indian Stock Market Analyzer

## Project Overview

AI Indian Stock Market Analyzer is a Python-based web application that helps users analyze Indian stocks listed on the National Stock Exchange (NSE). The application combines real-time market data, technical indicators, interactive charts, and Google Gemini AI to provide easy-to-understand stock insights.

The project is built using a modular service-oriented architecture, making it easy to maintain, extend, and scale with future enhancements.

---

# Project Objectives

- Analyze Indian stocks using real-time market data.
- Visualize price movements with professional charts.
- Calculate important technical indicators.
- Generate AI-powered stock analysis using Google Gemini.
- Build a portfolio-quality project following software engineering best practices.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.x |
| UI | Streamlit |
| Charts | Plotly |
| Market Data | yfinance |
| Technical Indicators | ta |
| AI | Google Gemini |
| Version Control | Git & GitHub |
| Environment | python-dotenv |

---

# Current Features

## Market Data

- Live NSE Stock Data
- Company Information
- Current Price
- Open Price
- Previous Close
- Day High / Low
- 52 Week High / Low
- Market Cap
- Volume
- Sector
- Industry

---

## Technical Analysis

### Price Chart

- Candlestick Chart
- SMA 20
- SMA 50
- Volume

### Indicators

- RSI (Relative Strength Index)
- MACD
- Bollinger Bands

---

## AI Features

- AI Technical Score
- Confidence Score
- Buy / Hold / Sell Recommendation
- Gemini AI Stock Advisor
- AI-generated Technical Summary

---

# Project Architecture

```
app.py
│
├── services/
│   ├── stock_service.py
│   ├── chart_service.py
│   ├── technical_service.py
│   └── ai_service.py
│
├── docs/
├── assets/
├── .env
├── requirements.txt
└── README.md
```

---

# Current Version

**Version:** 1.5

---

# Completed Versions

| Version | Features |
|----------|----------|
| v1.0 | Live Stock Dashboard |
| v1.1 | Candlestick Chart, SMA20, SMA50, Volume |
| v1.2 | RSI Analysis |
| v1.3 | MACD Analysis |
| v1.4 | Bollinger Bands, AI Technical Score |
| v1.5 | Gemini AI Integration, AI Stock Advisor, Improved Architecture |

---

# Key Highlights

- Modular Architecture
- Service Layer Design
- Secure API Key Management using `.env`
- Interactive Plotly Charts
- AI-powered Stock Analysis
- Git Version Control
- Professional Documentation

---

# Future Enhancements

- News Sentiment Analysis
- Fundamental Analysis
- Portfolio Tracker
- Watchlist
- Stock Comparison
- AI Risk Analysis
- Deployment to Streamlit Cloud
- Historical Analysis
- Performance Optimization

## Current Status

Version: v1.8

Sprint: 2

Completed:

- Live Market Ticker
- AI + News Summary
- Fundamental Analysis
- AI Verdict
- Technical Indicators
- Live News
- Navigation Cleanup

Pending:

- Market Analysis
- Compare Stocks
- Portfolio

Next Sprint:

- Finish Market Analysis
- Complete Compare Stocks
- Build Portfolio

## Current Version

**v1.10**

Latest completed module:
- ✅ Compare Stocks

### New Module

Compare two Indian stocks using both technical and fundamental metrics with an overall winner based on multiple evaluation criteria.

# Current Version

**v1.11**

---

# Project Overview

AI Indian Stock Market Analyzer is a Streamlit-based application that combines financial analysis with Generative AI to help investors make informed decisions.

The application supports:

- Technical Analysis
- Fundamental Analysis
- Market Analysis
- Stock Comparison
- News Analysis
- Portfolio Management
- AI Portfolio Advisor

---

# Technology Stack

Frontend

- Streamlit

Backend

- Python

Libraries

- Pandas
- NumPy
- Plotly
- yFinance
- Matplotlib

Artificial Intelligence

- Google Gemini AI

---

# Current Modules

## Home

- Dashboard
- Live Market Ticker

---

## Market Analysis

- NIFTY
- BANKNIFTY
- SENSEX

---

## Technical Analysis

- Candlestick Chart
- SMA
- RSI
- MACD
- Bollinger Bands
- AI Recommendation

---

## Fundamental Analysis

- Company Information
- Financial Ratios
- Valuation Metrics
- AI Summary

---

## Compare Stocks

- Side-by-side comparison
- Technical comparison
- Fundamental comparison
- AI Verdict

---

## News Analysis

- Latest News
- AI News Summary

---

## Portfolio Management

Features

- Add Holdings
- Edit Holdings
- Delete Holdings
- Portfolio Summary
- Allocation Chart
- Save Portfolio
- Load Portfolio
- Auto Load
- Live Price Refresh

---

## AI Portfolio Advisor

Uses Google Gemini AI to generate

- Portfolio Health
- Risk Analysis
- Strengths
- Weaknesses
- Diversification Suggestions
- Investment Advice

---

# Current Project Structure

```
AI-Indian-Stock-Market-Analyzer/

app.py

services/
│
├── stock_service.py
├── chart_service.py
├── news_service.py
├── ai_service.py
└── portfolio_service.py

docs/

assets/

requirements.txt
README.md
```

---

# Architecture

The application follows a modular service-based architecture.

```
Streamlit UI
        │
        ▼
Application Logic
        │
        ▼
Service Layer
        │
        ├── Stock Service
        ├── Chart Service
        ├── News Service
        ├── Portfolio Service
        └── AI Service
        │
        ▼
Yahoo Finance
Google Gemini AI
```

---

# Current Status

Completed Modules

✅ Home

✅ Market Analysis

✅ Technical Analysis

✅ Fundamental Analysis

✅ Compare Stocks

✅ News Analysis

✅ Portfolio Management

✅ AI Portfolio Advisor

---

# Current Release

Version

**v1.11**

Status

✅ Stable

Ready for GitHub Release

---

# Next Development (v1.12)

Upcoming Features

- Smart Stock Search
- Company Name Search
- NSE Symbol Validation
- Autocomplete
- Sector Allocation
- Historical Portfolio Performance
- Auto Live Refresh
- Portfolio Health Score
- Enhanced AI Portfolio Advisor

---

# Long-Term Vision

Transform the application into a complete AI-powered investment assistant capable of:

- Real-time market analysis
- Portfolio optimization
- AI-driven investment insights
- Personalized recommendations
- Advanced visualization
- Professional reporting

---

# Repository

GitHub Repository

https://github.com/pawandamo-cyber/AI-Indian-Stock-Market-Analyzer

---

# Author

**Pawan**

AI Indian Stock Market Analyzer is being developed as a portfolio project to demonstrate practical skills in Python development, data visualization, financial data analysis, AI integration, and software engineering best practices.