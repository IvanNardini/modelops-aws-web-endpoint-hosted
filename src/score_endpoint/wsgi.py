
from app import app
import logging
import os

import warnings
warnings.filterwarnings("ignore")

if __name__ != '__main__':
    app.run(host='0.0.0.0', port=9999)
    #Return a logger named gunicorn.error
    gunicorn_logger = logging.getLogger('gunicorn.error')
    #Set app logging policies
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

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

# setup model folder
model_folder = '/app/model'
if not os.path.isdir(model_folder):
    app.logger.info("ERROR: Can't find model folder in the file system")
    raise RuntimeError("Model Folder does not exist. Please check how you create the docker image")
    
# locate model pickle
model_path = locate_model(model_folder)
if model_path is None:
    app.logger.info("ERROR: Can't find model pickle file in the {}".format(model_path))
    raise RuntimeError("Can't find model pickle file in the {}!".format(model_path))

print('The Scoring Web Service is ready!')
