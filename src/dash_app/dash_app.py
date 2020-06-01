
# -*- coding: utf-8 -*-

import dash
import dash_core_components as component
import dash_html_components as html

app = dash.Dash(__name__)

# Dash apps 1st element: layout
app.layout = html.Div(children=[
    #Title
    html.H1(children='Shopping App'),
    
    html.Div(children=
             """
             A Scoring Interactive Web Service for testing
             """)
])

if __name__ == '__main__':
    app.run_server(port='8052', debug=True)
