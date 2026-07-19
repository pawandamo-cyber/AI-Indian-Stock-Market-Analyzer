# AI Indian Stock Market Analyzer
# AI Prompt Library

> **Purpose**
>
> This document stores every important AI prompt used throughout the project.
>
> It serves as the central reference for prompt engineering,
> allowing prompts to be improved without searching through source code.
>
> Each prompt includes:
>
> - Purpose
> - Prompt
> - Expected Output
> - Improvements
> - Notes

---

# AI Architecture

Current AI Model

Google Gemini

Current Service

services/ai_service.py

Current Function

generate_ai_summary()

---

# Prompt Version History

| Version | Purpose | Status |
|----------|---------|---------|
| Prompt v1 | Basic Technical Summary | Archived |
| Prompt v2 | Structured Technical Analysis | Active |
| Prompt v3 | AI + News Intelligence | Planned |

---

# ==========================================================
# PROMPT V1
# ==========================================================

## Version

v1.5

---

## Purpose

Generate a basic technical summary using RSI, MACD and Bollinger Bands.

---

## Prompt

```text
You are an expert Indian Stock Market Technical Analyst.

Analyze the provided technical indicators.

Provide:

1. Overall Trend
2. Technical Interpretation
3. Risks
4. Short-Term Outlook

Keep the response under 120 words.
```

---

## Limitations

Returned a simple paragraph.

Formatting inconsistent.

No headings.

No structured recommendation.

---

## Status

Archived

---

# ==========================================================
# PROMPT V2
# ==========================================================

## Version

v1.6

---

## Purpose

Generate a professional AI stock analysis report.

---

## Input

Stock Symbol

Company Name

RSI

MACD

Bollinger Bands

Technical Score

Confidence

Recommendation

---

## Prompt

```text
You are a Senior Indian Stock Market Technical Analyst.

Analyze the provided technical indicators.

Provide your response using the following structure.

## 📈 Overall Trend

Short explanation.

## ✅ Bullish Signals

Bullet points.

## ⚠ Risks

Bullet points.

## 📅 Short-Term Outlook

2-3 sentences.

## 🎯 Final Recommendation

BUY / HOLD / SELL

Confidence

One-line conclusion.

Rules

Keep the response below 200 words.

Use beginner-friendly language.

Do not mention that you are an AI.
```

---

## Improvements

Added

- Structured headings
- Professional formatting
- Bullet points
- Final recommendation
- Confidence
- Better readability

---

## Output Example

```text
📈 Overall Trend

The stock is showing bullish momentum.

✅ Bullish Signals

• RSI improving

• MACD crossover

• Price near support

⚠ Risks

• High volatility

📅 Short-Term Outlook

Positive momentum expected.

🎯 Final Recommendation

BUY

Confidence

82%
```

---

## Status

Current Production Prompt

---

# ==========================================================
# PROMPT V3
# ==========================================================

## Version

v1.7

---

## Purpose

Combine Technical Analysis with Live Market News.

---

## Planned Input

Technical Indicators

+

Google News Headlines

---

## Planned Prompt

```text
You are a Senior Indian Stock Market Technical Analyst.

Use BOTH

1. Technical Indicators

2. Latest News Headlines

Analyze

- Overall Trend
- News Impact
- Bullish Signals
- Risks
- Short-Term Outlook

Provide

Recommendation

BUY / HOLD / SELL

Confidence

Explain how the latest news affects the technical outlook.

Keep the response below 250 words.
```

---

## Expected Improvements

- News-aware AI
- Better reasoning
- Smarter recommendations
- More realistic investment guidance

---

## Status

Planned

---

# Prompt Engineering Guidelines

When designing prompts

Always

- Give the AI a role
- Clearly define the objective
- Provide structured input
- Specify output format
- Set response limits
- Use simple language
- Avoid ambiguous instructions

---

# Prompt Design Principles

Every prompt should contain

Role

↓

Context

↓

Input Data

↓

Expected Output

↓

Formatting Rules

↓

Restrictions

---

# AI Best Practices

Avoid

- Very long prompts
- Ambiguous wording
- Multiple unrelated tasks
- Unstructured output

Prefer

- Clear headings
- Bullet points
- Short paragraphs
- Deterministic responses

---

# Future Prompt Ideas

Prompt 4

Fundamental Analysis

Prompt 5

Portfolio Recommendation

Prompt 6

Risk Assessment

Prompt 7

Sector Comparison

Prompt 8

Investment Strategy

Prompt 9

Long-Term Wealth Advisor

---

# AI Evolution Timeline

v1.5

↓

Basic Summary

↓

v1.6

↓

Professional Report

↓

v1.7

↓

Technical + News Intelligence

↓

v1.8

↓

Technical + News + Fundamentals

↓

v2.0

↓

Complete AI Investment Assistant

---

# Lessons Learned

Prompt engineering is as important as model selection.

A well-designed prompt produces significantly more consistent
and professional AI responses than a generic instruction.

Always improve prompts incrementally and document every major version.

---

Prompt:

Compare two Indian stocks using their technical and fundamental metrics and determine the better investment based on overall performance.

Last Updated

July 2026