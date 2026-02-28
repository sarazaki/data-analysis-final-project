from dash import Input, Output
from plots.user_plots import subscriber_vs_customer, gender_distribution, trips_by_age_group
from plots.time_plots import create_duration_histogram, trips_by_hour, duration_distribution
from plots.station_plots import top_start_stations
import plotly.graph_objects as go

# Color palette for consistency
COLORS = {
    'primary': '#00BCD4',
    'secondary': '#FF9800', 
    'accent': '#9C27B0',
    'light_blue': '#4FC3F7',
    'dark': '#37474F'
}

def register_callbacks(app, df):
    @app.callback(
        [
            Output("kpi_trips", "children"),
            Output("kpi_duration", "children"),
            Output("kpi_users", "children"),
            Output("kpi_station", "children"),
            Output("weekday_chart", "figure"),
            Output("duration_chart", "figure"),
            Output("subscriber_chart", "figure"),
            Output("gender_chart", "figure"),
            Output("station_chart", "figure"),
            Output("age_chart", "figure"),
        ],
        [
            Input("user_filter", "value"),
            Input("gender_filter", "value"),
            Input("age_filter", "value"),
        ]
    )
    def update_dashboard(user_type, gender, age_group):
        # تثبيت القيم الافتراضية لو حصل None
        if user_type is None:
            user_type = list(df["user_type"].unique())
        if gender is None:
            gender = list(df["member_gender"].dropna().unique())
        if age_group is None:
            age_group = list(df["age_group"].unique())
        
        # فلترة البيانات
        filtered = df[
            (df["user_type"].isin(user_type)) &
            (df["member_gender"].isin(gender)) &
            (df["age_group"].isin(age_group))
        ]
        
        # لو مفيش بيانات
        if filtered.empty:
            empty_fig = go.Figure()
            empty_fig.update_layout(template="plotly_white")
            return (
                "0",
                "0",
                "0",
                empty_fig,
                empty_fig,
                empty_fig,
                empty_fig,
                empty_fig,
                empty_fig,
            )
        
        total_trips = f"{len(filtered):,}"
        avg_duration = f"{filtered['duration_min'].mean():.1f}"
        active_users = f"{filtered['bike_id'].nunique():,}"
        top_station = filtered["start_station_name"].value_counts().idxmax()
        
        # إعداد بيانات الساعات
        hour_data = filtered.groupby('hour').size().reset_index(name='trips')
        
        return (
            total_trips,
            avg_duration,
            active_users,
            top_station,
            trips_by_hour(hour_data),
            duration_distribution(filtered),
            subscriber_vs_customer(filtered),
            gender_distribution(filtered),
            top_start_stations(filtered, colors=COLORS),
            trips_by_age_group(filtered),
        )