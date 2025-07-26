import pandas as pd
import plotly.express as px

# hard‑coded lat/lon for cities in the dataset
_COORDS = {
    "Seattle": (47.6062, -122.3321),
    "Bellevue": (47.6101, -122.2015),
    "Redmond": (47.6730, -122.1215),
    "Kirkland": (47.6815, -122.2087),
    "Renton": (47.4829, -122.2171),
    "Issaquah": (47.5301, -122.0326),
    "Federal Way": (47.3223, -122.3126),
    "Auburn": (47.3073, -122.2285),
    "Kent": (47.3809, -122.2348),
    "Sammamish": (47.6163, -122.0356),
    "Woodinville": (47.7543, -122.1635),
    "Duvall": (47.7427, -121.9854),
    "Maple Valley": (47.3923, -122.0456),
    "North Bend": (47.4932, -121.7868),
    "Carnation": (47.6476, -121.9143),
    "Black Diamond": (47.3207, -122.0043),
    "Snoqualmie": (47.5288, -121.8250),
    "Fall City": (47.5679, -121.8887),
    "Skykomish": (47.7093, -121.3576),
    "Newcastle": (47.5387, -122.1704),
    "Clyde Hill": (47.6272, -122.2146),
    "Yarrow Point": (47.6440, -122.2196),
    "Medina": (47.6200, -122.2307),
    "Beaux Arts Village": (47.5824, -122.2015),
}

def avg_price_map(df: pd.DataFrame):
    """Return a Plotly scatter‑mapbox figure of average house prices per city."""
    avg = df.groupby("city")["price"].mean().reset_index()
    avg = avg[avg["city"].isin(_COORDS)]
    if avg.empty:
        return None

    avg["lat"] = avg["city"].map(lambda c: _COORDS[c][0])
    avg["lon"] = avg["city"].map(lambda c: _COORDS[c][1])

    fig = px.scatter_mapbox(
        avg, lat="lat", lon="lon",
        size="price", color="price",
        hover_name="city",
        zoom=8, height=600,
        title="Average House Prices by City (Map)",
        color_continuous_scale="Viridis",
    )
    fig.update_layout(
        mapbox_style="carto-positron",
        margin=dict(l=0, r=0, t=40, b=0)
    )
    return fig
