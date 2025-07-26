import streamlit as st

# ───────────────────────── page setup
st.set_page_config(
    page_title="US Housing • Overview",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ───────────────────────── Introduction
st.markdown(
    """
    <h1 style="text-align:center;font-size:2.6rem;">🏡 US Housing Market Overview</h1>

    ### Introduction
    This application explores more than four‑thousand residential listings
    from cities in the greater Seattle area.  
    Each record captures details such as interior size, lot size, number of
    bedrooms and bathrooms, construction year, renovation status, and basic
    location information.

    ### Objectives
    * **Visualise** how key property features vary across cities.  
    * **Interactively filter** the dataset to match user‑defined criteria
      (price range, bedrooms, bathrooms, year built, and more).  
    * **Highlight** patterns and outliers for further investigation by
      homeowners, buyers, and real‑estate professionals.
    """,
    unsafe_allow_html=True,
)

# ───────────────────────── CTA
st.markdown("---")
if st.button("🔍 Open the interactive dashboard"):
    st.switch_page("pages/Dashboard.py")

st.caption("Use the sidebar at any time to navigate back to this overview.")
