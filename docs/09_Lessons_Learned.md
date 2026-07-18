# AI Indian Stock Market Analyzer
# Lessons Learned

> **Purpose**
>
> This document records the most important engineering lessons learned
> throughout the development of the project.
>
> Unlike the Developer Journal, this file focuses on knowledge,
> best practices and software engineering principles rather than
> chronological events.

---

# Lesson 001

## Topic

Modular Architecture

---

## Observation

Large applications become difficult to maintain when all logic is placed inside a single file.

---

## Best Practice

Separate responsibilities into independent services.

Example

```
app.py

↓

stock_service.py

↓

technical_service.py

↓

chart_service.py

↓

ai_service.py

↓

news_service.py
```

---

## Result

- Easier debugging
- Better code organization
- Higher maintainability
- Reusable code

==========================================================

# Lesson 002

## Topic

Separate UI from Business Logic

---

## Observation

Business calculations should never exist inside Streamlit pages.

---

## Best Practice

Keep

Streamlit

Responsible only for

- Layout
- Buttons
- Charts
- Display

Move

Calculations

into service modules.

---

## Result

Cleaner architecture.

==========================================================

# Lesson 003

## Topic

Debug Before Changing Code

---

## Observation

Many issues initially appeared to be coding problems.

After investigation, the actual causes were different.

Examples

- Streamlit cache
- Wrong interpreter
- Old running process

---

## Best Practice

Always investigate before rewriting code.

---

## Process

Observe

↓

Investigate

↓

Confirm

↓

Fix

==========================================================

# Lesson 004

## Topic

Financial Data Cannot Be Trusted Blindly

---

## Observation

Yahoo Finance occasionally returns incomplete trading data.

Latest market rows may contain

NaN values.

---

## Best Practice

Always validate incoming data.

Use

```python
dropna()
```

before calculations.

---

## Result

More reliable technical indicators.

==========================================================

# Lesson 005

## Topic

Prompt Engineering Matters

---

## Observation

Changing the prompt produced significantly better AI responses.

No model change required.

---

## Best Practice

Clearly define

- Role
- Context
- Input
- Expected Output
- Formatting
- Restrictions

---

## Result

Professional AI analysis.

==========================================================

# Lesson 006

## Topic

Markdown Produces Better AI Reports

---

## Observation

Displaying AI output using

```python
st.success()
```

removed formatting.

---

## Best Practice

Use

```python
st.markdown()
```

for AI-generated reports.

---

## Result

Professional headings.

Bullet points.

Readable reports.

==========================================================

# Lesson 007

## Topic

Never Commit Secrets

---

## Observation

GitHub Push Protection rejected commits containing API keys.

---

## Best Practice

Store credentials inside

.env

Exclude using

.gitignore

---

## Result

Secure repository.

==========================================================

# Lesson 008

## Topic

Virtual Environments

---

## Observation

Missing packages often occurred because they were installed outside the project's environment.

---

## Best Practice

Always activate

.venv

before installing packages.

Use

```bash
python -m pip install package_name
```

---

## Result

Consistent development environment.

==========================================================

# Lesson 009

## Topic

Documentation Is Part of Development

---

## Observation

Many debugging solutions would have been forgotten without documentation.

---

## Best Practice

Update documentation after every completed sprint.

Maintain

- Developer Journal
- Bug Log
- Release Notes
- Project Context

---

## Result

Project knowledge is preserved.

==========================================================

# Lesson 010

## Topic

Small Releases Are Better

---

## Observation

Building one feature at a time made debugging easier.

---

## Best Practice

Follow

One Sprint

↓

One Feature

↓

One Release

---

## Result

Stable version history.

==========================================================

# Lesson 011

## Topic

Use Git Properly

---

## Observation

Frequent commits made it easier to recover from mistakes.

---

## Best Practice

Commit after every completed feature.

Tag important milestones.

Create GitHub Releases.

---

## Result

Reliable version control.

==========================================================

# Lesson 012

## Topic

Cache Improves Performance

---

## Observation

Repeated Yahoo Finance requests slowed down the application.

---

## Best Practice

Use

```python
@st.cache_data
```

for data retrieval functions.

Do not cache AI responses.

---

## Result

Faster dashboard performance.

==========================================================

# Lesson 013

## Topic

Build Before Optimizing

---

## Observation

Premature optimization slows development.

---

## Best Practice

Finish the feature first.

Optimize later.

---

## Result

Steady project progress.

==========================================================

# Lesson 014

## Topic

Think Like a Software Engineer

---

## Observation

Writing code is only one part of building software.

Engineering also includes

- Planning
- Debugging
- Testing
- Documentation
- Version Control
- Architecture
- Security

---

## Best Practice

Treat every project as if it will eventually be maintained by another developer.

---

## Result

Higher quality software.

==========================================================

# Lesson 015

## Topic

AI Is a Tool, Not a Replacement

---

## Observation

AI accelerates development but does not replace debugging, testing or engineering judgment.

---

## Best Practice

Verify every AI-generated suggestion.

Understand the code before using it.

---

## Result

Better reliability.

==========================================================

# Engineering Principles

Throughout this project the following principles were followed.

✅ Modular Architecture

✅ Service-Oriented Design

✅ Clean Code

✅ Incremental Development

✅ Debug Before Fixing

✅ Documentation First

✅ Git Version Control

✅ Secure Credential Management

✅ AI-Assisted Development

==========================================================

# Personal Takeaways

This project strengthened practical knowledge in:

- Python
- Streamlit
- Plotly
- Git
- GitHub
- Prompt Engineering
- Gemini AI
- Financial APIs
- Debugging
- Software Architecture
- Documentation
- Release Management

==========================================================

# Continuous Improvement

This document should continue growing throughout the life of the project.

Every difficult problem solved should contribute a new lesson.

The goal is not only to build software,
but to become a better software engineer through the process.

---

Last Updated

July 2026

## Lesson

Do not couple technical indicator calculations with chart display periods.

Indicators such as MACD should always use sufficient historical data, regardless of the chart duration selected by the user.

---

## Lesson

Develop one feature at a time using the workflow:

Build → Test → Integrate → Verify

This reduces debugging complexity and improves stability.

## Yahoo Finance Ticker Changes

Issue:
- Tata Motors (TATAMOTORS.NS) returned:
  "Quote not found" and "possibly delisted".

Root Cause:
- Yahoo Finance changed the active ticker from
  TATAMOTORS.NS to TMCV.NS.

Resolution:
- Updated Data/nifty50.py to use TMCV.

Lesson:
- Financial data providers may change ticker symbols due to
  mergers, demergers, or corporate restructuring.
- Periodically validate ticker lists instead of assuming they remain permanent.