import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

px.defaults.template = "plotly_white"

# Color palette
COLORS = {
    'primary': '#00BCD4',
    'secondary': '#FF9800', 
    'accent': '#9C27B0',
    'light_blue': '#4FC3F7',
    'dark': '#37474F'
}

def trips_by_hour(hour_data):
    """
    Create a Plotly figure showing number of trips by hour.
    """
    hours = hour_data["hour"]
    trips_hour = hour_data["trips"]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hours,
        y=trips_hour,
        mode="lines+markers",
        line=dict(width=3, color=COLORS["accent"]),
        marker=dict(size=6),
        hovertemplate="Hour: %{x}<br>Trips: %{y}<extra></extra>"
    ))
    
    fig.update_layout(
        title=dict(
            text="Trips by Hour of Day",
            font=dict(size=18, color=COLORS['dark'])
        ),
        template="plotly_white",
        height=350,
        font=dict(family="Segoe UI, Arial", size=12),
        xaxis=dict(
            title="Hour of Day",
            title_font=dict(size=16),
            dtick=1,
            showgrid=False,
            linecolor="lightgray"
        ),
        yaxis=dict(
            title="Number of Trips",
            title_font=dict(size=16),
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)",
            linecolor="lightgray"
        ),
        margin=dict(l=50, r=30, t=50, b=40)
    )
    return fig

def duration_distribution(df):
    """
    Plot distribution of trip duration in minutes.
    """
    x_col = "duration_min"
    bins = 50
    title = "Trip Duration Distribution (Minutes)"
    height = 400
    
    fig = px.histogram(
        df,
        x=x_col,
        nbins=bins,
        title=title,
        color_discrete_sequence=[COLORS['primary']]
    )
    fig.update_traces(
    marker_line_width=1.5,
    marker_line_color="white"
    )
    
    fig.update_layout(
        template="plotly_white",
        height=height,
        font=dict(family="Segoe UI, Arial", size=11),
        title=dict(font=dict(size=18, color=COLORS['dark'])),  # Consistent title size
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis=dict(
            title="Duration (Minutes)",
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)"
        ),
        yaxis=dict(
            title="Number of Trips",
            showgrid=True,
            gridcolor="rgba(0,0,0,0.05)"
        ),
        margin=dict(l=50, r=30, t=50, b=40)  # Consistent margins
    )
    return fig

def create_duration_histogram(df, color=None):  # Added color parameter with default
    """
    Create a histogram for trip duration.
    """
    if color is None:
        color = COLORS['primary']  # Use default color from palette
        
    fig = px.histogram(
        df,
        x="duration_min",
        nbins=50,
        title="Trips by Minutes",
        color_discrete_sequence=[color]
    )
    
    fig.update_traces(
        marker_line_width=1.5,
        marker_line_color="white"
    )
    
    fig.update_layout(
        template="plotly_white",
        height=350,  # Consistent height
        font=dict(family="Segoe UI, Arial", size=12),
        title=dict(font=dict(size=18, color=COLORS['dark'])),  # Consistent title
        xaxis_title="Duration (Minutes)",
        yaxis_title="Number of Trips",
        margin=dict(l=50, r=30, t=50, b=40)  # Consistent margins
    )
    return fig