
from flask import Flask

#create an instance
app = Flask(__name__)

#what URL should trigger our function
@app.route('/')
def hello_world():
    return 'Hello, World!'
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
