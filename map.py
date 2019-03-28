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
# map_data = df = pd.read_csv('//Users/jamesswank/Python_projects/solar-map/solarPV.csv')

df = pd.read_csv(
    'https://raw.githubusercontent.com/'
    'plotly/datasets/master/'
    '1962_2006_walmart_store_openings.csv')

# data = [
#     go.Scattermapbox(
#         lat=['45.5017'],
#         lon=['-73.5673'],
#         mode='markers',
#         marker=go.scattermapbox.Marker(
#             size=14
#         ),
#         text=['Montreal'],
#     )
# ]



#  Layouts


body = dbc.Container([
    dbc.Row([
        html.Div(
            [
                dcc.Graph(id='map', figure={
                    'data': [{
                        'lat': df['LAT'],
                        'lon': df['LON'],
                        'marker': {
                            'color': df['YEAR'],
                            'size': 8,
                            'opacity': 0.6
                        },
                        'customdata': df['storenum'],
                        'type': 'scattermapbox'
                    }],
                    'layout': {
                        'mapbox': {
                            'accesstoken': mapbox_access_token,
                            'center': {'lon':-105.5, 'lat':39},
                            'zoom': 7,
                            'style': 'light'
                        },
                        'hovermode': 'closest',
                        'height': 1000
                        # 'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0},
                    },
                }),
            ], 
        ),    
    ])
])

app.layout = html.Div(body)

if __name__ == '__main__':
    app.run_server(debug=True)
