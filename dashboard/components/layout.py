from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd # لازم تضيفي ده فوق عشان الـ dropna تشتغل

def create_layout(df):
    # تنسيق السايدبار
    SIDEBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "16rem",
        "padding": "1.5rem",
        "background-color": "#ffffff",
        "border-right": "1px solid #e0e0e0",
        "overflow-y": "auto",
        "box-shadow": "2px 0 8px rgba(0,0,0,0.05)"
    }


    # تنسيق المحتوى
    CONTENT_STYLE = {
        "margin-left": "18rem",
        "margin-right": "2rem",
        "padding": "2rem",
        "background-color": "#f5f7fa",
        "min-height": "100vh"
    }

    # تجهيز قيم الـ Age Group عشان نضمن إنها مش فاضية
    # بنشيل الـ NaN وبنرتبهم
    # ترتيب ثابت
    age_order = ["Younger", "Adult", "Senior"]
    gender_order = ["Male", "Female", "Other"]

    return html.Div([
        # --- Sidebar ---
                html.Div([
            html.H4("Filters", className="mb-4 text-dark", style={"fontWeight": "600"}),
            
            # User Type (Checkboxes)
            html.Div([
                html.H6("User Type", className="fw-bold text-secondary mb-2", 
                        style={"fontSize": "20px", "textTransform": "uppercase", "letterSpacing": "0.5px"}),
                dbc.Checklist(
                    id="user_filter",
                    options=[{"label": html.Span(i, style={"marginLeft": "8px", "fontSize": "18px"}), "value": i} 
                            for i in df["user_type"].unique()],
                    value=list(df["user_type"].unique()),
                    inline=False,
                    className="mb-3",
                    labelStyle={"display": "block", "marginBottom": "8px", "cursor": "pointer"}
                ),
            ], className="mb-4"),

            # Gender (Checkboxes)
            html.Div([
                html.H6("Gender", className="fw-bold text-secondary mb-2",
                        style={"fontSize": "20px", "textTransform": "uppercase", "letterSpacing": "0.5px"}),
                dbc.Checklist(
                    id="gender_filter",
                    options=[{"label": html.Span(i, style={"marginLeft": "8px", "fontSize": "18px"}), "value": i} 
                        for i in gender_order if i in df["member_gender"].dropna().unique()],
                    value=[i for i in gender_order if i in df["member_gender"].dropna().unique()],
                    inline=False,
                    className="mb-3",
                    labelStyle={"display": "block", "marginBottom": "8px", "cursor": "pointer"}
                ),
            ], className="mb-4"),

            # Age Group (Checkboxes)
            html.Div([
                html.H6("Age Group", className="fw-bold text-secondary mb-2",
                        style={"fontSize": "20px", "textTransform": "uppercase", "letterSpacing": "0.5px"}),
                dbc.Checklist(
                    id="age_filter",
                    options=[{"label": html.Span(i, style={"marginLeft": "8px", "fontSize": "18px"}), "value": i} 
                            for i in age_order if i in df["age_group"].unique()],
                    value=[i for i in age_order if i in df["age_group"].unique()],
                    inline=False,
                    className="mb-3",
                    labelStyle={"display": "block", "marginBottom": "8px", "cursor": "pointer"}
                ),
            ], className="mb-4"), ], style=SIDEBAR_STYLE),
                
        # --- Main Content ---
        html.Div([
    # Header
    dbc.Row([
        dbc.Col(html.H1(
            "Ford GoBike Performance Dashboard",
            className="text-center text-primary mb-5"
        ))
    ]),

    # KPIs Section
    dbc.Row([
        # KPI 1: Trips
        dbc.Col(
                html.Div([
                html.P("🚲Total Trips", className="text-muted", style={"fontSize": "20px"}),
                html.H3(id="kpi_trips", className="text-primary mb-2", 
                        style={"fontSize": "25px", "fontWeight": "700"}),
            ], className="text-center p-1", 
                style={"background": "white", "borderRadius": "12px", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)", "height": "100%"})
        , width=3),
        
        # KPI 2: Avg Duration
        dbc.Col(
            html.Div([ 
                html.P("🕓Avg duration (Min)", className="text-muted", style={"fontSize": "20px"}),
                html.H3(id="kpi_duration", className="text-primary mb-5",
                        style={"fontSize": "25px", "fontWeight": "700"}),
            ], className="text-center p-1",
                style={"background": "white", "borderRadius": "12px", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)", "height": "100%"})
        , width=3),
        
        # KPI 3: Active Users
        dbc.Col(
            html.Div([
                html.P("👤Active users", className="text-muted", style={"fontSize": "20px"}),
                html.H3(id="kpi_users", className="text-primary mb-2",
                        style={"fontSize": "25px", "fontWeight": "700"}),
                
            ], className="text-center p-1",
                style={"background": "white", "borderRadius": "12px", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)", "height": "100%"})
        , width=3),
        
        # KPI 4: Most Popular Station
        dbc.Col(
            html.Div(
                [html.P("📍Most popular station", className="text-muted", style={"fontSize": "20px"}),
                html.H3(id="kpi_station", className="text-primary mb-2",
                        style={"fontSize": "25px", "fontWeight": "700"}),
                
            ], className="text-center p-1",
                style={"background": "white", "borderRadius": "12px", "boxShadow": "0 2px 8px rgba(0,0,0,0.08)", "height": "100%"})
        , width=3),
    ], className="mb-4", justify="center"),
]),
            # Graphs Section 1
            dbc.Row([
                dbc.Col(dcc.Graph(id="weekday_chart"), width=6),
                dbc.Col(dcc.Graph(id="duration_chart"), width=6),
            ], className="mb-4"),

            # Graphs Section 2
            dbc.Row([
                dbc.Col(dcc.Graph(id="subscriber_chart"), width=6),
                dbc.Col(dcc.Graph(id="gender_chart"), width=6),
            ], className="mb-4"),

            # Graphs Section 3
            dbc.Row([
                dbc.Col(dcc.Graph(id="age_chart"), width=6),
                dbc.Col(dcc.Graph(id="station_chart"), width=6),
            ], className="mb-4"),

        ], style=CONTENT_STYLE)