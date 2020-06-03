

'''
This is the docstring for module/script.
'''

import os
import logging
from collections import defaultdict
import pandas as pd
from surprise import dump

import dash
import dash_core_components as component
import dash_html_components as html
from dash.dependencies import Input, Output, State


def locate_model(dest):
    
    """ 
    return path of binary model
    args:
       dest: folder for searching
    returns:
       model_path
    """

    for dirpath, dirnames, filenames in os.walk(dest):
        for filename in [f for f in filenames if f.endswith((".pkl", ".pickle"))]:
            model_path = os.path.join(dirpath, filename)
            return model_path
    return None

def model_reader(model_path):
    """ 
    return predictions and model class
    args:
       model_path: pickle file path
    returns:
       predictions and model
    """
    predictions, algo = dump.load(model_path)
    return predictions, algo

def get_top(predictions, n=10):
    
    '''
    Returns the the top-N recommendation from a set of predictions
    args:
       predictions: predictions generated in testing phase
       n: number of items to suggest (default=10)
    return:
       top_n dictionary: user-prediction dictionaries
    '''
    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
        
    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
        
    return top_n

def get_top_n_ui(top, uid):
    '''
    Returns the list of selected items
    args:
       top: user-prediction dictionaries
       uid: user id for filtering
    return:
       top_n dictionary: user-prediction dictionaries
    '''
    try:
        top_n_ui = [[iid for (iid, _) in user_ratings] for UID, user_ratings in top.items() if UID==uid][0]
        return top_n_ui
    except ValueError: 
        return 0


external_stylesheets = ['https://codepen.io/ivannardini/pen/QWyLZJw.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions = True)

# Page 1

app.layout = html.Div(
    
    #Frame in the iphone cover
    id="iphoneCover", children=[
    
    #Insert a form
    html.Div(id="form_camp", children=[ 
    
    html.Form(children=[
        
        html.Div(id='form_camp_customerid', children=[
            html.Label('Customer ID: '), 
            component.Input(id='uid', name='uid', type='text', placeholder='Customer ID')
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
    
    ], action='/predictions', method='post')]), 
    
        html.Div(id="out1"),
        html.Div(id="out2")
    ])

@app.callback(
    [Output('out2', component_property='children'), 
     Output('out1', component_property='children')], 
    [Input(component_id='uid', component_property='value')]
)

def predict(uid):
#     logging.info('Scoring Application is starting to process the request')
    model_path = locate_model(os.getcwd())
    predictions, _ = model_reader(model_path)
    uid_predictions = get_top_n_ui(get_top(predictions), uid)

    prediction_rank_lenght = len(uid_predictions)
    prediction_rank_labels = ["".join([" Product", str(i)]) for i in range(1,prediction_rank_lenght)]
    products_recommended = pd.DataFrame(list(zip(prediction_rank_labels, uid_predictions)), columns=['Product_Rank', 'Product_id'])

    data = products_recommended.to_dict()
    prodname = data["Product_Rank"]
    prodid = data["Product_id"]
    
    return prodname, prodid

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
