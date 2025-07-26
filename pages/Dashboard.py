import streamlit as st
import pathlib

import core.loader as loader
import core.filters as filters
import core.stats as stats

import viz.city as v_city
import viz.city_map as v_map         
import viz.correlation as v_corr
import viz.sqft as v_sqft
import viz.condition as v_cond
import viz.renovation as v_reno
import viz.build_year as v_build

# ───────────────────── Config ─────────────────────
DATA_PATH = pathlib.Path("data/USA_Housing_Dataset.csv")
st.set_page_config(page_title="Housing Market Dashboard", layout="wide")
st.title("🏠 Housing Market Dashboard")

# ───────────────────── Load data ─────────────────────
df = loader.load(DATA_PATH)

# ───────────────────── Sidebar filters ─────────────────────
st.sidebar.header("Filters")

price_min, price_max = int(df.price.min()), int(df.price.max())
price_range = st.sidebar.slider("Price (USD)", price_min, price_max,
                                (price_min, price_max), step=10_000)

bed_min, bed_max = int(df.bedrooms.min()), int(df.bedrooms.max())
bedrooms = st.sidebar.slider("Bedrooms", bed_min, bed_max, (bed_min, bed_max))

bath_min, bath_max = float(df.bathrooms.min()), float(df.bathrooms.max())
bathrooms = st.sidebar.slider("Bathrooms", bath_min, bath_max, (bath_min, bath_max))

year_min, year_max = int(df.yr_built.min()), int(df.yr_built.max())
year_built = st.sidebar.slider("Year Built", year_min, year_max, (year_min, year_max))

cities = st.sidebar.multiselect("City",
                                options=sorted(df.city.unique()),
                                default=sorted(df.city.unique()))

filtered_df = filters.apply(df, price_range, bedrooms, bathrooms, year_built, cities)

if filtered_df.empty:
    st.warning("No properties match the selected filters.")
    st.stop()

# ───────────────────── Key metrics ─────────────────────
col1, col2, col3,col4 = st.columns(4)
col1.metric("Average Price", f"${filtered_df.price.mean():,.0f}")
col2.metric("Max Price", f"${filtered_df.price.max():,.0f}")
col3.metric("Most Common City", filtered_df.city.mode()[0])
avg_price_per_sqft = filtered_df.price.sum() / filtered_df.sqft_living.sum()
col4.metric("Avg Price per Sqft", f"${avg_price_per_sqft:,.2f}")



# ───────────────────── Detailed stats ─────────────────────
st.header("Detailed Summary Statistics")
st.dataframe(stats.detailed(filtered_df))

# ───────────────────── Visualisations ─────────────────────
st.header("Visualisations")
st.plotly_chart(v_city.houses_per_city(filtered_df), use_container_width=True)
st.plotly_chart(v_corr.price_corr(filtered_df), use_container_width=True)
st.plotly_chart(v_sqft.price_vs_sqft(df), use_container_width=True)
st.plotly_chart(v_cond.price_by_condition(filtered_df), use_container_width=True)
st.plotly_chart(v_city.avg_price(filtered_df), use_container_width=True)
# city‑wise map
fig_map = v_map.avg_price_map(filtered_df)
if fig_map:
    st.plotly_chart(fig_map, use_container_width=True)

fig_reno = v_reno.price_by_renovation(df)
if fig_reno:
    st.plotly_chart(fig_reno, use_container_width=True)

st.plotly_chart(v_build.price_by_build_decade(df), use_container_width=True)



# ───────────────────── Download ─────────────────────
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)
csv_bytes = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download filtered data as CSV",
                   data=csv_bytes,
                   file_name="filtered_housing_data.csv",
                   mime="text/csv")
