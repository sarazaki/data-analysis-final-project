from dash import Dash
import dash_bootstrap_components as dbc
from utils.data_loader import load_data
from components.layout import create_layout
from components.callbacks import register_callbacks
import pandas as pd

df = pd.read_csv("your_dataset.csv")

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

app.layout = create_layout(df)

register_callbacks(app, df)

if __name__ == "__main__":
    app.run_server(debug=True)
