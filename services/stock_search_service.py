import pandas as pd


def load_stock_master():
    return pd.read_csv("data/nse_symbols.csv")


def search_company(search_term: str):

    df = load_stock_master()

    if not search_term:
        return []

    filtered = df[
        df["Company"].str.contains(search_term, case=False, na=False)
        |
        df["Symbol"].str.contains(search_term, case=False, na=False)
    ]

    return [
        f"{row.Company} ({row.Symbol})"
        for _, row in filtered.iterrows()
    ]


def get_symbol(selected):

    if not selected:
        return ""

    return selected.split("(")[-1].replace(")", "").strip()