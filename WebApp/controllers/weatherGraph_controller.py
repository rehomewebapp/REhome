
from app import app
from dash.dependencies import Input, Output

import dash_core_components as dcc
import plotly.graph_objs as go

import numpy as np

from models.building.utilities import read_tmy_data




def make_weather_graph(df):
    fig = go.Figure(data=[go.Scatter(x=np.arange(len(df.index)), y=df.T2m)])
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Temperature in °C')

    legend = dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
    # Change the bar mode
    fig.update_layout(transition_duration= 1000, legend=legend, yaxis_tickformat = 'd')
    graph = dcc.Graph(figure=fig)
    return graph

@app.callback(
    Output('weatherGraph_content_id', 'children'),
    Input("update_weather_button_id", "n_clicks"),
)
def update_weather_graph(n_clicks):
    df = read_tmy_data()
    graph = make_weather_graph(df)
    return graph