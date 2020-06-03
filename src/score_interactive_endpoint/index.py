
'''
Module to execute the app
'''

import dash_core_components as component
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import form_app1

form_app1.layout()

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
