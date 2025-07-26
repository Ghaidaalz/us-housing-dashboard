import pandas as pd
import streamlit as st

_NUMERIC_COLS = [
    "price", "bedrooms", "bathrooms",
    "sqft_living", "sqft_lot", "floors",
    "sqft_above", "sqft_basement",
    "yr_built", "yr_renovated",
]

@st.cache_data(ttl="1h", show_spinner="Loading data …")
def load(path: str) -> pd.DataFrame:
    """Read the CSV and coerce numeric columns."""
    df = pd.read_csv(path)

    for col in _NUMERIC_COLS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df.dropna(subset=["price", "bedrooms", "bathrooms", "sqft_living"])
