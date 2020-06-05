# -*- coding: utf-8 -*-

'''
This is the docstring for module/script.
'''

import os
import logging
from collections import defaultdict
import pandas as pd
from surprise import dump

import dash
import dash_table
import dash_core_components as component
import dash_html_components as html

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions = True)

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

#Customerid Input
c_id_component = component.Input(id="uid", 
                                 type="text", 
                                 placeholder='100')

c_id_div = html.Div(id='customerid', children=[html.Label("Please enter your customer ID : "), 
                                               c_id_component,
                                               html.Br()], 
                   className="six columns")

#Prediction Output
predictions_div = html.Div(id='predictions', 
                           children=[html.H4(children='Products Recommended'),
                                     dash_table.DataTable(id='table')],
                           className="six columns")

app.layout= html.Div(
    
    id="score_gui", children=[
        
        html.H1('Recommendation System for Purchase Data'),
        html.H2('Scoring Interactive Web Service draft'),
        html.Div(children=[c_id_div, 
                           predictions_div], 
                 className="row"),
    ]
)

@app.callback([Output('table', component_property='columns'), Output('table', component_property='data')],[Input(component_id='uid', component_property='value')])
def predict(uid):
    columns = []
    products_recommended = []
    if uid:
        model_path = locate_model(os.getcwd())
        predictions, _ = model_reader(model_path)
        uid_predictions = get_top_n_ui(get_top(predictions), uid)
        prediction_rank_lenght = len(uid_predictions)
        prediction_rank_labels = ["".join([" Product", str(i)]) for i in range(1,prediction_rank_lenght)]
        products_recommended = pd.DataFrame(list(zip(prediction_rank_labels, uid_predictions)), columns=['Product_Rank', 'Product_id'])
        columns=[{"name": i, "id": i} for i in products_recommended.columns]
        return columns, products_recommended.to_dict('records')
    else:
        return columns, products_recommended

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", debug=True)
