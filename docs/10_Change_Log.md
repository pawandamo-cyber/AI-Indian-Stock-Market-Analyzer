# AI Indian Stock Market Analyzer
# Project Context

> **Purpose**
>
> This document is the single source of truth for the current state of the project.
>
> Uploading this file in a new ChatGPT conversation should provide enough
> context to continue development without reviewing previous conversations.
>
> This file is updated after every completed sprint.

---

# Project Information

Project Name

AI Indian Stock Market Analyzer

Repository

https://github.com/pawandamo-cyber/AI-Indian-Stock-Market-Analyzer

Language

Python

Framework

Streamlit

Current Version

v1.7 Sprint 1

Project Status

🟢 Active Development

Development Methodology

Incremental Sprint-Based Development

---

# Project Objective

Develop a professional AI-powered Indian Stock Market Analysis platform capable of combining:

- Live Stock Market Data
- Technical Indicators
- Artificial Intelligence
- Live News
- Financial Analysis
- Portfolio Management

into a single intelligent dashboard.

---

# Current Architecture

```
AI_Indian_Stock_Market_Analyzer/

│
├── app.py
│
├── services/
│   ├── stock_service.py
│   ├── chart_service.py
│   ├── technical_service.py
│   ├── ai_service.py
│   └── news_service.py
│
├── docs/
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Current Features

## Live Market Data

Completed

- Live NSE Stock Search
- Company Information
- Current Price
- Open
- Previous Close
- Day High
- Day Low
- 52 Week High
- 52 Week Low
- Market Cap
- Volume

---

## Technical Analysis

Completed

- Candlestick Chart
- SMA20
- SMA50
- RSI
- MACD
- Bollinger Bands

---

## AI

Completed

- Google Gemini Integration
- AI Technical Summary
- AI Technical Score
- Confidence Percentage
- Star Rating
- Professional Prompt Engineering

---

## News

Completed

- Google News RSS
- Live Headlines
- Published Date
- Read Full Article Links

---

# Services

## stock_service.py

Responsibilities

- Fetch stock information
- Format company data

---

## chart_service.py

Responsibilities

- Generate Plotly charts
- Candlestick
- SMA20
- SMA50
- Volume

---

## technical_service.py

Responsibilities

- RSI
- MACD
- Bollinger Bands
- Overall Technical Score

---

## ai_service.py

Responsibilities

- Gemini Integration
- AI Prompt
- Technical Summary

---

## news_service.py

Responsibilities

- Google News RSS
- Parse Headlines
- Return Structured News

---

# Current Workflow

User enters stock

↓

Yahoo Finance

↓

Technical Indicators

↓

Google News RSS

↓

Gemini AI

↓

Dashboard

---

# Current Sprint

Version

v1.7 Sprint 2

Objective

Integrate

Technical Indicators

+

Latest News

↓

Gemini AI

↓

Single Intelligent Recommendation

---

# Pending Work

Immediate

- AI + News Integration
- News-aware Gemini Prompt
- News Impact Analysis
- AI Confidence Improvement

Upcoming

- Fundamental Analysis
- Portfolio Tracker
- Watchlist
- Public Deployment

---

# Documentation

Completed

- Project Overview
- Architecture
- Developer Journal
- Bug Log
- Release Notes
- Roadmap
- Setup Guide
- AI Prompt Library
- Lessons Learned

---

# Important Engineering Decisions

✔ Modular Architecture

✔ Service-Oriented Design

✔ Business Logic separated from UI

✔ Prompt Engineering

✔ Documentation First

✔ Sprint-Based Development

✔ Git Versioning

✔ Release Management

---

# Important Lessons

- Always clean financial data before calculations.
- Never commit API keys.
- Use virtual environments.
- Use Markdown for AI responses.
- Debug before changing code.
- Separate UI from business logic.
- Keep documentation updated.

---

# Known Resolved Issues

- MACD rendering
- Bollinger NaN
- Gemini ImportError
- GitHub Push Protection
- feedparser installation
- AI formatting

No active critical bugs.

---

# Development Workflow

Plan Feature

↓

Implement

↓

Test

↓

Debug

↓

Commit

↓

Update Documentation

↓

Push to GitHub

↓

Create Release

---

# Git Status

Current Branch

main

Latest Stable Release

v1.6.1

Current Development

v1.7 Sprint 2

Repository Status

Up to Date

---

# Future Roadmap

v1.7

AI + News Intelligence

↓

v1.8

Fundamental Analysis

↓

v1.9

Portfolio Management

↓

v2.0

Production Deployment

---

# Files Most Frequently Modified

- app.py
- technical_service.py
- ai_service.py
- news_service.py
- chart_service.py

---

# Recommended Files To Upload In New Chat

Minimum

1. 10_Project_Context.md

Recommended

1. 10_Project_Context.md
2. 03_Developer_Journal.md
3. 02_Architecture.md

---

# Instructions For Future ChatGPT Sessions

Before suggesting code:

- Read this document.
- Preserve modular architecture.
- Avoid moving business logic into app.py.
- Continue the current sprint.
- Update documentation after every completed sprint.
- Follow existing coding style.

Current Objective

Continue Version v1.7 Sprint 2

Implement AI-powered News Intelligence by combining technical indicators with live Google News headlines inside the Gemini prompt.

Google News
        │
        ▼
News Service
        │
Formatted News
        │
        ▼
Gemini AI
        ▲
Technical Indicators
        │
        ▼
AI Market Intelligence

---

Last Updated

July 2026

Maintained By

Pawan & ChatGPT