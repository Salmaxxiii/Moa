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




#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore

#use the app default credentials
#cred = credentials.ApplicationDefault()
#firebase_admin.initialize_app(cred, {
#    'projectId': project_id,})
#db = firestore.client()

#use a service account
#cred = credentials.Certificate(r'C:\Users\dlgas\source\repos\Moa\Moa\moa-niwamd-23db315d91eb.json')
#firebase_admin.initialize_app(cred)
#db = firestore.client()

#create collection
#doc_ref = db.collection(u'users').document(u'alovelace')
#doc_ref.set({
#    u'first': u'Ada',
#    u'last': 'Lovelace',
#    u'born': 1815})

#read data
#users_ref = db.collection(u'users')
#docs = users_ref.stream()
#for doc in docs:
#    print(u'{} => {}'.format(doc.id, doc.to_dict()))


