import plotly.express as px
import plotly.graph_objects as go
from my_functions import read_activity_data


activity_data = read_activity_data()

fig_hr = go.Figure(
    data=go.Scatter(
        x=activity_data["Duration"],
        y=activity_data["HeartRate"],
        marker = {"color" : activity_data["Color"]},
        line = {"color" : "lightgray"},
        mode='lines+markers'
    )
)
fig_hr.show()

fig_power = go.Figure(
    data=go.Scatter(
        x=activity_data["Duration"],
        y=activity_data["PowerOriginal"],
        marker = {"color" : activity_data["Color"]},
        line = {"color" : "lightgray"},
        mode='lines+markers'
    )
)
fig_power.show()

