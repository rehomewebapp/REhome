
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
    fig.update_layout(transition_duration= 1000, 
                      legend=legend, 
                      yaxis_tickformat = 'd',
                      margin=dict(l=0, r=0, t=0, b=0),
                      )
    graph = dcc.Graph(figure=fig, style={"height":"calc(50vh - 7.5rem)"})
    return graph

@app.callback(
    Output('weatherGraph_content_id', 'children'),
    Input("update_graphs_button_id", "n_clicks"),
)
def update_weather_graph(n_clicks):
    df = read_tmy_data()
    graph = make_weather_graph(df)
    return graph