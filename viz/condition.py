import pandas as pd
import plotly.express as px

def price_by_condition(df: pd.DataFrame):
    avg = df.groupby("condition")["price"].mean().reset_index()
    return px.bar(avg, x="condition", y="price", title="Average Price by Condition")
