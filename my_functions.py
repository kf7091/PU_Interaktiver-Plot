import pandas as pd
import numpy as np


def read_activity_data(hr_max):
    #load data
    activity_data = pd.read_csv('activity.csv', usecols=["Duration", "PowerOriginal", "HeartRate"])

    #convert duration to absolute time
    activity_data["Duration"] = range(len(activity_data))
    #for i in range(1, len(activity_data)):
    #    activity_data["Duration"][i] = activity_data["Duration"][i] + activity_data["Duration"][i-1]

    # add new collum "zones" with information on zone
        # assume maximal heart rate
    for index, observation in activity_data.iterrows():
        zone = "keine Angabe"
        color = "lightgray"
        if observation["HeartRate"] < 0.6 * hr_max and observation["HeartRate"] >= 0.5 * hr_max:
            zone = "sehr leicht"
            color = "lightgreen"
        elif observation["HeartRate"] < 0.7 * hr_max and observation["HeartRate"] >= 0.6 * hr_max:
            zone = "leicht"
            color = "green"
        elif observation["HeartRate"] < 0.8 * hr_max and observation["HeartRate"] >= 0.7 * hr_max:
            zone = "moderat"
            color = "yellow"
        elif observation["HeartRate"] < 0.9 * hr_max and observation["HeartRate"] >= 0.8 * hr_max:
            zone = "hart"
            color = "red"
        elif observation["HeartRate"] < hr_max and observation["HeartRate"] >= 0.9 * hr_max:
            zone = "sehr hart"
            color = "darkred"
        activity_data.at[index, 'Zone'] = zone
        activity_data.at[index, 'Color'] = color

    return activity_data


if __name__ == "__main__":
    activity_data = read_activity_data()
    print(type(activity_data))
    print(activity_data.head())
    print(activity_data.tail())
    print(activity_data["PowerOriginal"].mean())
    print(activity_data["PowerOriginal"].max())
    print(activity_data["Duration"].head())
    print(activity_data["Duration"].tail())
    print(activity_data["Zone"].head())
    print(activity_data["Zone"].tail())
    print(activity_data.describe())
    print(activity_data.info())
    print(activity_data.isnull().sum())
    print(activity_data.dtypes)
    print(activity_data["Zone"].value_counts())
    print(activity_data["Zone"].unique())
    print(activity_data["Zone"].nunique())
    print(activity_data["Zone"].mode())