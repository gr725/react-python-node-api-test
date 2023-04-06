from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/merchant_page_initial_data/<string:path>')
def get_info(path):
    title = request.args.get('title')
    description = request.args.get('description')
    
    return path + ' ' + title + ' ' + description
  
