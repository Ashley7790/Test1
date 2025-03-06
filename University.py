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

# Sidebar Filters
st.sidebar.header("Filters")

# Year filter
year_filter = st.sidebar.multiselect("Select Year", options=df['Year'].unique(), default=df['Year'].unique())
df = df[df['Year'].isin(year_filter)]

# Term filter
term_filter = st.sidebar.multiselect("Select Term", options=df['Term'].unique(), default=df['Term'].unique())
df = df[df['Term'].isin(term_filter)]


# Create the new column 'YearTerm' (after filtering)
df['YearTerm'] = df['Year'] + ' ' + df['Term']

# KPIs
st.metric("Total Applications", df['Applications'].sum())
st.metric("Total Admitted", df['Admitted'].sum())
st.metric("Total Enrolled", df['Enrolled'].sum())

# Chart
st.subheader("University Trends in Admissions")
st.line_chart(df, x="YearTerm", y=["Admitted", "Enrolled", "Applications"])


# create a line chart for retention rate and student satisfaction by year and term
fig = px.line(df, x='YearTerm', y=['Retention Rate (%)', 'Student Satisfaction (%)'],
              labels={'value': 'Percent', 'YearTerm': 'Year and Term'},
              title='Retention Rate and Student Satisfaction by Year and Term')







