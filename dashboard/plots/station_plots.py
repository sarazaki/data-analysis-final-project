import plotly.graph_objects as go
import plotly.express as px

px.defaults.template = "plotly_white"

# Color palette
COLORS = {
    'primary': '#00BCD4',
    'secondary': '#FF9800', 
    'accent': '#9C27B0',
    'light_blue': '#4FC3F7',
    'dark': '#37474F'
}

def top_start_stations(df, station_col='start_station_name', top_n=10, 
                       highlight_top=3, title='Top Stations', colors=None, height=350):
    """
    Plot top N stations by number of trips (horizontal bar chart).
    """
    if colors is None:
        colors = COLORS  # Use default colors if not provided
        
    top_stations = (
        df[station_col]
        .value_counts()
        .head(top_n)
        .sort_values(ascending=False)
    )
    
    stations = top_stations.index
    counts = top_stations.values
    highlight_values = top_stations.head(highlight_top).values
    
    bar_colors = [
        colors['primary'] if value in highlight_values
        else colors['light_blue']
        for value in counts
    ]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=stations,
        x=counts,
        orientation='h',
        marker=dict(
            color=bar_colors,
            line=dict(width=1, color='white')
        ),
        text=[f'{c:,}' for c in counts],
        textposition='inside',
        textfont=dict(size=10, color=colors['dark'])
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=18, color=colors['dark'])),  # Consistent size
        template='plotly_white',
        height=height,
        font=dict(family="Segoe UI, Arial", size=12),  # Consistent font
        paper_bgcolor='white',
        plot_bgcolor='white',
        xaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.05)',
            linecolor='lightgray',
            title='Number of Trips'
        ),
        yaxis=dict(
            showgrid=False,
            linecolor='lightgray',
            autorange="reversed"
        ),
        margin=dict(l=120, r=30, t=50, b=40),  # Consistent margins
        bargap=0.2
    )
    return fig