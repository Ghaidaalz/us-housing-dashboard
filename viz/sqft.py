import pandas as pd
import numpy as np
import plotly.express as px

def price_vs_sqft(df: pd.DataFrame, bins: int = 10):
    _bins = np.linspace(df["sqft_living"].min(), df["sqft_living"].max(), bins + 1)
    df2 = df.copy()
    df2["sqft_bin"] = pd.cut(df2["sqft_living"], bins=_bins)
    avg = (
        df2.groupby("sqft_bin")["price"].mean().reset_index()
            .assign(sqft_mid=lambda d: d["sqft_bin"].apply(lambda x: x.mid))
    )
    fig = px.line(
        avg, x="sqft_mid", y="price", markers=True,
        labels={"sqft_mid": "Sqft Living (bin midpoint)", "price": "Average Price (USD)"},
        title="Average House Price by Living‑Area Size",
    )
    return fig
