import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_summary(stock, company, rsi, macd, bollinger, overall):

    prompt = f"""
You are an expert Indian Stock Market Technical Analyst.

Stock: {stock}
Company: {company}

RSI:
Value: {rsi['value']}
Signal: {rsi['signal']}
Recommendation: {rsi['recommendation']}

MACD:
Value: {macd['macd']}
Signal Line: {macd['signal']}
Recommendation: {macd['recommendation']}

Bollinger Bands:
Status: {bollinger['status']}
Recommendation: {bollinger['recommendation']}

Overall Technical Score:
{overall['score']}/6

Confidence:
{overall['confidence']}%

Overall Recommendation:
{overall['recommendation']}

Provide:
1. Overall trend
2. Technical interpretation
3. Risks
4. Short-term outlook

Limit to about 120 words.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"AI Error: {e}"