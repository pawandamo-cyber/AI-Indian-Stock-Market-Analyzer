# AI Indian Stock Market Analyzer
# Developer Journal

> **Purpose**
>
> This document serves as the engineering diary of the project.
>
> It records every important discussion, debugging session, investigation,
> architectural decision, terminal output, solution, and lesson learned.
>
> Unlike release notes, this document preserves *how* problems were solved,
> making it easier to continue development or troubleshoot similar issues in
> the future.

---

# Project Information

Project Name:
AI Indian Stock Market Analyzer

Language:
Python

Framework:
Streamlit

Current Version:
v1.5

Repository:
https://github.com/pawandamo-cyber/AI-Indian-Stock-Market-Analyzer

---

# Development Philosophy

This project follows several engineering principles:

- Modular architecture
- Service-oriented design
- Clean separation of responsibilities
- Small incremental releases
- Git versioning
- Debug before changing code
- Record every important lesson

---

# ==========================================================
# SESSION 01
# ==========================================================

## Goal

Create a live Indian stock dashboard.

---

## Initial Requirements

The application should:

- Search Indian NSE stocks
- Fetch live market information
- Display company information
- Build a clean Streamlit dashboard

---

## Design Decision

Instead of putting all code into app.py,
the project was divided into services.

Reason:

- Easier maintenance
- Easier debugging
- Reusable code
- Cleaner architecture

---

## Files Created

app.py

services/

stock_service.py

---

## Outcome

Successfully displayed:

- Current Price
- Open
- Previous Close
- Day High
- Day Low
- 52 Week High
- 52 Week Low
- Market Cap
- Volume

Status

✅ Completed

---

# ==========================================================
# SESSION 02
# ==========================================================

## Goal

Implement professional stock charts.

---

## Features Added

- Candlestick Chart
- SMA20
- SMA50
- Volume

---

## Design Decision

Plotly was selected instead of Matplotlib.

Reason

- Interactive
- Zoom
- Better UI
- Financial chart support

---

## Files Modified

chart_service.py

app.py

---

## Outcome

Professional interactive stock chart completed.

Status

✅ Completed

---

# ==========================================================
# SESSION 03
# ==========================================================

## Goal

Implement RSI.

---

## Features Added

- RSI Calculation
- Buy / Hold / Sell Logic
- Recommendation
- Interpretation

---

## Design Decision

All technical indicators belong inside

technical_service.py

Reason

Business logic should never exist inside app.py.

---

## Lesson Learned

Keep Streamlit responsible only for presentation.

Business calculations belong inside service classes.

Status

✅ Completed

---

# ==========================================================
# SESSION 04
# ==========================================================

## Goal

Implement MACD.

---

## User Observation

MACD calculations completed.

Chart not visible.

---

## Initial Assumption

Possible Plotly issue.

---

## Investigation 1

Verified traces.

Added:

print(fig)

Result

Chart contained:

Price

20 SMA

50 SMA

Volume

MACD

Signal

Histogram

Conclusion

Plotly generated the chart correctly.

---

## Investigation 2

Printed layout.

Verified:

rows

domains

annotations

Everything looked correct.

---

## Investigation 3

Verified chart_service.py loaded.

Inserted

raise Exception("CHART SERVICE IS RUNNING")

Result

Exception displayed.

Correct file executed.

---

## Investigation 4

Verified app.py executed.

Inserted

raise Exception("APP.PY IS RUNNING")

Result

Confirmed.

---

## Investigation 5

Printed trace count.

Terminal Output

Number of traces: 7

Price

20 SMA

50 SMA

Volume

MACD

Signal

Histogram

Conclusion

Chart generation successful.

Rendering problem existed elsewhere.

---

## Root Cause

Old Streamlit process continued loading cached modules.

---

## Resolution

Deleted

__pycache__

Killed

python.exe

Restarted

VS Code

Activated

.venv

Started application using

python -m streamlit run app.py

---

## Verification

MACD chart appeared correctly.

---

## Lesson Learned

Whenever Streamlit ignores changes:

Verify

- Correct file
- Correct interpreter
- Cached modules
- Running process

Do not immediately assume Plotly is incorrect.

---

## Commands Used

python -m streamlit run app.py

Get-ChildItem -Recurse -Filter chart_service.py

taskkill

---

Status

✅ Resolved

---

# ==========================================================
# SESSION 05
# ==========================================================

## Goal

Implement Bollinger Bands.

---

## Features Added

Upper Band

Middle Band

Lower Band

Recommendation

Interpretation

---

## Initial Result

Implementation completed.

Chart displayed correctly.

Metrics displayed.

---

Status

✅ Feature Completed

---

(To be continued in Part 2...)

Next Sections

- AI Technical Score
- Gemini AI Integration
- Bollinger NaN Investigation
- GitHub Push Protection
- Environment Configuration
- Lessons Learned
- Version 1.5 Release

# ==========================================================
# SESSION 06
# ==========================================================

## Version

v1.4

---

## Goal

Implement AI Technical Score.

---

## User Requirement

Instead of showing individual indicators only, provide a single overall technical recommendation that combines RSI, MACD and Bollinger Bands.

---

## Design Discussion

Initially the application displayed:

- RSI Recommendation
- MACD Recommendation
- Bollinger Recommendation

Each indicator worked independently.

The application lacked an overall conclusion.

---

## Design Decision

Create a dedicated scoring engine inside

technical_service.py

instead of calculating the score inside app.py.

Reason

- Better separation of responsibilities.
- Easier maintenance.
- Easier future expansion.

---

## Scoring Logic

RSI

BUY = +2

HOLD = +1

SELL = +0

MACD

BUY = +2

HOLD = +1

SELL = +0

Bollinger

BUY = +2

HOLD = +1

SELL = +0

Maximum Score

6

---

## Features Added

- Overall Technical Score
- Confidence Percentage
- Overall Recommendation
- Star Rating

---

## UI Discussion

Initially

Technical Score

6

Looked too technical.

Decision

Convert score into

⭐⭐⭐⭐⭐⭐

Reason

Visual indicators improve readability.

---

## Files Modified

technical_service.py

app.py

---

## Lessons Learned

Business rules should remain inside services.

UI should only display the result.

---

## Status

✅ Completed

---

# ==========================================================
# SESSION 07
# ==========================================================

## Version

v1.5

---

## Goal

Integrate Google Gemini AI.

---

## User Requirement

Generate an AI-powered explanation of the technical indicators.

---

## Initial Design

Create

services/ai_service.py

instead of embedding Gemini logic inside app.py.

---

## Reason

Maintain modular architecture.

Future AI improvements should only affect one service.

---

## Environment Configuration

Created

.env

Stored

GOOGLE_API_KEY

Loaded using

python-dotenv

---

## Initial Issue

ImportError

cannot import name 'genai'

---

## Investigation

Checked package installation.

Verified virtual environment.

Compared Google SDK documentation.

---

## Root Cause

Incorrect SDK import.

---

## Resolution

Installed

google-generativeai

Imported

import google.generativeai as genai

Configured

genai.configure(api_key=...)

---

## Verification

Gemini successfully generated stock summaries.

---

## Lessons Learned

Always verify SDK versions before writing code.

---

## Files Created

services/ai_service.py

.env

---

## Files Modified

app.py

requirements.txt

---

## Status

✅ Completed

---

# ==========================================================
# SESSION 08
# ==========================================================

## Version

v1.5.1

---

## Goal

Fix Bollinger Bands displaying NaN.

---

## User Observation

Application displayed

Current Price

NaN

Upper Band

NaN

Middle Band

NaN

Lower Band

NaN

---

## Initial Assumptions

Possible causes

- Incorrect Bollinger formula
- DataFrame issue
- Yahoo Finance issue
- Wrong dataframe row

---

## Investigation 1

Printed latest dataframe.

Code

print(hist.tail())

---

## Terminal Output

History Length

124

Latest Close

NaN

Upper

NaN

Middle

NaN

Lower

NaN

---

## Investigation 2

Printed

hist["Close"].iloc[-1]

Result

NaN

---

## Investigation 3

Observed latest trading day.

Yahoo Finance returned

Open

NaN

High

NaN

Low

NaN

Close

NaN

Volume

Available

---

## Root Cause

Yahoo Finance published an incomplete trading day.

The Bollinger calculation used the final row which contained NaN values.

---

## Failed Attempts

Recalculate Bollinger.

❌ Failed.

Reason

Input data already invalid.

---

## Successful Resolution

Added

hist = hist.dropna(subset=["Close"])

before calculating indicators.

---

## Verification

Current Price

Displayed correctly.

Upper Band

Displayed correctly.

Lower Band

Displayed correctly.

---

## Lessons Learned

Never trust the latest market row.

Always clean financial data before performing calculations.

---

## Files Modified

technical_service.py

---

## Status

✅ Resolved

---

# ==========================================================
# SESSION 09
# ==========================================================

## Version

v1.5.1

---

## Goal

Improve AI output formatting.

---

## User Observation

AI generated only a plain paragraph.

The output looked basic.

---

## Requirement

Produce a professional report.

---

## Design Decision

Rewrite Gemini prompt.

Required sections

- Overall Trend
- Bullish Signals
- Risks
- Short-Term Outlook
- Final Recommendation

---

## UI Improvement

Replaced

st.success(ai_summary)

with

st.markdown(ai_summary)

Reason

Markdown preserves headings and bullet points.

---

## Additional UI Discussion

Reviewed placement of

- Chart
- AI Advisor
- Technical Indicators

Decision

Future versions should display:

Chart

↓

Indicators

↓

AI Summary

---

## Lessons Learned

Prompt engineering significantly improves perceived AI quality.

---

## Files Modified

services/ai_service.py

app.py

---

## Status

✅ Completed

---

# ==========================================================
# SESSION 10
# ==========================================================

## Version

v1.5.1

---

## Goal

Resolve GitHub Push Protection.

---

## User Observation

Git push rejected.

---

## Error

GH013

Repository rule violations found.

Push cannot contain secrets.

---

## Investigation

GitHub Secret Scanning detected

API Key.txt

inside commit history.

---

## Root Cause

Google API Key accidentally committed.

---

## Resolution

Removed

API Key.txt

Generated new API key.

Created

.env

Updated

.gitignore

Recommitted changes.

---

## Verification

git push origin main

Successful.

---

## Lessons Learned

Never commit

- API Keys
- Passwords
- Secrets

Always use

.env

---

## Status

✅ Resolved

# Development Journal

## Date
11 July 2026

## Version
v1.8.0

## Sprint
Sprint 2 - AI Intelligence & Fundamental Analysis

### Completed

- Added AI Verdict Dashboard
- Improved application workflow
- Moved Stock Price Chart higher in the dashboard
- Connected Google News to the AI summary pipeline
- Enhanced Gemini prompt to analyze both technical indicators and latest company news
- Added Fundamental Analysis module
- Added the following financial metrics:
  - PE Ratio
  - Forward PE
  - EPS
  - Book Value
  - Price to Book
  - Dividend Yield
  - ROE
  - Debt to Equity
  - Profit Margin
  - Revenue Growth
- Improved handling of missing values using `is not None`
- Fixed multiple syntax and indentation issues during dashboard restructuring

### Deferred

- AI News Sentiment Engine
  - Decided to remove the separate Gemini call.
  - The functionality will be merged into the main AI analysis to reduce API calls and improve performance.

- Compare Stocks
  - Initial implementation tested.
  - Deferred for a future release due to limited user value compared to remaining modules.

### Next Sprint

- Market Analysis
- Global Market News
- Portfolio Module

## Sprint 2 – Live Market Integration & Technical Enhancements

### Date
July 2026

### Completed

- Implemented Live Market Ticker using Yahoo Finance.
- Created reusable `market_ticker_service.py`.
- Added automatic market data refresh.
- Enhanced AI Summary with market news context.
- Improved Fundamental Analysis module.
- Added financial metrics:
  - P/E Ratio
  - Forward P/E
  - EPS
  - Book Value
  - Price-to-Book
  - Dividend Yield
  - ROE
  - Debt-to-Equity
  - Profit Margin
  - Revenue Growth
- Improved News section with source and publication date.
- Improved Home page navigation and layout.
- Began debugging and stabilizing MACD calculations.

### Challenges

- MACD returned `NaN` due to insufficient historical data and indicator initialization.
- Market Analysis page routing required restructuring.
- Auto-refresh package installation issue (`streamlit-autorefresh`) caused environment mismatch.

### Resolution

- Decoupled indicator calculations from chart display period.
- Introduced reusable services for market ticker.
- Standardized import structure and removed duplicate imports.
- Adopted "Build → Test → Integrate → Verify" workflow for new features.

### Next Sprint

- Complete Market Analysis module.
- Complete Compare Stocks.
- Build Portfolio module.