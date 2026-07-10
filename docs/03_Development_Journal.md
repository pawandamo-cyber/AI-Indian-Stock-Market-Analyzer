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