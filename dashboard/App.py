import os
import sys
import pandas as pd
from dash import Dash
import dash_bootstrap_components as dbc

# ضبط المسارات
base_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(base_dir, '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# الاستدعاء الصحيح بناءً على الصورة
from preprocessing.preprocessor import BikeSharePreprocessor
from components.layout import create_layout
from components.callbacks import register_callbacks

# تشغيل الـ Pipeline
data_path = os.path.join(base_dir, "..", "data", "raw", "fordgobike-tripdataFor201902.csv")

preprocessor = BikeSharePreprocessor(data_path)
df = (preprocessor
      .load_data()
      .clean_data()
      .engineer_features() # دي اللي بتعمل الـ age_group والـ hour والـ duration_min
      .get_data())

# إعداد التطبيق
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
app.layout = create_layout(df)
register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=True)