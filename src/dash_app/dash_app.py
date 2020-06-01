
# -*- coding: utf-8 -*-

import dash
import dash_core_components as component
import dash_html_components as html

external_stylesheets = ['https://codepen.io/EugenioPeluso/pen/jOWNmvb.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Dash apps 1st element: layout
app.layout = html.Div(id="iphoneCover", children=[
    
    html.Div(id="form_camp", children=[ 
        
        html.P([
        html.Label('Customer ID: '),
        component.Input(type='text', id='uid')
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
