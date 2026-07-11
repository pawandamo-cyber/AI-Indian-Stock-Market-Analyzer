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

---

# End of Bug Log