import plotly.graph_objects as go # or plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd




def create_graph(df):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    data = df.groupby(pd.Grouper(freq='M')).sum()/1000
    fig = px.bar(data, x=months, y=data["Qflow_trans"], labels={'Qflow_trans':'Heat flows [kWh/month]'}, title = "Heat flows")
    fig.update_xaxes(title_text='')
    graph = dcc.Graph(figure=fig)
    return graph
    
