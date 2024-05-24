import plotly.express as px
import plotly.graph_objects as go
from my_functions import read_activity_data
import streamlit as st

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Session State wird angelegt und Visibility und Disabled auf False gesetzt
if "visibility" not in st.session_state: 
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

# Session State wird angelegt und hr_max auf 200 gesetzt
if "hr_max" not in st.session_state: 
    st.session_state.hr_max = 200 
    # Ein default Wert damit die Funktion etwas berechnen kann und keinen Fehler anzeigt

st.write('# Leistung und HF in Zonen') # Überschrift

col1, col2 = st.columns(2) # Columns Erstellen
with col1: # Erstes Column für die max_hr
    hr_max = st.text_input(
        "Enter max heart rate:",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
    if hr_max: # Wenn hr_max eingegeben wurde, wird der Wert in den Session State geschrieben
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
fig_hr.update_layout(title='Heartrate Zones', # Layout für die Grafik
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

st.plotly_chart(fig_hr) # plotly Chart in Streamlit einfügen
st.plotly_chart(fig_power)

# Durschnitt und Max Leistung
st.write('Die Durchschnitt Leistung beträgt: {:.2f} [W]'.format(activity_data["PowerOriginal"].mean()))
st.write('Die Maximal Leistung beträgt:  {:.2f} [W]'.format(activity_data["PowerOriginal"].max()))

# Tabelle mit den Zonen und Zeit per Zonen erstellen
zeit_in_zone = activity_data["Zone"].value_counts()
# Beschriftung Spalte in Sekunden
zeit_in_zone = zeit_in_zone.rename_axis('Zone').reset_index(name='Time [s]')

# Überschrift für die Tabelle
st.write('#### Zeit / Durchschnittsleistung in Zonen :')

# Tabelle für Durschnittsleistung in Zonen erstellen
power_zone = activity_data.groupby("Zone")["PowerOriginal"].mean().reset_index()
power_zone = power_zone.rename(columns={"PowerOriginal": "Meanpower [W]"})

# Tabelle Zeit und Durchschnittsleistung in Zonen zusammenführen
table = zeit_in_zone.merge(power_zone, on="Zone")

# Tabelle in Streamlit als HTML einfügen und die INDEX-Spalte verstecken
st.markdown(table.style.hide(axis="index").to_html(), unsafe_allow_html=True)

