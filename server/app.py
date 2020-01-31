'''server/app.py - main api app declaration'''
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from datacontrollers.userDataController import UserDataController
import json

'''Main wrapper for app creation'''
app = Flask(__name__, static_folder='../build')
CORS(app)

##
# API routes
##

@app.route('/api/users', methods=['GET'])
def getUsers():
  return jsonify(UserDataController().getUsers())

@app.route('/api/user/<int:uid>', methods=['GET'])
def getUser(uid):
  return jsonify(UserDataController().getUsers([uid]))

@app.route('/api/user', methods=['POST'])
def saveUser():
  user_json = request.get_json()
  user = json.loads(user_json)
  return jsonify(UserDataController().saveUser(user))

##
# View route
##

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  '''Return index.html for all non-api routes'''
  #pylint: disable=unused-argument
  return send_from_directory(app.static_folder, 'index.html')