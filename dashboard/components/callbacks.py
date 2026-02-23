from dash import Input, Output
from plots.user_plots import subscriber_vs_customer, gender_distribution
from plots.time_plots import trips_by_weekday, duration_distribution
from plots.station_plots import top_start_stations


def register_callbacks(app, df):

    @app.callback(
        [
            Output("kpi_trips", "children"),
            Output("kpi_duration", "children"),
            Output("kpi_users", "children"),
            Output("weekday_chart", "figure"),
            Output("duration_chart", "figure"),
            Output("subscriber_chart", "figure"),
            Output("gender_chart", "figure"),
            Output("station_chart", "figure"),
        ],
        [
            Input("user_filter", "value"),
            Input("gender_filter", "value"),
            Input("age_filter", "value"),
        ]
    )
    def update_dashboard(user_type, gender, age_group):

        filtered = df[
            (df["user_type"].isin(user_type)) &
            (df["member_gender"].isin(gender)) &
            (df["age_group"].isin(age_group))
        ]

        total_trips = f"{len(filtered):,}"
        avg_duration = f"{filtered['duration_min'].mean():.1f}"
        active_users = f"{filtered['bike_id'].nunique():,}"

        return (
            total_trips,
            avg_duration,
            active_users,
            trips_by_weekday(filtered),
            duration_distribution(filtered),
            subscriber_vs_customer(filtered),
            gender_distribution(filtered),
            top_start_stations(filtered)
        )
