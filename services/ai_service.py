import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_summary(stock, company, rsi, macd, bollinger, overall):

    prompt = f"""
You are a Senior Indian Stock Market Technical Analyst.

Analyze the following technical indicators and provide a professional stock analysis.

Stock Symbol: {stock}
Company: {company}

Technical Indicators

RSI
- Value: {rsi['value']}
- Signal: {rsi['signal']}
- Recommendation: {rsi['recommendation']}

MACD
- MACD: {macd['macd']}
- Signal Line: {macd['signal']}
- Recommendation: {macd['recommendation']}

Bollinger Bands
- Status: {bollinger['status']}
- Recommendation: {bollinger['recommendation']}

Overall Technical Score
- Score: {overall['score']} / 6
- Confidence: {overall['confidence']}%
- Recommendation: {overall['recommendation']}

Provide your response in the following format.

## 📈 Overall Trend

(One short paragraph)

## ✅ Bullish Signals

- Point 1
- Point 2
- Point 3

## ⚠️ Risks

- Point 1
- Point 2

## 📅 Short-Term Outlook

(2-3 sentences)

## 🎯 Final Recommendation

Recommendation: BUY / HOLD / SELL

Confidence: XX%

One-line conclusion.

Rules

- Keep the response under 200 words.
- Do not mention that you are an AI.
- Base the analysis only on the provided indicators.
- Use simple language suitable for beginner investors.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI Error: {e}"