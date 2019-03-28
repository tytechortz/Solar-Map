import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc

from plotly import graph_objs as go
from plotly.graph_objs import *
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
server = app.server

mapbox_access_token = 'pk.eyJ1IjoidHl0ZWNob3J0eiIsImEiOiJjanN1emtuc2cwMXNhNDNuejdrMnN2aHYyIn0.kY0fOoozCTY-4IUzcLx22w'
map_data = df = pd.read_csv('//Users/jamesswank/Python_projects/solar-map/solarPV.csv')

#  Layouts
layout_map = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    title='WiFi Hotspots in NYC',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(
            lon=-73.91251,
            lat=40.7342
        ),
        zoom=10,
    )
)

body = dbc.Container([
    dbc.Row([
        html.Div(
            [
                dcc.Graph(id='map-graph',
                            animate=True,
                            style={'margin-top': '20'})
            ], 
        ),    
    ])
])

app.layout = html.Div(body)

if __name__ == '__main__':
    app.run_server(debug=True)
