
import dash_html_components as html
import dash_bootstrap_components as dbc

def create_content_nav(activePage, url_prev, text, url_next):


    if url_prev:
        prev_button = dbc.Col([html.P(dbc.Button("Back", color="success", href=url_prev, id="prev_button_id"))], style={"text-align" : "left"})
    else:
        prev_button = dbc.Col([])

    nextButtonID = activePage + "_done_button_id"

    content_nav = dbc.Row([
        prev_button,
        dbc.Col([
            html.H3(text)
        ], style={"text-align" : "center"}),
        dbc.Col([html.P(dbc.Button("Next", color="primary", href=url_next, id=nextButtonID, n_clicks=0, disabled=True))], style={"text-align" : "right"}),
    ], style={'padding':'1rem'})
    return content_nav