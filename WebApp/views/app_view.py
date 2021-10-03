import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app

from views.templates.header import navbar
from views.templates.footer import footer

from views.location_view import content as location_content
from views.occupancy_view import content as occupancy_content
from views.floorplan_view import content as floorplan_content
from views.geometry_view import content as geometry_content
from views.materials_view import content as materials_content

from views.weather_view import content as weather_content
from views.heatDemand_view import content as heatDemand_content

#INPUT TABS

location_tab_content = dbc.Card(
    dbc.CardBody([
        location_content,
        dbc.Button("Save", color="primary", id="location_done_button_id", n_clicks=0, disabled=True,
            style = {"position":"absolute", "top":"-2.5rem", "right":"1.25rem", "padding-top":"0.5rem", "padding-bottom":"0.5rem"}),
    ],style={"padding-top":"0px", "padding-bottom":"0px"}), style = {"border":"0", "margin-top":"0"}
)

occupancy_tab_content = dbc.Card(
    dbc.CardBody([
        occupancy_content,
        dbc.Button("Save", color="primary", id="occupancy_done_button_id", disabled=True,
            style = {"position":"absolute", "top":"-2.5rem", "right":"1.25rem", "padding-top":"0.5rem", "padding-bottom":"0.5rem"}),
    ],style={"padding-top":"0px", "padding-bottom":"0px"}), style = {"border":"0", "margin-top":"0"}
)

floorplan_tab_content = dbc.Card(
    dbc.CardBody([
        floorplan_content,
        dbc.Button("Save", color="primary", id="floorplan_done_button_id", disabled=True,
            style = {"position":"absolute", "top":"-2.5rem", "right":"1.25rem", "padding-top":"0.5rem", "padding-bottom":"0.5rem"}),
    ],style={"padding-top":"0px", "padding-bottom":"0px"}), style = {"border":"0", "margin-top":"0"}
)

geometry_tab_content = dbc.Card(
    dbc.CardBody([
        geometry_content,
        dbc.Button("Save", color="primary", id="geometry_done_button_id", disabled=True,
            style = {"position":"absolute", "top":"-2.5rem", "right":"1.25rem", "padding-top":"0.5rem", "padding-bottom":"0.5rem"}),
    ],style={"padding-top":"0px", "padding-bottom":"0px"}), style = {"border":"0", "margin-top":"0"}
)

materials_tab_content = dbc.Card(
    dbc.CardBody([
        materials_content,
        dbc.Button("Save", color="primary", id="materials_done_button_id", disabled=True,
            style = {"position":"absolute", "top":"-2.5rem", "right":"1.25rem", "padding-top":"0.5rem", "padding-bottom":"0.5rem"}),
    ],style={"padding-top":"0px", "padding-bottom":"0px"}), style = {"border":"0", "margin-top":"0"}
)

input_tabs = dbc.Tabs(
            [
                dbc.Tab( label="Location", tab_id="location_tab_id"),
                dbc.Tab( label="Usage", tab_id="occupancy_tab_id"),
                dbc.Tab( label="Floorplan", tab_id="floorplan_tab_id"),
                dbc.Tab( label="Geometry", tab_id="geometry_tab_id"),
                dbc.Tab( label="Materials", tab_id="materials_tab_id"),
            ],
            id="input_tabs",
            active_tab="location_tab_id",
            style={"border-bottom":"0", "padding-left":"1.25rem"}
        )


# OUTPUT TABS
weather_tab_content = dbc.Card(
    dbc.CardBody([
        weather_content,
        ],style={"padding-top":"0"}),style = {"border":"0"}
)

heatDemand_tab_content = dbc.Card(
    dbc.CardBody([
        heatDemand_content,
        ],style={"padding-top":"0"}), style = {"border":"0"}
)

output_tabs = dbc.Tabs(
            [
                dbc.Tab( label="Weather", tab_id="weather_tab_id"),
                dbc.Tab( label="Heat demand", tab_id="heatDemand_tab_id"),
            ],
            id="output_tabs",
            active_tab="weather_tab_id",
            style={"border-bottom":"0", "padding-left":"1.25rem"}
        )

output_tabs_bar = dbc.Row(children= [
    dbc.Col(output_tabs),
    dbc.Col(dbc.Button("Update", color="primary", id="update_graphs_button_id", style={"padding-top":"0.5rem", "padding-bottom":"0.5rem"}),style={"text-align":"right", "margin-right":"20px"})
])

layout = html.Div([
        html.Div(id = "input_div", children = [
            navbar,
            input_tabs,
            html.Div(id="input_content"),
        ],style = {"height":"50vh"}),
        html.Div(id = "output_div",children = [
            output_tabs_bar,
            html.Div(id="output_content"),
            footer,
        ],style = {"height":"50vh", 
                   "display":"flex", 
                   "flex-direction":"column",
                   "justify-content":"space-between"}
    ),
])

@app.callback(
    Output("input_content", "children"), 
    Input("input_tabs", "active_tab"),
)
def switch_tab(at):
    if at == "location_tab_id":
        return  location_tab_content
    elif at == "occupancy_tab_id":
        return  occupancy_tab_content
    elif at == "floorplan_tab_id":
        return  floorplan_tab_content
    elif at == "geometry_tab_id":
        return  geometry_tab_content
    elif at == "materials_tab_id":
        return  materials_tab_content
    return html.P("This shouldn't ever be displayed...")


@app.callback(
    Output("output_content", "children"), 
    Input("output_tabs", "active_tab"),
)
def switch_tab(at):
    if at == "weather_tab_id":
        return  weather_tab_content
    elif at == "heatDemand_tab_id":
        return  heatDemand_tab_content
    return html.P("This shouldn't ever be displayed...")

