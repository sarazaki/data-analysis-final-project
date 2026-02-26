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

def subscriber_vs_customer(df):
    """
    Create a donut chart for user type distribution.
    """
    user_counts = df['user_type'].value_counts()
    total = user_counts.sum()
    max_label = user_counts.idxmax()
    max_percent = (user_counts.max() / total) * 100

    fig = go.Figure(data=[go.Pie(
        labels=user_counts.index,
        values=user_counts.values,
        hole=0.65,
        marker=dict(
            colors=[COLORS['primary'], COLORS['secondary']],
            line=dict(width=2, color='white')
        ),
        textinfo='none',
        hoverinfo='label+percent'
    )])

    fig.update_layout(
        title=dict(
            text='Subscriber vs Customer Usage',
            font=dict(size=18, color=COLORS['dark'])  # Consistent size
        ),
        template='plotly_white',
        height=350,  # Consistent height
        font=dict(family="Segoe UI, Arial", size=12),
        paper_bgcolor='white',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.15,
            x=0.5,
            xanchor="center"
        ),
        margin=dict(l=40, r=40, t=50, b=60),
        annotations=[
            dict(
                text=f"{max_percent:.1f}%",
                x=0.5,
                y=0.5,
                font_size=24,  # Slightly smaller
                showarrow=False,
                font_family="Segoe UI"
            ),
            dict(
                text=max_label,
                x=0.5,
                y=0.35,
                font_size=12,
                showarrow=False,
                font_color='gray'
            )
        ]
    )
    return fig

def gender_distribution(df):
    """
    Create a bar chart for trips by gender.
    """
    gender_counts = df['member_gender'].value_counts()
    gender_percent = (gender_counts / gender_counts.sum()) * 100

    order = ['Male', 'Female', 'Other']
    gender_counts = gender_counts.reindex(order).fillna(0)
    gender_percent = gender_percent.reindex(order).fillna(0)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=gender_counts.index,
        y=gender_counts.values,
        marker=dict(
            color=[COLORS['primary'], COLORS['secondary'], COLORS['accent']],
            line=dict(width=1, color='white')
        ),
        text=[f"{p:.1f}%" for p in gender_percent.values],
        textposition='outside',
        textfont=dict(size=11, color=COLORS['dark'])
    ))

    fig.update_layout(
        title=dict(
            text='Trips By Gender',
            font=dict(size=18, color=COLORS['dark'])  # Consistent size
        ),
        template='plotly_white',
        height=350,  # Consistent height
        font=dict(family="Segoe UI, Arial", size=12),
        paper_bgcolor='white',
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, linecolor='lightgray'),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.05)', linecolor='lightgray'),
        margin=dict(l=50, r=30, t=50, b=40),  # Consistent margins
        bargap=0.3
    )
    return fig

def trips_by_age_group(df, age_col='age_group', title='Trips by Age Group'):
    """
    Plots number of trips by age group using a bar chart.
    """
    age_data = (
        df[age_col]
        .value_counts()
        .sort_index()
        .reset_index()
    )
    age_data.columns = ['age_group', 'trips']

    fig = px.bar(
        age_data,
        x='age_group',
        y='trips',
        title=title,
        color='age_group',
        color_discrete_sequence=[COLORS['primary'], COLORS['secondary'], COLORS['accent']]
    )

    fig.update_layout(
        template='plotly_white',
        height=350,  # Consistent height
        font=dict(family="Segoe UI, Arial", size=12),
        title=dict(font=dict(size=18, color=COLORS['dark'])),  # Consistent title
        xaxis_title='Age Group',
        yaxis_title='Number of Trips',
        margin=dict(l=50, r=30, t=50, b=40),  # Consistent margins
        showlegend=False  # Hide legend since colors are self-explanatory
    )
    return fig