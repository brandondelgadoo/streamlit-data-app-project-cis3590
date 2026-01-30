import streamlit as st
import pandas as pd
import plotly.express as px

import os
from dotenv import load_dotenv
from apis import api_generator
from pprint import pprint

load_dotenv()

# to run file, in the terminal put: streamlit run (name of file with streamlit)

st.title("Water Quality Dashboard")
st.header("Internship Ready Software Development")
st.subheader("Brandon Delgado")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Descriptive Statistics",
     "2d plots",
     "3d plots",
     "APOD",
     "Asteroids"]
)

with tab1:
    st.info("Working on this")
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    st.info("Still working on it")
    fig1 = px.line(df, x="Time", y="Temperature (c)")
    st.plotly_chart(fig1)
    fig2 = px.scatter(df, x="ODO mg/L", y="Temperature (c)", color="pH")
    st.plotly_chart(fig2)

with tab3:
    st.success("Keep waiting")
    fig3 = px.scatter_3d(df, x="Longitude", y="Latitude", z="Total Water Column (m)", color="Temperature (c)")
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("NASA's Astronomy Picture of the Day")
    response = api_generator("https://api.nasa.gov/planetary/apod?api_key=", os.getenv("NASA_API_KEY"))

    st.subheader(response["title"])
    st.markdown(response["date"])
    st.caption(response["explanation"])
    st.image(response["url"])

with tab5:

    def is_valid_date_range(start, end, max_days=7):
        if start > end:
            return False, "Start date cannot be after end date."

        if (end - start).days > max_days:
            return False, f"Date range cannot exceed {max_days} days."

        return True, None

    st.header("Get Asteroid Information")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    is_valid, error = is_valid_date_range(start_date, end_date)

    if not is_valid:
        st.error(error)
    else:
        response = api_generator(
            "https://api.nasa.gov/neo/rest/v1/feed"
            + f"?start_date={start_date}&end_date={end_date}&api_key=", os.getenv('NASA_API_KEY')
        )

        st.success("Data fetched successfully!")
        for day in response["near_earth_objects"]:
            st.subheader(day)
            pprint(response["near_earth_objects"][day])
            for asteroid in response["near_earth_objects"][day]:
                st.text("Name: " + asteroid["name"])
                st.caption("Link to view asteroid data from NASA's website: " + asteroid["nasa_jpl_url"])
            st.divider()
