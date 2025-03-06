import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('university_student_dashboard_data.csv')

# Title of the app
st.title("University Admission Data")

# Filter Data
filtered_df = df[df.Year == Year]

# Filter Data
filtered_df2 = df[df.Term == Term]

# Convert 'Year' and 'Term' columns to string 
df['Year'] = df['Year'].astype(str)
df['Term'] = df['Term'].astype(str)

# Create the new column 'YearTerm'
df['YearTerm'] = df['Year'] + ' ' + df['Term']

term_data = df.groupby('YearTerm').agg(
    {'Applications': 'sum', 'Admitted': 'sum', 'Enrolled': 'sum'}
).reset_index()

retention_satisfaction = df.groupby('YearTerm').agg(
    {'Retention Rate (%)': 'mean', 'Student Satisfaction (%)': 'mean'}
).reset_index()

enrollment_by_department = df.groupby('YearTerm').agg(
    {'Engineering Enrolled': 'sum', 'Business Enrolled': 'sum', 'Arts Enrolled': 'sum', 'Science Enrolled': 'sum'}
).reset_index()

#create plots

fig1 =
plt.figure(figsize=(12, 6))
plt.plot(term_data['YearTerm'], term_data['Applications'], label='Applications', marker='o')
plt.plot(term_data['YearTerm'], term_data['Admitted'], label='Admitted', marker='s')
plt.plot(term_data['YearTerm'], term_data['Enrolled'], label='Enrolled', marker='^')

fig2 =
plt.figure(figsize=(12, 6))
plt.plot(retention_satisfaction['YearTerm'], retention_satisfaction['Retention Rate (%)'], label='Retention Rate (%)', marker='o')
plt.plot(retention_satisfaction['YearTerm'], retention_satisfaction['Student Satisfaction (%)'], label='Student Satisfaction (%)', marker='s')


fig3 = 
# Create the stacked bar chart
plt.figure(figsize=(12, 6))

# Define the width of the bars
bar_width = 0.8

# Plot each department's enrollment as a separate bar segment
bottom = np.zeros(len(enrollment_by_department))  # Initialize the bottom position for each bar
for department in ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']:
  plt.bar(enrollment_by_department['YearTerm'], enrollment_by_department[department], bottom=bottom, label=department, width=bar_width)
  bottom += enrollment_by_department[department]



# Arrange the plots in a grid layout
col1, col2 = st.columns(2)  # Create 2 columns
with col1:
    st.plotly_chart(fig1, use_container_width=True)  # First plot in first column
with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Second plot in second column

# Add the third plot in a full-width row below
st.plotly_chart(fig3, use_container_width=True)


# Display the Plotly chart in Streamlit
st.plotly_chart(fig)
