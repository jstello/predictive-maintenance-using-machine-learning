import streamlit as st
import plotly.express as px
from streamlit_plotly_events import plotly_events
import pandas as pd


# Sample data
df = pd.DataFrame({
    'timestamp': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'value': range(100)
})

# Sidebar dropdown for critical condition types
cc_types = ['cc_1', 'cc_2', 'cc_3']
selected_cc = st.sidebar.selectbox('Select Critical Condition Type', cc_types)

# Create a Plotly figure
fig = px.scatter(df, x='timestamp', y='value')  # Adjust x and y according to your DataFrame
fig.update_layout(dragmode='select')  # 'lasso' for lasso selection

# Capture selected points
selected_points = plotly_events(fig, select_event=True)

# Structure to store labels
if 'labels' not in st.session_state:
    st.session_state['labels'] = []

# Button to save the label
if st.button('Save Label'):
    if selected_points:
        timestamps = [df.iloc[point['pointIndex']]['timestamp'] for point in selected_points]
        timestamp_range = (min(timestamps), max(timestamps))
        st.session_state['labels'].append({'range': timestamp_range, 'type': selected_cc})
        st.sidebar.write("Labels Saved:", st.session_state['labels'])
    else:
        st.sidebar.write("No points selected")

# Main area display (optional)
st.write("Select points on the graph and click 'Save Label' to store the critical condition.")
