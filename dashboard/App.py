from dash import Dash
import dash_bootstrap_components as dbc
from dashboard.utils.data_loader import load_data
from dashboard.components.layout import create_layout
from dashboard.components.callbacks import register_callbacks

DATA_PATH = "data/processed/fordgobike-tripdataFor201902_cleaned.csv"

df = load_data(DATA_PATH)

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Ford GoBike Dashboard"

app.layout = create_layout(df)

register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=True)
