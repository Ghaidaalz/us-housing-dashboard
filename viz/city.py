import pandas as pd
import plotly.express as px

def houses_per_city(df: pd.DataFrame):
    grouped = df.groupby(['city','condition']).size().reset_index(name='house_count')
    city_order = (grouped.groupby('city')['house_count'].sum().sort_values(ascending=False)
                  .index.tolist())
    fig = px.bar(
        grouped, x='city', y='house_count', color='condition',
        title='Number of Houses per City by Condition',category_orders={"city": city_order},barmode='group',color_discrete_sequence=px.colors.sequential.Plasma)
    fig.update_layout(xaxis_title='City', yaxis_title='Number of Houses',xaxis_tickangle=45)
    return fig

def avg_price(df: pd.DataFrame):
    avg = df.groupby("city")["price"].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(avg, x="city", y="price", title="Average Price by City")
    fig.update_layout(xaxis_tickangle=-45)
    return fig
