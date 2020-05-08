# /index.py

from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# run Flask app
if __name__ == "__main__":
    app.run()

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    # commented out by Naresh
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    if req.get("queryResult").get("action") != "Happy":
        print("Please check your action name in DialogFlow...")
        return {}
    result = req.get("queryResult")
    parameters = result.get("parameters")
    baseurl = 'https://www.google.com/search?q=google&rlz=1C1CHBF_enTN886TN886&oq=google&aqs=chrome..69i57j69i59j69i60l3j69i65l2j69i60.1048j0j7&sourceid=chrome&ie=UTF-8';
    if baseurl is None:
        return {}
    result = urlopen(baseurl).read()
    data = json.loads(result)
    # for some the line above gives an error and hence decoding to utf-8 might help
    # data = json.loads(result.decode('utf-8'))
    res = makeWebhookResult(data)
    return res

def makeWebhookResult(data,currency2):
    query = data.get('Happy')
    if query is None:
        return {}
    
    speech = "GREAT NEWS !  "
    # Naresh
    return {
        "fulfillmentText": speech,
    }