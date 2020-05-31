
import logging
import flask

#create an instance
app = Flask(__name__)

@app.route('/predict', methods=['GET','POST'])
def predict():
    
    logging.info('Scoring Application is starting to process the request')
    
    #Intiate variables
    data = defaultdict()
    data["success"] = False
#     params = flask.request.args
    
    return flask.jsonify(data)
    
#     if "uid" in params.keys():
        
    
#     ## input checking
#     if not request.json:
#         print("ERROR: API (predict): did not receive request data")
#         return jsonify([])

#     query = request.json
#     query = pd.DataFrame(query)
    
#     if len(query.shape) == 1:
#          query = query.reshape(1, -1)

#     y_pred = model.predict(query)
    
#     return(jsonify(y_pred.tolist()))        
            
# if __name__ == '__main__':
#     saved_model = 'aavail-rf.joblib'
#     model = joblib.load(saved_model)
#     app.run(host='0.0.0.0', port=8080,debug=True)
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
