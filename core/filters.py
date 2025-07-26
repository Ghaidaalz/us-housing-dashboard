import pandas as pd

def apply(
    df: pd.DataFrame,
    price_range: tuple,
    bedrooms: tuple,
    bathrooms: tuple,
    year_built: tuple,
    cities: list[str],
) -> pd.DataFrame:
    out = df[
        (df["price"].between(*price_range)) &
        (df["bedrooms"].between(*bedrooms)) &
        (df["bathrooms"].between(*bathrooms)) &
        (df["yr_built"].between(*year_built))
    ]
    if cities:
        out = out[out["city"].isin(cities)]
    return out
