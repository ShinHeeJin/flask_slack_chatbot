from flask import jsonify
from flask import request
import requests
from . import api

@api.route("/todos", methods=['GET', 'POST'])
def todos():
    if request.method=='POST':
        res = requests.post('https://hooks.slack.com/services/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', json={
            'text' : 'Hello world'
        }, headers={ 'Content-Type' : 'application/json' })
    elif request.method=='GET':
        pass

    data = request.get_json()
    return jsonify(data)

@api.route('/test', methods=['POST'])
def test():
    res = request.form['text']

    print(res)
    return jsonify(res)

