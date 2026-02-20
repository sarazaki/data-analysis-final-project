import pandas as pd 
import plotly.express as px 
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

"""
Project: Comprehensive Ford GoBike Analysis Dashboard
Description: A professional, multi-chart dashboard using Dash, Plotly, and Bootstrap.
المشروع: لوحة بيانات شاملة لتحليل Ford GoBike
الوصف: داشبورد احترافية متعددة الرسومات باستخدام Dash و Plotly و Bootstrap.
"""

# 1. Load and prepare data
# تحميل وتجهيز البيانات
df = pd.read_csv(r'C:\Users\zbookg6\data_analysi\data-analysis-final-project\data\processed\fordgobike-tripdataFor201902_cleaned.csv')

# Mapping for weekends to make labels clearer
# تحويل قيم الويك إيند لأسماء واضحة في الرسم
df['day_type'] = df['weekend_flag'].map({0: 'Weekday', 1: 'Weekend'})

# 2. Initialize the App with a professional theme (LUX)
# LUX provides a high-end, clean aesthetic.
# تهيئة التطبيق باستخدام ثيم LUX
# ثيم LUX يعطي مظهراً راقياً وعصرياً للوحة البيانات.
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Full Professional Analysis"

# 3. Layout Design
# تصميم الواجهة وتوزيع العناصر في صفوف وأعمدة
app.layout = dbc.Container([
    
    # Main Header
    # العنوان الرئيسي للوحة البيانات
    dbc.Row([
        dbc.Col(html.H1("Ford GoBike Comprehensive Dashboard", 
                        className='text-center text-primary mb-4 mt-4'), width=12)
    ]),

    # KPI Section: Quick Stats Cards
    # قسم مؤشرات الأداء: كروت تعرض أرقام ملخصة سريعة
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H6("Total Trips | إجمالي الرحلات", className="text-muted"),
            html.H3(f"{len(df):,}", className="text-primary")
        ])), width=4),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H6("Avg Duration (Min) | متوسط المدة", className="text-muted"),
            html.H3(f"{df['duration_min'].mean():.1f}", className="text-info")
        ])), width=4),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H6("Subscribers % | نسبة المشتركين", className="text-muted"),
            html.H3(f"{(df['user_type']=='Subscriber').mean()*100:.1f}%", className="text-success")
        ])), width=4),
    ], className="mb-4"),

    # Middle Section: Hourly Peaks and User Types
    # القسم الأوسط: توزيع الرحلات حسب الساعة ونوع المستخدم
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Hourly Trip Distribution | توزيع الرحلات حسب الساعة"),
                dbc.CardBody(dcc.Graph(figure=px.histogram(df, x='hour', color_discrete_sequence=['#2c3e50'])))
            ])
        ], width=8),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("User Type Distribution | أنواع المستخدمين"),
                dbc.CardBody(dcc.Graph(figure=px.pie(df, names='user_type', hole=0.4)))
            ])
        ], width=4),
    ], className="mb-4"),

    # Demographics Section: Gender and Age
    # قسم البيانات الديموغرافية: النوع (جنس) والفئات العمرية
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Trips by Gender | الرحلات حسب الجنس"),
                dbc.CardBody(dcc.Graph(figure=px.bar(df['member_gender'].value_counts().reset_index(), 
                                                 x='member_gender', y='count', color='member_gender')))
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Trips by Age Group | الرحلات حسب العمر"),
                dbc.CardBody(dcc.Graph(figure=px.bar(df['age_group'].value_counts().reset_index(), 
                                                 x='age_group', y='count', color='age_group')))
            ])
        ], width=6),
    ], className="mb-4"),

    # Bottom Section: Top Stations and Day Type
    # القسم السفلي: أعلى المحطات ومقارنة أيام الأسبوع بالويك إيند
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Top 10 Start Stations | أهم 10 محطات"),
                dbc.CardBody(dcc.Graph(figure=px.bar(df['start_station_name'].value_counts().head(10).reset_index(), 
                                                 x='count', y='start_station_name', orientation='h', color='count')))
            ])
        ], width=7),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Weekday vs Weekend | العمل مقابل الإجازة"),
                dbc.CardBody(dcc.Graph(figure=px.pie(df, names='day_type', color_discrete_sequence=['#636EFA', '#EF553B'])))
            ])
        ], width=5),
    ]),

    # Footer
    # تذييل الصفحة
    html.Footer("Final Professional Project - Developed with ❤️ | تم التطوير بكل حب", 
                className="text-center mt-5 pb-3 text-muted")

], fluid=True)

# 4. Run the server
# تشغيل خادم التطبيق
if __name__ == "__main__":
    app.run(debug=True)