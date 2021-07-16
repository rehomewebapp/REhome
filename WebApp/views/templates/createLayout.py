import dash_html_components as html
import dash_bootstrap_components as dbc

from views.templates.footer import footer
from views.templates.header import create_navbar
from views.templates.content_navigation import create_content_nav

def create_layout(activePage, urlPrev, hint, urlNext, content):

    navbar = create_navbar(activePage)
    content_nav = create_content_nav(activePage, urlPrev, hint, urlNext)

    layout = html.Div(children=[
        navbar,
        html.Div([
                    content,
                    content_nav,
        ], style={'padding':'1rem'}),
        html.Hr(),
        footer,
    ])

    return layout