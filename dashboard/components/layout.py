from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(df):

    return dbc.Container([

    # Main Header
    # العنوان الرئيسي للوحة البيانات
        dbc.Row([
            dbc.Col(html.H1(
                "Ford GoBike Performance Dashboard",
                className="text-center text-primary my-4"
            ))
        ]),

        # FILTERS
        dbc.Row([
            dbc.Col([
                html.Label("User Type"),
                dcc.Dropdown(
                    id="user_filter",
                    options=[{"label": i, "value": i} for i in df["user_type"].unique()],
                    value=df["user_type"].unique(),
                    multi=True
                )
            ], width=4),

            dbc.Col([
                html.Label("Gender"),
                dcc.Dropdown(
                    id="gender_filter",
                    options=[{"label": i, "value": i} for i in df["member_gender"].dropna().unique()],
                    value=df["member_gender"].dropna().unique(),
                    multi=True
                )
            ], width=4),

            dbc.Col([
                html.Label("Age Group"),
                dcc.Dropdown(
                    id="age_filter",
                    options=[{"label": i, "value": i} for i in df["age_group"].unique()],
                    value=df["age_group"].unique(),
                    multi=True
                )
            ], width=4),
        ], className="mb-4"),

    # KPI Section: Quick Stats Cards
    # قسم مؤشرات الأداء: كروت تعرض أرقام ملخصة سريعة
    
        dbc.Row([
            dbc.Col(dbc.Card(dbc.CardBody([
                html.H6("Total Trips"),
                html.H3(id="kpi_trips")
            ])), width=4),

            dbc.Col(dbc.Card(dbc.CardBody([
                html.H6("Average Duration (Min)"),
                html.H3(id="kpi_duration")
            ])), width=4),

            dbc.Col(dbc.Card(dbc.CardBody([
                html.H6("Active Users"),
                html.H3(id="kpi_users")
            ])), width=4),
        ], className="mb-4"),

        # TIME SECTION
        dbc.Row([
            dbc.Col(dcc.Graph(id="weekday_chart"), width=6),
            dbc.Col(dcc.Graph(id="duration_chart"), width=6),
        ], className="mb-4"),

        # USER SECTION
        dbc.Row([
            dbc.Col(dcc.Graph(id="subscriber_chart"), width=6),
            dbc.Col(dcc.Graph(id="gender_chart"), width=6),
        ], className="mb-4"),

        # STATION SECTION
        dbc.Row([
            dbc.Col(dcc.Graph(id="station_chart"), width=12),
        ]),

    ], fluid=True)
