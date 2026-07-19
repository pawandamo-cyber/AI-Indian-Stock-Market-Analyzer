# Project Architecture

## Overview

The AI Indian Stock Market Analyzer follows a modular service-oriented architecture. Each module has a single responsibility, making the project easier to maintain, test, and extend.

---

# Architecture Diagram

```
                    +----------------------+
                    |      Streamlit UI    |
                    |       app.py         |
                    +----------+-----------+
                               |
        -------------------------------------------------
        |               |               |               |
        |               |               |               |
+---------------+ +---------------+ +---------------+ +---------------+
| Stock Service | | Chart Service | |Technical Svc  | |  AI Service   |
+---------------+ +---------------+ +---------------+ +---------------+
        |               |               |               |
        |               |               |               |
        +---------------+---------------+---------------+
                               |
                      Yahoo Finance API
                               |
                        Google Gemini API
```

---

# Folder Structure

```
AI_Indian_Stock_Market_Analyzer
│
├── app.py
│
├── services
│   ├── ai_service.py
│   ├── stock_service.py
│   ├── technical_service.py
│   ├── chart_service.py
│   ├── news_service.py
│   ├── market_service.py
│   └── market_ticker_service.py   ← NEW
│
├── docs
│
└── assets
```

---

# Module Responsibilities

## app.py

Responsibilities

- Streamlit User Interface
- User Input
- Display Metrics
- Display Charts
- Display AI Summary
- Connect all services

---

## stock_service.py

Responsibilities

- Fetch stock information
- Retrieve company details
- Retrieve market statistics
- Handle Yahoo Finance requests

Returns

- Company Name
- Current Price
- Open
- Previous Close
- Day High
- Day Low
- Market Cap
- Volume
- Sector
- Industry

---

## chart_service.py

Responsibilities

Generate interactive Plotly charts.

Features

- Candlestick Chart
- SMA 20
- SMA 50
- Volume Chart

---

## technical_service.py

Responsibilities

Calculate technical indicators.

Indicators

- RSI
- MACD
- Bollinger Bands
- AI Technical Score

---

## ai_service.py

Responsibilities

Generate AI-powered stock analysis.

Uses

- Google Gemini API
- Prompt Engineering
- AI Summary Generation

---

# Data Flow

```
User

↓

Enter Stock Symbol

↓

app.py

↓

stock_service.py

↓

Yahoo Finance

↓

Stock Data

↓

technical_service.py

↓

Indicators

↓

chart_service.py

↓

Interactive Charts

↓

ai_service.py

↓

Gemini AI

↓

AI Summary

↓

Streamlit Dashboard
```

---

# External Dependencies

| Package | Purpose |
|----------|----------|
| streamlit | Web UI |
| plotly | Charts |
| yfinance | Market Data |
| ta | Technical Indicators |
| google-generativeai | Gemini AI |
| python-dotenv | Environment Variables |
| pandas | Data Processing |

---

# Design Principles

- Modular Architecture
- Separation of Concerns
- Reusable Services
- Clean Code
- Easy Maintenance
- Scalable Design

---

# Future Architecture

```
services/

stock_service.py

chart_service.py

technical_service.py

ai_service.py

news_service.py

portfolio_service.py

fundamental_service.py

prediction_service.py
```

---

# Architecture Benefits

- Easy to maintain
- Easy to test
- Easy to extend
- Clean separation of responsibilities
- Production-ready structure
- Supports future feature additions without major refactoring

## New Component

### market_ticker_service.py

Responsibilities:

- Fetch live market index data.
- Provide reusable market ticker data.
- Render market ticker HTML.
- Support automatic refresh without affecting other application modules.

### Design Benefits

- Separation of concerns.
- Reusable service.
- Easier maintenance.
- Cleaner `app.py`.

## Compare Service

File:
services/compare_service.py

Responsibilities:

- Fetch stock metrics
- Compare two companies
- Evaluate metric winners
- Calculate overall scores
- Return formatted comparison table