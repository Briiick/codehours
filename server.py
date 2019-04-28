from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from . import main

@app.route('/', methods=['GET'])
@cross_origin()
def get_hours():

    response = {
        'hours': main.getNumber()
    }

    return jsonify(response), 200

@app.route('/update', methods=['GET'])
@cross_origin()
def update_hours():
    hours = int(request.args.get('hours'))
    

    response = {
        'updated_hours': main.updateNumber(hours)
    }

    return jsonify(response), 200
