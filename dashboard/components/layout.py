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
        "width": "18rem",
        "padding": "2rem 1rem",
        "background-color": "#f8f9fa",
        "border-right": "1px solid #dee2e6",
        "overflow-y": "auto" # عشان لو الفلاتر كتير تقدر تسكرول
    }

    # تنسيق المحتوى
    CONTENT_STYLE = {
        "margin-left": "20rem",
        "margin-right": "2rem",
        "padding": "2rem 1rem",
    }

    # تجهيز قيم الـ Age Group عشان نضمن إنها مش فاضية
    # بنشيل الـ NaN وبنرتبهم
    age_options = sorted([i for i in df["age_group"].unique() if pd.notna(i)])

    return html.Div([
        # --- Sidebar ---
        html.Div([
            html.H2("Filters", className="display-6 text-primary"),
            html.Hr(),
            
            # فلتر User Type
            html.Div([
                html.Label("User Type", className="fw-bold"),
                dcc.Dropdown(
                    id="user_filter",
                    options=[{"label": i, "value": i} for i in df["user_type"].unique()],
                    value=list(df["user_type"].unique()),
                    multi=True,
                    className="mb-3"
                ),
            ]),

            # فلتر Gender
            html.Div([
                html.Label("Gender", className="fw-bold"),
                dcc.Dropdown(
                    id="gender_filter",
                    options=[{"label": i, "value": i} for i in df["member_gender"].dropna().unique()],
                    value=list(df["member_gender"].dropna().unique()),
                    multi=True,
                    className="mb-3"
                ),
            ]),

            # فلتر Age Group (التعديل هنا)
            html.Div([
                html.Label("Age Group", className="fw-bold"),
                dcc.Dropdown(
                    id="age_filter",
                    options=[{"label": i, "value": i} for i in age_options],
                    value=age_options, # كدا هيختارهم كلهم أوتوماتيك أول ما يفتح
                    multi=True,
                    className="mb-3"
                ),
            ]),
        ], style=SIDEBAR_STYLE),

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
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H6("Total Trips", className="text-muted"),
                    html.H3(id="kpi_trips", className="text-primary")
                ])), width=4),
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H6("Average Duration (Min)", className="text-muted"),
                    html.H3(id="kpi_duration", className="text-primary")
                ])), width=4),
                dbc.Col(dbc.Card(dbc.CardBody([
                    html.H6("Active Users", className="text-muted"),
                    html.H3(id="kpi_users", className="text-primary")
                ])), width=4),
            ], className="mb-4"),

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
    ])