
'''
This is the docstring for module/script.
'''

import dash

external_stylesheets = ['https://codepen.io/ivannardini/pen/QWyLZJw.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
