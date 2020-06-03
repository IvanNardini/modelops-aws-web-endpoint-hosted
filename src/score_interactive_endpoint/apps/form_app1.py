
import dash_core_components as component
import dash_html_components as html

#Insert a Input form
form = html.Form(children=[
        
        html.Div(id='form_camp_customerid', children=[
            html.Label('Customer ID: '), 
            component.Input(id='uid', name='username', type='number')
        ]), 
        
        html.Br(), 
        
        html.Div(id='form_camp_password', children=[
            html.Label('Password: '),
            component.Input(id='password', name='password', type='text')
        ]), 
        
        html.Br(), 
        
        html.Div(id='form_camp_username', children=[
             html.Button('Login', type='submit')]), 
    
    action='/predict', method='post'])

# Dash apps 1st element: layout
app.layout = html.Div(
    
    #Record the url
    component.Location(id='url', refresh=False),
    
    #Frame in the iphone cover
    id="iphoneCover", children=[
        html.Div(id="form_camp", children=[form])
])

