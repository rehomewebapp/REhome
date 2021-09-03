import plotly.graph_objects as go # or plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


'''
def create_graph(df):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    data = df.groupby(pd.Grouper(freq='M')).sum()/1000
    data['Qflow_int'] = data['Qflow_int'] * -1
    fig = px.bar(data, x=months, y=[data['Qflow_trans'], data['Qflow_int']], labels={'Qflow_trans':'Transmission losses', 'Qflow_int':'Internal gains'}, title = "Heat flows")
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Heat flows [kWh/month]')
    graph = dcc.Graph(figure=fig)
    return graph
'''


def create_graph(df):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    data = df.groupby(pd.Grouper(freq='M')).sum()/1000
    data['Qflow_int'] = data['Qflow_int'] * -1
    fig = go.Figure(data=[
        go.Bar(name='Internal gains', x=months, y=data['Qflow_int']),
        go.Bar(name='Transmission losses', x=months, y=data['Qflow_trans'])
    ])
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='Heat flows [kWh/month]')
    # Change the bar mode
    fig.update_layout(barmode='relative', title_text='Heat flows')
    graph = dcc.Graph(figure=fig)
    return graph