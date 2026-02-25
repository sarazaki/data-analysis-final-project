import pandas as pd
import plotly.express as px

def trips_by_weekday(df):

    df = df.copy()

    df["start_time"] = pd.to_datetime(
        df["start_time"],
        errors="coerce"
    )

    df = df.dropna(subset=["start_time"])

    df["weekday"] = df["start_time"].dt.day_name()

    data = df.groupby("weekday").size().reset_index(name="trips")

    fig = px.bar(
        data,
        x="weekday",
        y="trips",
        title="Trips by Weekday"
    )

    fig.update_layout(template="plotly_white")

    return fig


def duration_distribution(df):
    fig = px.histogram(
        df,
        x="duration_min",
        nbins=50,
        title="Trip Duration Distribution (Minutes)"
    )
    fig.update_layout(template="plotly_white")
    return fig
