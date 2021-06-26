import dash_bootstrap_components as dbc
import dash_html_components as html


footer = html.Div(children = [
    dbc.NavbarSimple(
        [
            dbc.NavItem(dbc.NavLink("About us", href="/views/about_us_view")),
            dbc.NavItem(dbc.NavLink("Documentation", href="https://rehome.readthedocs.io/en/latest/index.html")),
            dbc.NavItem(dbc.NavLink("GitHub", href="https://github.com/rehomewebapp/REhome")),
        ],color="success",className="navbar-dark"
    )
])


