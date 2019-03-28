import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from plotly import graph_objs as go
from plotly.graph_objs import *
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
server = app.server





if __name__ == '__main__':
    app.run_server(debug=True)
