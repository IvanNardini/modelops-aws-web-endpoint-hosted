
'''
Module to render the form page
'''

import dash_core_components as component
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

#Insert a Input form
form = html.Form(children=[
        
        html.Div(id='form_camp_customerid', children=[
            html.Label('Customer ID: '), 
            component.Input(id='uid', type='text', placeholder='Customer ID')
        ]), 
        
        html.Br(), 
        
        html.Div(id='form_camp_password', children=[
            html.Label('Password: '),
            component.Input(id='password', type='password',  placeholder='Enter Password')
        ]), 
        
        html.Br(), 
        
        html.Div(id='form_camp_username', children=[
             html.Button('Login', type='submit')
        ])
    ])

# Dash apps 1st element: layout
layout = html.Div(
    
    #Frame in the iphone cover
    id="iphoneCover", children=[
        
        html.Div(id="form_camp", children=[form])
        
        html.Div(id="link")
        
])

# #Dash apps 2nd element: Callbacks
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     return html.Div([
#         html.H3('You are on page {}'.format(pathname))
#     ])
