# AI Indian Stock Market Analyzer
# Bug Log

> **Purpose**
>
> This document records every important bug encountered during the project.
>
> Unlike the Developer Journal, this file is intended to be a quick
> troubleshooting reference.
>
> Each bug contains:
>
> - Symptoms
> - Root Cause
> - Investigation
> - Resolution
> - Verification
> - Lessons Learned

---

# BUG-0001

## Title

MACD Chart Not Displaying

---

## Version

v1.3

---

## Symptoms

MACD calculations completed successfully.

Chart displayed:

- Candlestick
- SMA20
- SMA50
- Volume

MACD panel missing.

---

## Investigation

Verified:

- Plotly traces
- Layout
- Subplots
- Chart rendering
- Streamlit execution

Printed:

- fig.data
- fig.layout

Confirmed:

MACD traces existed.

---

## Root Cause

Old Streamlit process loaded cached modules.

Application was not executing the latest code.

---

## Resolution

Deleted:

__pycache__

Restarted:

VS Code

Killed:

python.exe

Executed:

python -m streamlit run app.py

---

## Verification

MACD chart displayed successfully.

---

## Status

✅ Resolved

---

## Lesson

Always verify the running process before debugging visualization logic.

==========================================================

# BUG-0002

## Title

Bollinger Bands Displaying NaN

---

## Version

v1.5.1

---

## Symptoms

Dashboard displayed:

Current Price

NaN

Upper Band

NaN

Middle Band

NaN

Lower Band

NaN

---

## Investigation

Printed:

hist.tail()

Observed latest trading row contained:

Open

NaN

High

NaN

Low

NaN

Close

NaN

Volume available.

---

## Root Cause

Yahoo Finance returned an incomplete trading day.

Latest Close value was NaN.

Indicator calculations used the invalid row.

---

## Resolution

Added

```python
hist = hist.dropna(subset=["Close"])
```

before indicator calculations.

---

## Verification

All Bollinger values displayed correctly.

---

## Status

✅ Resolved

---

## Lesson

Never assume financial APIs return complete market data.

Always clean datasets before calculations.

==========================================================

# BUG-0003

## Title

Google Gemini ImportError

---

## Version

v1.5

---

## Symptoms

ImportError

cannot import name 'genai'

---

## Investigation

Checked:

- Installed packages
- Virtual environment
- Google SDK documentation

---

## Root Cause

Incorrect Gemini SDK import.

---

## Resolution

Installed

google-generativeai

Used

```python
import google.generativeai as genai
```

Configured API key correctly.

---

## Verification

Gemini generated AI summaries successfully.

---

## Status

✅ Resolved

---

## Lesson

Always verify SDK documentation before implementation.

==========================================================

# BUG-0004

## Title

GitHub Push Protection Blocked Push

---

## Version

v1.5.1

---

## Symptoms

Git push rejected.

Error:

GH013

Push cannot contain secrets.

---

## Investigation

GitHub Secret Scanning detected

API Key.txt

inside commit history.

---

## Root Cause

Google API key accidentally committed.

---

## Resolution

Removed

API Key.txt

Created

.env

Updated

.gitignore

Generated new API key.

Committed again.

---

## Verification

git push origin main

Completed successfully.

---

## Status

✅ Resolved

---

## Lesson

Never commit

- API Keys
- Passwords
- Secrets

Always use

.env

==========================================================

# BUG-0005

## Title

AI Summary Formatting Incorrect

---

## Version

v1.6

---

## Symptoms

AI output appeared as one large paragraph.

Markdown headings were not rendered.

---

## Root Cause

Displayed using

```python
st.success(ai_summary)
```

instead of markdown.

---

## Resolution

Changed to

```python
st.markdown(ai_summary)
```

Improved Gemini prompt formatting.

---

## Verification

AI response displayed:

- Headings
- Bullet points
- Sections
- Professional formatting

---

## Status

✅ Resolved

---

## Lesson

Use markdown for formatted AI responses.

==========================================================

# BUG-0006

## Title

feedparser ModuleNotFoundError

---

## Version

v1.7

---

## Symptoms

Running

python services/news_service.py

returned

ModuleNotFoundError

No module named 'feedparser'

---

## Root Cause

Package not installed inside the active virtual environment.

---

## Resolution

Executed

```bash
python -m pip install feedparser
```

---

## Verification

Successfully fetched live Google News RSS headlines.

---

## Status

✅ Resolved

---

## Lesson

Always install new packages inside the project's virtual environment.

==========================================================

# BUG-0007

## Title

GitHub Secret Protection During AI Integration

---

## Version

v1.5.1

---

## Symptoms

GitHub blocked push due to secret scanning.

---

## Root Cause

API credentials were accidentally tracked by Git.

---

## Resolution

- Removed tracked secret
- Moved credentials to `.env`
- Updated `.gitignore`
- Generated new API key

---

## Verification

Repository pushed successfully.

---

## Status

✅ Resolved

---

## Lesson

Always configure `.gitignore` before adding secrets to a project.

==========================================================

# Bug Statistics

| Status | Count |
|----------|------:|
| Resolved | 7 |
| Open | 0 |
| Critical | 0 |

---

# Common Debugging Checklist

Before investigating any issue:

- Verify active virtual environment
- Restart Streamlit if UI behaves unexpectedly
- Clear __pycache__ if required
- Confirm correct Python interpreter
- Check terminal logs
- Print intermediate values
- Validate external API responses
- Ensure API keys are loaded from .env
- Verify Git status before pushing

## BUG-011

### Title
MACD displayed `NaN`

### Status
In Progress

### Root Cause

The MACD indicator used the user-selected chart period. Short periods (e.g., 1 month) did not provide enough historical candles for EMA(12), EMA(26), and Signal calculations, resulting in `NaN` values.

### Fix

- Always fetch sufficient historical data (6 months) for MACD.
- Drop rows with `NaN` before reading the latest MACD and Signal values.

---

## BUG-012

### Title
Duplicate imports in `technical_service.py`

### Status
Resolved

### Root Cause

`ta` and `yfinance` were imported twice in the same file.

### Resolution

Removed duplicate imports and retained a single import section at the top.

---

## BUG-013

### Title
Market ticker auto-refresh module not found

### Status
Resolved

### Root Cause

`streamlit-autorefresh` package was not installed in the active virtual environment.

### Resolution

Installed the package in the project virtual environment and verified the correct Python interpreter.

Bug #019

Issue:
TATAMOTORS.NS returned HTTP 404 during yfinance download.

Root Cause:
Yahoo Finance ticker changed to TMCV.NS.

Status:
Resolved

Resolution:
Updated NIFTY50 ticker list.

## v1.10

### Fixed

- Compare Stocks page refresh issue
- Session state reset problem
- Currency formatting
- Market Cap formatting
- Percentage formatting

### Known Issue

- P/E Ratio displays full precision instead of two decimal places.
- Functionality is correct.
- Planned fix in a future version.

# Current Version

**v1.11**

---

# ✅ Bugs Fixed in v1.11

## Portfolio Module

### BUG-001

**Issue**

Portfolio data was lost after restarting the application.

**Status**

✅ Fixed

**Solution**

Implemented CSV-based portfolio persistence with automatic loading during application startup.

---

### BUG-002

**Issue**

Portfolio was not loading automatically.

**Status**

✅ Fixed

**Solution**

Initialized the portfolio using:

```python
load_portfolio()
```

during Streamlit session initialization.

---

### BUG-003

**Issue**

Portfolio Allocation Chart disappeared after editing holdings.

**Status**

✅ Fixed

**Solution**

Recalculated the portfolio before regenerating the Plotly pie chart.

---

### BUG-004

**Issue**

Delete Holding did not immediately refresh the portfolio summary.

**Status**

✅ Fixed

**Solution**

Forced Streamlit rerun after deletion and recalculated portfolio statistics.

---

### BUG-005

**Issue**

ImportError:

```
cannot import name 'refresh_live_prices'
```

**Status**

✅ Fixed

**Solution**

Replaced individual imports with module-based imports.

Old:

```python
from services.portfolio_service import ...
```

New:

```python
import services.portfolio_service as portfolio_service
```

---

### BUG-006

**Issue**

NameError:

```
df is not defined
```

after importing the Portfolio Service.

**Status**

✅ Fixed

**Solution**

Updated every service call to use:

```python
portfolio_service.calculate_portfolio(...)
```

---

### BUG-007

**Issue**

Portfolio AI Advisor produced:

```
TypeError
generate_ai_summary()
missing required positional arguments
```

**Status**

✅ Fixed

**Solution**

Created an independent Gemini prompt specifically for portfolio analysis instead of calling the stock-level AI function.

---

### BUG-008

**Issue**

Live Price Refresh returned previous closing prices for some stocks.

**Status**

✅ Improved

**Solution**

Implemented `fast_info` with fallback to historical closing prices.

Remaining limitation depends on Yahoo Finance data availability.

---

### BUG-009

**Issue**

Some companies such as:

- Indian Oil
- South Indian Bank

did not return updated prices.

**Status**

⚠ Known Limitation

**Reason**

Yahoo Finance requires the official NSE trading symbol instead of the company name.

Examples:

| Company | NSE Symbol |
|----------|------------|
| Indian Oil | IOC |
| South Indian Bank | SOUTHBANK |
| State Bank of India | SBIN |

This will be addressed in Version 1.12 through automatic symbol mapping.

---

# Known Limitations

- Yahoo Finance data may be delayed.
- Some stocks require official NSE symbols.
- Auto-refresh is not implemented.
- Company name search is not available.

---

# Planned Fixes (v1.12)

- Smart Stock Search
- Company Name Search
- Symbol Validation
- Autocomplete
- Sector Allocation
- Historical Portfolio Performance
- Auto Live Refresh

---

# Overall Stability

Current Version: **v1.11**

Application Status:

✅ Stable

Recommended for GitHub Release.

---

# End of Bug Log