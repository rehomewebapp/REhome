import dash_html_components as html
import dash_bootstrap_components as dbc

content = html.Div([
    dbc.Row([
        html.P('The annual energy demand for space heating is:  '),
        html.P('',id='shDemand_output_id'),
        html.P('  kWh/a = '),
        html.P('',id='shDemandSpec_output_id'),
        html.P('  kWh/(m²a).'),
    ]),
    dbc.Row([
        html.P('The annual CO2 emissions for space heating are:  '),
        html.P('',id='emissions_output_id'),
        html.P('  kg/a.'),
    ])

])