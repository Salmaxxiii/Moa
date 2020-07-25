# /index.py

from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json

import argparse
import uuid


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# run Flask app
if __name__ == "__main__": 
    app.run()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(silent=True)
    if data['queryResult']['queryText'] == 'hi':
        reply = {"fullfillmentText": "Positive response from webhook!",}
        return jsonify(reply)
    else:
        reply = {"fullfillmentText": "Negative response from webhook!",}
        return jasonify(reply)
