import pandas as pd
import numpy as np
import plotly.express as px
from my_functions import read_activity_data


activity_data = read_activity_data()

zone_colors = {
    "keine Angabe": "weiß",
    "sehr leicht": "grün",
    "leicht": "gelb",
    "moderat": "orange",
    "hart": "rot",
    "sehr hart": "schwarz"
}

