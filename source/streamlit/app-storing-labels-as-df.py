import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_plotly_events import plotly_events

# Sample data
df = pd.DataFrame({
    'timestamp': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'value': range(100)
})

# Create a Plotly figure
fig = px.scatter(df, x='timestamp', y='value',)
fig.update_layout(dragmode='select', 
                #   template='plotly_dark'
                  )  # Enable box select

# Capture selected points
selected_points = plotly_events(fig, select_event=True)

# Initialize or retrieve the labels DataFrame
if 'labels_df' not in st.session_state:
    st.session_state['labels_df'] = pd.DataFrame(columns=['start', 'end', 'type'])

# Function to save labels
def save_label(label_type):
    if selected_points:
        timestamps = [df.iloc[point['pointIndex']]['timestamp'] for point in selected_points]
        if timestamps:
            new_row = pd.DataFrame({'start': [min(timestamps)], 'end': [max(timestamps)], 'type': [label_type]})
            st.session_state['labels_df'] = pd.concat([st.session_state['labels_df'], new_row], ignore_index=True)

# Layout for buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button('Save as cc_1'):
        save_label('cc_1')
with col2:
    if st.button('Save as cc_2'):
        save_label('cc_2')
with col3:
    if st.button('Save as cc_3'):
        save_label('cc_3')

# Display the labels DataFrame
st.write("Saved Labels:")

with st.expander("Show Labels"):
    st.dataframe(st.session_state['labels_df'])

# Main area display (optional)
st.write("Select points on the graph and click a 'Save as' button to store the critical condition.")
