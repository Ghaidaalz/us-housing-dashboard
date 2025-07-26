import pandas as pd
import plotly.express as px

def price_by_build_decade(df: pd.DataFrame):
    df2 = df.copy()
    df2["decade_built"] = (df2["yr_built"] // 10) * 10
    avg = df2.groupby("decade_built")["price"].mean().reset_index()
    fig = px.line(
        avg, x="decade_built", y="price", markers=True,
        title="Average Price by Decade Built",
        labels={"decade_built": "Decade Built", "price": "Average Price"},
    )
    fig.update_xaxes(dtick=10)
    return fig
