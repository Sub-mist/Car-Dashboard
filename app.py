# import libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Car Dashboard", page_icon=":automobile:", layout="wide")

# Read data
@st.cache_data
def get_data():
    df = pd.read_csv('./Dataset/cleaned_car_data.csv',index_col=0)
    return df

df = get_data()

valid_fuel_types=['Petrol','Diesel','Hybrid','Electric']
df['fuel_type'] = df['fuel_type'].str.capitalize()
df=filtered=df[df['fuel_type'].isin(valid_fuel_types)]

# Sidebar
st.sidebar.header("Filter")
brand = st.sidebar.multiselect(
    "Select the Brand:",
    options=df['brand'].unique(),
    default=df['brand'].unique()
)

# Radio buttons

transmission_type = st.sidebar.radio(
    "Select the Transmission Type:",
    options = df['transmission_type'].unique()
)

fuel_type = st.sidebar.radio(
    "Select the Fuel type:",
    options = df['fuel_type'].unique()
)

# Apply the sidebar selections
df_select = df.query(
    "brand== @brand & fuel_type ==@fuel_type & transmission_type ==@transmission_type"
)

# If dataframe is empty or not
if df_select.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() ##-- halt streamlit from further execution
    

##---------------------------------------

## Main page

st.title(":racing_car: Car Dashboard")
st.markdown('##')


#calculate KPI's
average_price= int(df_select['price_in_euro'].mean())
car_count = df_select.shape[0]
starting_year = df_select['year'].min()

first_column, second_column , third_column = st.columns(3)

with first_column:
    st.subheader("Average Price:")
    st.subheader(f"€ {average_price:,}")
with second_column:
    st.subheader("Car Count:")
    st.subheader(f"{car_count:,} Cars")
with third_column:
    st.subheader("First Car Manufacturing Year:")
    st.subheader(f"{int(starting_year)}")
    
st.divider()

# Bar chart to show price_in_euro based on color
price_color = df_select.groupby(by=["color"])[["price_in_euro"]].sum().sort_values(by="price_in_euro")

fig_price_color = px.bar(
    price_color,
    x="price_in_euro",
    y=price_color.index,
    orientation="h",
    title="<b>Price in Euros based on Color</b>",
    color_discrete_sequence=["#faf15d"] * len(price_color),
    template="plotly_white",
)

fig_price_color.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# Brand distribution plot
price_brand = df_select.groupby(by=["brand"])[["price_in_euro"]].sum().sort_values(by="price_in_euro")

fig_price_brand = px.bar(
    price_brand,
    x=price_brand.index,
    y="price_in_euro",
    orientation="v",
    title="<b>Price in Euros based on Brand</b>",
    color_discrete_sequence=["#faf15d"] * len(price_brand),
    template="plotly_white",
)

fig_price_brand.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_price_color, use_container_width=True)
right_column.plotly_chart(fig_price_brand, use_container_width=True)

st.divider()

# Pie chart to show Brand distribution
Transmission_type_dist = df.groupby(by=["transmission_type"])[['price_in_euro']].agg('count').sort_values(by='transmission_type')

fig_Transmission_type_dist = px.pie(
    Transmission_type_dist,
    values="price_in_euro",
    title="Transmission Type",
    names=Transmission_type_dist.index,
    color_discrete_sequence=px.colors.sequential.Sunset,
    hole=0.4
)

fig_Transmission_type_dist.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


left_column, middle_column, right_column = st.columns(3)

# Left Part
with left_column:
    min_price = df_select['price_in_euro'].min()
    left_column.metric(
        label = "Minimum Price in Euros of Cars Selected ⏳(€)",
        value = min_price       
    )

    
with left_column:
    max_price = df_select['price_in_euro'].max()
    left_column.metric(
        label = "Maximum Price in Euros of Cars Selected ⏳(€)",
        value = max_price        
    )

    
with left_column:
    median_price = df_select['price_in_euro'].median()
    left_column.metric(
        label = "Median Price in Euros of Stock Selected ⏳(€)",
        value = median_price        
    )

# Middle Part
middle_column.plotly_chart(fig_Transmission_type_dist, use_container_width=True)


# Right Plot
manufactured_year_fig = px.histogram(df_select, 
                             x="year",
                            title='Manufacturing Distribution',
                            color_discrete_sequence=["#faf15d"])

manufactured_year_fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    bargap=0.1,
    xaxis=(dict(showgrid=False))
)

    
right_column.plotly_chart(manufactured_year_fig, use_container_width=True)


# ---- Streamlit Style ----
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    
    footer:after {
        content: 'By Submist';
        visibility: visible;
        display: block;
        position: fixed;
        bottom: 0;
        right: 15px; 
        background: LightBlue;
        color: black;
        padding: 5px 10px;
        font-size: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)