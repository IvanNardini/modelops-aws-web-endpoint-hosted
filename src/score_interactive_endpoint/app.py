
'''
Module to initiate Dash Server App
'''

import dash

external_stylesheets = ['https://codepen.io/ivannardini/pen/QWyLZJw.css']

app = dash.Dash(__name__, 
                external_stylesheets=external_stylesheets,
                 suppress_callback_exceptions = True)
server = app.server
