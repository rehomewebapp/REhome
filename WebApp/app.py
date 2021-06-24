import dash

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__,
    external_stylesheets=external_stylesheets,
    suppress_callback_exceptions=True
    )
                 
server = app.server

#this script in required to be put in a seperate python file in case of building multipage apps. The styling of our webpage will also be mentioned here.
