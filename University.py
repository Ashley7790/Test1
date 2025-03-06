import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('university_student_dashboard_data.csv')

# Title of the app
st.title("University Admission Data")

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select Year:", int(df["Year"].min()), int(df["Year"].max()), int(df["Year"].min()))

# Filter Data
filtered_df = df[df.year == 'Year']








# Display the Plotly chart in Streamlit
st.plotly_chart(fig)
