import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("world_bank_dataset.csv")


st.set_page_config(page_title="World Bank Dashboard", layout="wide")

st.title("🌍 World Bank Development Indicators Dashboard")
st.markdown("""
This interactive dashboard explores global development indicators such as
GDP, population, life expectancy, CO₂ emissions, and access to electricity.
""")

# Sidebar filters
st.sidebar.header("Filters")

country = st.sidebar.selectbox(
    "Select Country",
    sorted(df["country"].unique())
)

indicator_map = {
    "GDP (USD)": "gdp_usd",
    "Population": "population",
    "Life Expectancy": "life_expectancy",
    "CO₂ Emissions per Capita": "co2_emissions_per_capita",
    "Access to Electricity (%)": "access_to_electricity"
}

indicator_label = st.sidebar.selectbox(
    "Select Indicator",
    list(indicator_map.keys())
)

indicator = indicator_map[indicator_label]


filtered_df = df[df["country"] == country].sort_values("year")

# Line chart
st.subheader(f"{indicator_label} over Time for {country}")

fig1 = px.line(
    filtered_df,
    x="year",
    y=indicator,
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# Scatter plots
st.subheader("GDP vs Life Expectancy")

fig2 = px.scatter(
    df,
    x="gdp_usd",
    y="life_expectancy",
    color="country",
    hover_name="country"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("GDP vs CO₂ Emissions per Capita")

fig3 = px.scatter(
    df,
    x="gdp_usd",
    y="co2_emissions_per_capita",
    color="country",
    hover_name="country"
)

st.plotly_chart(fig3, use_container_width=True)


