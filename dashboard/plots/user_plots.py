import plotly.express as px

def subscriber_vs_customer(df):
    fig = px.pie(
        df,
        names="user_type",
        hole=0.4,
        title="Subscriber vs Customer Usage"
    )
    fig.update_layout(template="plotly_white")
    return fig


def gender_distribution(df):
    data = df["member_gender"].value_counts().reset_index()
    data.columns = ["gender", "count"]

    fig = px.bar(
        data,
        x="gender",
        y="count",
        title="Trips by Gender"
    )
    fig.update_layout(template="plotly_white")
    return fig
