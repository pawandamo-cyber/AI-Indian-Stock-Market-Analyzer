import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.stock_search_service import (
    load_stock_master,
    search_company,
    get_symbol
)

print("=" * 50)
print("TEST 1 - Loading Stock Master")
print("=" * 50)

stocks = load_stock_master()

print(stocks.head())
print(f"\nTotal Stocks Loaded: {len(stocks)}")

print("\n" + "=" * 50)
print("TEST 2 - Search Company")
print("=" * 50)

results = search_company("ind")

print(results)

print("\n" + "=" * 50)
print("TEST 3 - Get Symbol")
print("=" * 50)

symbol = get_symbol("Indian Oil Corporation")

print("Company : Indian Oil Corporation")
print("Symbol  :", symbol)

print("\n" + "=" * 50)
print("TEST 4 - Invalid Company")
print("=" * 50)

symbol = get_symbol("Google")

print("Result :", symbol)