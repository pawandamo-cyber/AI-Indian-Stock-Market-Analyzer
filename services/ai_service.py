import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_ai_summary(stock, company, rsi, macd, bollinger, overall, news):

    prompt = f"""
You are a Senior Indian Stock Market Analyst specializing in Indian equities.

Your task is to combine BOTH technical indicators and the latest company news
to produce an intelligent stock analysis.

=================================================

Stock Symbol:
{stock}

Company:
{company}

=================================================
TECHNICAL ANALYSIS

RSI
- Value: {rsi['value']}
- Signal: {rsi['signal']}
- Recommendation: {rsi['recommendation']}

MACD
- Value: {macd['macd']}
- Signal Line: {macd['signal']}
- Recommendation: {macd['recommendation']}

Bollinger Bands
- Status: {bollinger['status']}
- Recommendation: {bollinger['recommendation']}

Overall Technical Score

Score:
{overall['score']} / 6

Confidence:
{overall['confidence']}%

Technical Recommendation:
{overall['recommendation']}

=================================================
LATEST NEWS

{news}

=================================================

Generate a professional report using the following format.

# 🤖 Overall Market Sentiment

State whether the overall outlook is:

Bullish

Bearish

Neutral

Explain in 2-3 sentences.

# 📈 Technical Analysis

Summarize what the technical indicators suggest.

# 📰 News Impact

Analyse the latest news.

Mention whether the news is:

Positive

Negative

Neutral

Explain WHY.

# ⚠️ Risk Factors

Mention 2-3 important risks.

# 📅 Short-Term Outlook

Provide a short outlook for the next few trading sessions.

# 🎯 Final Recommendation

Recommendation:
BUY / HOLD / SELL

Confidence:
XX%

Give a one-line investment conclusion.

Rules

- Keep the report under 300 words.
- Use markdown headings.
- Do not mention that you are an AI.
- Combine BOTH technical indicators and news.
- If news is limited, mention that technical indicators were given more weight.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI Error: {e}"
    