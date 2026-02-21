import plotly.express as px

def top_start_stations(df):
    data = df["start_station_name"].value_counts().head(10).reset_index()
    data.columns = ["station", "count"]

    fig = px.bar(
        data,
        x="count",
        y="station",
        orientation="h",
        title="Top 10 Start Stations"
    )
    fig.update_layout(template="plotly_white")
    return fig
