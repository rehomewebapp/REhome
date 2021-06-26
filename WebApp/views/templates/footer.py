import dash_bootstrap_components as dbc
import dash_html_components as html

WINDMILL = "/assets/windmill.png"

footer = html.Div(children = [
    dbc.Col(html.Img(src=WINDMILL, height="150px"), style={"text-align" : "right"}),
    dbc.NavbarSimple(
        [
            dbc.NavItem(dbc.NavLink("About us", href="/views/about_us_view")),
            dbc.NavItem(dbc.NavLink("Documentation", href="https://rehome.readthedocs.io/en/latest/index.html")),
            dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/rehomewebapp/REhome")),
        ],color="success",className="navbar-dark"
    )
])


