import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.createLayout import create_layout

comfortTempWithTooltip = html.P([
    html.Span("Comfort temperature", id="tooltip_comfortTemp", style={"cursor": "pointer"}),
    " [°C]"
], style={'margin-bottom':'0'})

comfTempInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label( comfortTempWithTooltip,
                                html_for="comfortTemp_id"),
                    dbc.Input(type="number", id="comfortTemp_id", placeholder="Comfort temperature ")
                ]), width=6
        )


internalGainsWithTooltip = html.P([
    html.Span("Internal Gains", id="tooltip_intGains", style={"cursor": "pointer"}),
    " [W/(m^2)]"
], style={'margin-bottom':'0'})

internalGainsInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label(internalGainsWithTooltip, html_for="internalGains_id"),
                    dbc.Input(type="number", id="internalGains_id", placeholder="Internal gains ")
                ]), width=6
        )


infWithTooltip = html.P([
    html.Span("Infiltration number", id="tooltip_inf", style={"cursor": "pointer"}),
    " [1/h]"
], style={'margin-bottom':'0'})

infInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label(infWithTooltip, html_for="infNumber_id"),
                    dbc.Input(type="number", id="infNumber_id", placeholder="Infiltration number"),
                    ]), width=6
                )


ventWithTooltip = html.P([
    html.Span("Ventilation number", id="tooltip_vent", style={"cursor": "pointer"}),
    " [1/h]"
], style={'margin-bottom':'0'})

ventInput = dbc.Col(
                dbc.FormGroup([
                    dbc.Label(ventWithTooltip, html_for="ventNumber_id"),
                    dbc.Input(type="number", id="ventNumber_id", placeholder="Ventilation number"),
                    ]), width=6
                )

input = html.Div([
                dbc.Row([
                    comfTempInput,
                    internalGainsInput,
                ]),
                dbc.Row([
                    infInput,
                    ventInput,
                ])
            ], 
)

output = html.Div("", id = "occupancy_output_id")


MUCKLA = "/assets/muckla.png"
tooltips = html.Div([
    dbc.Tooltip(children=[
        dbc.Row([
            dbc.Col([html.Img(src=MUCKLA,height = "70px")], style={"text-align" : "right"}),
            dbc.Col(["The minimum temperature you want to have in your living space."], width = 8, style={"text-align" : "left"} )
        ])
    ], target="tooltip_comfortTemp", placement="top"), 
    
    dbc.Tooltip(children=[
        dbc.Row([
            dbc.Col([html.Img(src=MUCKLA,height = "70px")], style={"text-align" : "right"}),
            dbc.Col(["The heat emitted by people and technical devices."], width = 8, style={"text-align" : "left"} )
        ])
    ], target="tooltip_intGains", placement="top"),

    dbc.Tooltip(children=[
        dbc.Row([
            dbc.Col([html.Img(src=MUCKLA,height = "70px")], style={"text-align" : "right"}),
            dbc.Col(["A value describing the air tightness of your building, i. e. how often is the air volume exchanged per hour."], width = 8, style={"text-align" : "left"} )
        ])
    ], target="tooltip_inf", placement="top"), 
    
    dbc.Tooltip(children=[
        dbc.Row([
            dbc.Col([html.Img(src=MUCKLA,height = "70px")], style={"text-align" : "right"}),
            dbc.Col(["A value describing your ventilation behaviour, i. e. how often is the air volume exchanged per hour."], width = 8, style={"text-align" : "left"} )
        ])
    ], target="tooltip_vent", placement="top"),

])


content= html.Div([input, output, tooltips])


layout = create_layout("occupancy","/location", "Specify how you use your building", "/floorplan", content)