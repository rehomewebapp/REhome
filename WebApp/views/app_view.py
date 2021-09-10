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

location_tab_content = dbc.Card(
    dbc.CardBody([
        location_content,
        dbc.Button("Save", color="primary", id="location_done_button_id", n_clicks=0, disabled=True),
        ]),className="mt-3",
)

occupancy_tab_content = dbc.Card(
    dbc.CardBody([
            occupancy_content,
            dbc.Button("Save", color="primary", id="occupancy_done_button_id", disabled=True),
        ]),className="mt-3",
)

floorplan_tab_content = dbc.Card(
    dbc.CardBody([
            floorplan_content,
            dbc.Button("Save", color="primary", id="floorplan_done_button_id", disabled=True),
        ]),className="mt-3",
)

geometry_tab_content = dbc.Card(
    dbc.CardBody([
            geometry_content,
            dbc.Button("Save", color="primary", id="geometry_done_button_id", disabled=True),
        ]),className="mt-3",
)

materials_tab_content = dbc.Card(
    dbc.CardBody([
            materials_content,
            dbc.Button("Save", color="primary", id="materials_done_button_id", disabled=True),
        ]),className="mt-3",
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
        )

 
output_tabs = dbc.Tabs(
            [
                dbc.Tab( label="Weather", tab_id="weather_tab_id"),
                dbc.Tab( label="Heat demand", tab_id="heatDemand_tab_id"),
                
            ],
            id="output_tabs",
            active_tab="weather_tab_id",
        )

layout = html.Div([
        navbar,
        input_tabs,
        html.Div(id="input_content"),
        output_tabs,
        html.Div(id="output_content"),
        footer,
    ]
)




@app.callback(
    Output("input_content", "children"), 
    #Output("input_tabs", "active_tab"),
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


