import pandas as pd
import plotly.express as px

def price_corr(df: pd.DataFrame):
    series = (
        df.corr(numeric_only=True)["price"]
          .drop("price")
          .sort_values()
    )
    fig = px.bar(
        series.reset_index(),
        x="price", y="index",
        orientation="h",
        labels={"index": "Feature", "price": "Correlation with Price"},
        title="Correlation between Price and Other Features",
        color="price", color_continuous_scale="RdBu",
    )
    fig.update_layout(coloraxis_showscale=False)
    return fig
