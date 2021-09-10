import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from app import app

from views.templates.header import create_navbar
from views.templates.footer import footer

BUILDING_BEFORE = "/assets/building_before.png"
STEP1 = "/assets/Step1.jpg"
STEP2 = "/assets/Step2.jpg"
STEP3 = "/assets/Step3.jpg"
BUILDING_AFTER = "/assets/building_after.png"

# VIEW

content_1 = dbc.Jumbotron(
    [
        html.H1("Welcome to REhome", className="display-3"),
        html.P(
            "An awesome webapp that lets you explore the carbondioxide emissions of buildings.",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(dbc.Button("START", color="primary", href="app", id="start_button_id", n_clicks=0), className="lead"),
    ], style={"margin-bottom":"0rem","padding-bottom":"10rem", "text-align" : "center"}
)


before = dbc.Row(children=[
    dbc.Col(html.Img(src=BUILDING_BEFORE,height = "200px"), style={"text-align" : "right"}),
    dbc.Col(children=[
        html.H1(children=["What is actually the problem?"]),
        html.P("On a global scale 40 % of the primary energy demand can be related to the building sector, resulting in 30 % of the global greenhouse gas emissions. Space heating (63.6 %) and domestic hot water (14.1 %) account for the main energy demand."),
        html.P("We need to drastically reduce our emissions for heating to meet the 1.5 °C goal as stated in the Paris Agreement."),
    ]),
])

step_1 = dbc.Row(children=[
    dbc.Col(children=[
        html.H2(children=["Step 1"]),
        html.H1(children=["Assess curREnt state"]),
        html.P("to get information about your current CO2 footprint for living."),
    ], style={"text-align" : "right"}),
    dbc.Col(html.Img(src=STEP1,height = "200px")),
])

step_2 = dbc.Row(children=[
    dbc.Col(html.Img(src=STEP2,height = "200px"), style={"text-align" : "right"}),
    dbc.Col(children=[
        html.H2(children=["Step 2"]),
        html.H1(children=["REnovate your building envelope"]),
        html.P("to reduce your energy demand for heating."),
    ]),
])

step_3 = dbc.Row(children=[
    dbc.Col(children=[
        html.H2(children=["Step 3"]),
        html.H1(children=["REnew your energy supply system"]),
        html.P("to meet your energy demand in a REnewable way and minimize your CO2 footprint."),
    ], style={"text-align" : "right"}),
    dbc.Col(html.Img(src=STEP3,height = "200px")),
])

after = dbc.Row(children=[
    dbc.Col(html.Img(src=BUILDING_AFTER,height = "200px"), style={"text-align" : "right"}),
    dbc.Col(children=[
        html.H1(children=["REsult"]),
        html.P("Make a step towards a carbon neutral home."),
        html.P("Get an idea about costs and fundings."),
        html.P("And use an awesome WebApp for this (-;"),
    ]),
])


content_2 = html.Div(children=[
    before,
    html.Hr(className="my-2"),
    step_1,
    html.Hr(className="my-2"),
    step_2,
    html.Hr(className="my-2"),
    step_3,
    html.Hr(className="my-2"),
    after,
])

navbar = create_navbar("home")

layout = html.Div(children=[
    navbar,
    content_1,
    content_2,
    footer,
    # needed for the callback, is there a better option if no output is needed?
    html.Div(children=[""], id="home_output_id") 
])

if __name__ == '__main__':
    app.run_server(debug=True)