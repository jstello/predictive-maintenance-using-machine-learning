import streamlit as st
import plotly.express as px
import pandas as pd

from streamlit_plotly_events import plotly_events

# Sample data
df = pd.DataFrame({
    'time': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'value': range(100)
})


# Create a Plotly figure
fig = px.scatter(df, x='time', y='value')

# Enable selection tools in the figure's layout
fig.update_layout(dragmode='select')  # 'select' for box select, 'lasso' for lasso select

# Use plotly_events to display the figure and capture events
selected_points = plotly_events(fig, select_event=True)

# Display the selected points
# st.write("Selected Points:", selected_points)

# Process the selected points as needed
# For example, extract the time range or specific data points

if selected_points:
    timestamps = [point['x'] for point in selected_points]
    start_time = min(timestamps)
    end_time = max(timestamps)
    st.write(f"Selected time range: {start_time} to {end_time}")
