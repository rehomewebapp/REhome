
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc

REHOME_LOGO = "/assets/Logo_med_gray.png"

navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=REHOME_LOGO, height="36px")),
                    #dbc.Col(dbc.NavbarBrand("REhome", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),
    ],color="primary", dark=True,
)