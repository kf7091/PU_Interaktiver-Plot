import plotly.express as px
import plotly.graph_objects as go
from my_functions import read_activity_data
import streamlit as st

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if "hr_max" not in st.session_state:
    st.session_state.hr_max = 200

st.write('# Leistung und HF in Zonen') # Überschrift

col1, col2 = st.columns(2)
with col1:
    hr_max = st.text_input(
        "Enter max heart rate:",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
    if hr_max:
        st.write("You entered: ", hr_max, "bpm")
        st.session_state.hr_max = float(hr_max)

activity_data = read_activity_data(st.session_state.hr_max)

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


