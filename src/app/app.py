
# -*- coding: utf-8 -*-

import os
import logging
from collections import defaultdict

import pandas as pd
from surprise import dump

import flask

#create an instance
app = flask.Flask(__name__)

def locate_model(dest):
    
    '''
    Locate model pickle file
    
    '''
    for dirpath, dirnames, filenames in os.walk(dest):
        for filename in [f for f in filenames if f.endswith((".pkl", ".pickle"))]:
            model_path = os.path.join(dirpath, filename)
            return model_path
    return None

def model_reader(model_path):
    predictions, algo = dump.load(model_path)
    return predictions, algo

def get_top(predictions, n=10):
    
    '''
    Returns the the top-N recommendation from a set of predictions
    
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
    try:
        top_n_ui = [[iid for (iid, _) in user_ratings] for UID, user_ratings in top.items() if UID==uid][0]
        return top_n_ui
    except ValueError: # user was not part of the trainset
        return 0

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    logging.info('Scoring Application is starting to process the request')
    
    #Intiate variables
    data = defaultdict()
    data["success"] = False
    params = flask.request.args
    
    if 'uid' in params.keys():
        uid_toscore = str(params.get('uid'))
        model_path = locate_model(os.getcwd())
        predictions, _ = model_reader(model_path)
        uid_predictions = get_top_n_ui(get_top(predictions), uid_toscore)
        
        prediction_rank_lenght = len(uid_predictions)
        prediction_rank_labels = ["".join([" Product", str(i)]) for i in range(1,prediction_rank_lenght)]
        products_recommended = pd.DataFrame(list(zip(prediction_rank_labels, uid_predictions)), columns=['Product_Rank', 'Product_id'])

        data['response'] = products_recommended.to_dict()
        data['success'] = True
    
    return flask.jsonify(data)
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
