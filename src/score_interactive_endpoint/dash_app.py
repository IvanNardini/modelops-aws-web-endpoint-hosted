
# -*- coding: utf-8 -*-

'''
This is the docstring for module/script.
'''

import dash
import dash_core_components as component
import dash_html_components as html

external_stylesheets = ['https://codepen.io/ivannardini/pen/QWyLZJw.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

# Dash apps 1st element: layout

app.layout = html.Div(
    
    #Frame in the iphone cover
    id="iphoneCover", children=[
    
    #Insert a form
    html.Div(id="form_camp", children=[ 
    
    html.Form(children=[
        
        html.Div(id='form_camp_customerid', children=[
            html.Label('Customer ID: '), 
            component.Input(id='uid', name='username', type='text')
        ]), 
        
        html.Br(), 
        
        html.Div(id='form_camp_password', children=[
            html.Label('Password: '),
            component.Input(id='password', name='password', type='text')
        ]), 
        
        html.Br(), 
        
        html.Div(id='form_camp_username', children=[
             html.Button('Login', type='submit')
        ])
    
    ], action='/predict', method='post')])
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
