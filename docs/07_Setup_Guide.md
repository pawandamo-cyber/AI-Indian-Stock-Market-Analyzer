# AI Indian Stock Market Analyzer
# Setup Guide

> **Purpose**
>
> This guide explains how to set up and run the project from scratch.
>
> Follow these steps to clone, configure, and execute the application successfully.

---

# System Requirements

## Operating System

- Windows 10 / 11
- macOS
- Linux

---

## Software Required

- Python 3.13+
- Git
- Visual Studio Code (Recommended)

---

## Python Packages

Project dependencies include:

- streamlit
- yfinance
- pandas
- plotly
- google-generativeai
- python-dotenv
- feedparser

---

# Project Structure

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
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Step 1

Clone Repository

```bash
git clone https://github.com/pawandamo-cyber/AI-Indian-Stock-Market-Analyzer.git
```

---

# Step 2

Open Project

```bash
cd AI-Indian-Stock-Market-Analyzer
```

---

# Step 3

Create Virtual Environment

Windows

```bash
python -m venv .venv
```

---

# Step 4

Activate Virtual Environment

PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
.venv\Scripts\activate.bat
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

# Step 5

Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is unavailable:

```bash
pip install streamlit
pip install yfinance
pip install pandas
pip install plotly
pip install google-generativeai
pip install python-dotenv
pip install feedparser
```

---

# Step 6

Configure Environment Variables

Create a file named

```
.env
```

Example

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

# Step 7

Configure .gitignore

```
.venv/
__pycache__/
.env
API Key.txt
```

---

# Step 8

Run Application

```bash
python -m streamlit run app.py
```

Expected Output

```
Local URL

http://localhost:8501
```

---

# Application Features

The dashboard includes

- Live Stock Search
- Company Information
- Candlestick Chart
- SMA20
- SMA50
- RSI Analysis
- MACD Analysis
- Bollinger Bands
- AI Technical Score
- Gemini AI Advisor
- Live News Feed

---

# Required API

Google Gemini

Used For

- AI Stock Summary
- AI Recommendation
- Technical Interpretation

No API required for

- Yahoo Finance
- Google News RSS

---

# Common Commands

Start Application

```bash
python -m streamlit run app.py
```

Update Packages

```bash
pip install -U -r requirements.txt
```

View Installed Packages

```bash
pip list
```

Freeze Requirements

```bash
pip freeze > requirements.txt
```

Git Status

```bash
git status
```

Commit Changes

```bash
git add .
git commit -m "message"
```

Push Changes

```bash
git push origin main
```

---

# Common Issues

## ModuleNotFoundError

Install missing package

```bash
python -m pip install package_name
```

---

## Gemini API Error

Verify

- API Key
- .env file
- Internet connection

---

## Streamlit Not Updating

Delete

```
__pycache__
```

Restart

- VS Code
- Terminal
- Streamlit

---

## GitHub Push Protection

Never commit

- API Keys
- .env
- Secret files

Store credentials inside

```
.env
```

---

# Verification Checklist

Before running the application

☑ Python Installed

☑ Virtual Environment Activated

☑ Dependencies Installed

☑ .env Created

☑ API Key Added

☑ Internet Connected

☑ Streamlit Installed

---

# Recommended Workflow

```
Create Feature

↓

Test

↓

Commit

↓

Update Documentation

↓

Push to GitHub

↓

Create Release
```

---

# Support

Project Repository

https://github.com/pawandamo-cyber/AI-Indian-Stock-Market-Analyzer

---

Last Updated

July 2026