import plotly.express as px
import plotly.graph_objects as go
from my_functions import read_activity_data
import streamlit as st

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'



activity_data = read_activity_data()

fig_hr = go.Figure(
    data=go.Scatter(
        x=activity_data["Duration"],
        y=activity_data["HeartRate"],
        marker = {"color" : activity_data["Color"]},
        line = {"color" : "lightgray"},
        mode='lines+markers',
        name = 'HeartRate'
    )
)
fig_hr.update_layout(title='Heartrate Zones',
                   xaxis_title='Time [s]',
                   yaxis_title='Heart Rate [bpm]',
                   showlegend=False,
                   legend_title="Zone colours:",)

# fig_hr.show()

fig_power = go.Figure(
    data=go.Scatter(
        x=activity_data["Duration"],
        y=activity_data["PowerOriginal"],
        marker = {"color" : activity_data["Color"]},
        line = {"color" : "lightgray"},
        mode='lines+markers',
        name = 'Power',
    )
)

fig_power.update_layout(title='Power and Heartrate Zones',
                   xaxis_title='Time [s]',
                   yaxis_title='Power [W]',
                   showlegend=False,
                   legend_title="Zone colours:",                                
                   )

# fig_power.show()

st.plotly_chart(fig_hr)
st.plotly_chart(fig_power)


