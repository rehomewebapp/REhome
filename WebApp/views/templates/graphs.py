import plotly.graph_objects as go # or plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go



def create_graph(df):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    data = df.groupby(pd.Grouper(freq='M')).sum()/1000
    data['Qflow_int'] = data['Qflow_int'] * -1
    fig = go.Figure(data=[
        go.Bar(name='Internal gains', x=months, y=data['Qflow_int'], marker_color='rgb(255, 95, 45)'),
        go.Bar(name='Transmission ground', x=months, y=data['Qflow_trans_ground'], marker_color='rgb(100, 100, 100)'),
        go.Bar(name='Transmission facade', x=months, y=data['Qflow_trans_facade'], marker_color='rgb(150, 150, 150)'),
        go.Bar(name='Transmission roof', x=months, y=data['Qflow_trans_roof'], marker_color='rgb(200, 200, 200)'),
        go.Bar(name='Ventilation', x=months, y=data['Qflow_vent'], marker_color='rgb(0, 100, 205)'),
    ])
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Heat flows [kWh/month]')
    # Change the bar mode
    fig.update_layout(barmode='relative', title_text='Heat flows', transition_duration= 1000)
    graph = dcc.Graph(figure=fig)
    return graph