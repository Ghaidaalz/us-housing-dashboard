import pandas as pd
import plotly.express as px

def price_by_renovation(df: pd.DataFrame):
    df2 = df[df["yr_renovated"] > 0].copy()
    if df2.empty:
        return None
    df2["decade_renovated"] = (df2["yr_renovated"] // 10) * 10
    avg = df2.groupby("decade_renovated")["price"].mean().reset_index()
    fig = px.line(
        avg, x="decade_renovated", y="price", markers=True,
        title="Average Price by Renovation Decade",
        labels={"decade_renovated": "Renovation Decade", "price": "Average Price"},
    )
    fig.update_xaxes(dtick=10)
    return fig
