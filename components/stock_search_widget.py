import streamlit as st

from services.stock_search_service import (
    load_stock_master,
    search_company,
    get_symbol,
)


def stock_search_widget(key="stock"):
    df = load_stock_master()

    # Search box
    query = st.text_input(
        "🔍 Search Company",
        key=f"{key}_search",
        placeholder="Type company name...",
    )

    if not query:
        return ""

    # Matching companies
    matches = search_company(query)

    if len(matches) == 0:
        st.warning("No matching companies found.")
        return ""

    company = st.selectbox(
        "🏢 Matching Companies",
        matches,
        key=f"{key}_company",
    )

    symbol = get_symbol(company)

    st.success(f"✅ Selected Stock: {symbol}")

    return symbol