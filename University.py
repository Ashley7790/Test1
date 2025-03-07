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
st.sidebar.header("Filters")
term_filter = st.sidebar.selectbox("Select Year", ['All'] + list(df['Year'].unique()))
if term_filter != 'All':
    df = df[df['Year'] == term_filter]

# KPIs
st.metric("Total Applications", df['Applications'].sum())
st.metric("Total Admitted", df['Admitted'].sum())
st.metric("Total Enrolled", df['Enrolled'].sum())

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





