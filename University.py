import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('university_student_dashboard_data.csv')

# Title of the app
st.title("University Admission Data")

# Convert 'Year' and 'Term' columns to string type if they are not already
df['Year'] = df['Year'].astype(str)
df['Term'] = df['Term'].astype(str)

# Create the new column 'YearTerm'
df['YearTerm'] = df['Year'] + ' ' + df['Term']

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select Year:", int(df["Year"].min()), int(df["Year"].max()), int(df["Year"].min()))


# Sidebar Filter
#st.sidebar.header("Filters")
#term_filter = st.sidebar.selectbox("Select Term", ['All'] + list(df['Term'].unique()))
#if department_filter != 'All':
    #df = df[df['Term'] == term_filter]

# KPIs
st.metric("Total Applications", df['Applications'].sum())
st.metric("Total Admitted", df['Admitted'].sum())
st.metric("Total Enrolled", df['Enrolled'].sum())

# Chart
st.subheader("University Trends in Admissions")
st.line_chart(df, y="Applications",x="YearTerm")






# Display the Plotly chart in Streamlit

