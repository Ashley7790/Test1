import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib as plt

# Load Data
df = pd.read_csv('university_student_dashboard_data.csv')

# Title of the app
st.title("University Admission Data")

# Convert 'Year' and 'Term' columns to string type if they are not already
df['Year'] = df['Year'].astype(str)
df['Term'] = df['Term'].astype(str)

# Create the new column 'YearTerm'
df['YearTerm'] = df['Year'] + ' ' + df['Term']


# Sidebar Filter
#st.sidebar.header("Filters")
#term_filter = st.sidebar.selectbox("Select Year", ['All'] + list(df['Year'].unique()))
#if term_filter != 'All':
#   df = df[df['Year'] == term_filter]


# Sidebar Filter
#st.sidebar.header("Filters")
#term_filter = st.sidebar.selectbox("Select Year", ['All'] + list(df['Year'].unique()))
#term_filter2 = st.sidebar.selectbox("Select Term", ['All'] + list(df['Term'].unique()))
#if term_filter != 'All':
#    df = df[df['Year'] == term_filter]
#if term_filter2 != 'All':
#    df = df[df['Term'] == term_filter2]

# Sidebar Filter
st.sidebar.header("Filters")
selected_years = st.sidebar.multiselect("Select Year", options=df['Year'].unique(), default=list(df['Year'].unique()))

if selected_years:
    df = df[df['Year'].isin(selected_years)]




# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Total Applications", df['Applications'].sum())
col2.metric("Total Admitted", df['Admitted'].sum())
col3.metric("Total Enrolled", df['Enrolled'].sum())

# Calculate the percentage admitted
total_admitted = df['Admitted'].sum()
total_applications = df['Applications'].sum()
if total_applications > 0:
  percent_admitted = (total_admitted / total_applications) * 100
else:
  percent_admitted = 0  

# Display the metric
st.metric("Percent Admitted", f"{percent_admitted:.2f}%")

# Calculate the percentage enrolled
total_admitted = df['Admitted'].sum()
total_enrolled = df['Enrolled'].sum()

if total_enrolled != 0:
  percent_enrolled = (total_enrolled / total_admitted) * 100
  st.metric("Percent Enrolled", f"{percent_enrolled:.2f}%")
else:
  st.metric("Percent Enrolled", "N/A")

# Chart
st.subheader("University Trends in Admissions")
st.line_chart(df, x="YearTerm", y=["Admitted", "Enrolled", "Applications"])

# Chart
st.subheader("Total Enrollment")
fig3 = px.bar(df, x="YearTerm", y="Enrolled",
labels={'value':'Enrolled','YearTerm': 'Year and Term'})
st.plotly_chart(fig3)

# Visualize Enrollment by Department
st.subheader("Student Enrollment by Department")
fig2 = px.line(df,x='YearTerm',y=['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled','Science Enrolled'],
               labels={'value':'Enrolled','YearTerm': 'Year and Term'})

st.plotly_chart(fig2)

# Line chart for Retention Rate and Student Satisfaction
st.subheader("Retention Rate and Student Satisfaction Over Time")

fig = px.line(df, x='YearTerm', y=['Retention Rate (%)', 'Student Satisfaction (%)'],
              labels={'value': 'Percent', 'YearTerm': 'Year and Term'})

st.plotly_chart(fig)





