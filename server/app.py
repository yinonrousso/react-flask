'''server/app.py - main api app declaration'''
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from models.user import User

'''Main wrapper for app creation'''
app = Flask(__name__, static_folder='../build')
CORS(app)

##
# Mock Data
##

mockUsers = [User(uid=n, name='User{0}'.format(n), email='user{0}@roussoinc.com'.format(n)) for n in range(25)]

##
# API routes
##

@app.route('/api/items')
def items():
  '''Sample API route for data'''
  return jsonify([{'title': 'A'}, {'title': 'B'}])

@app.route('/api/users')
def getUsers():
  return jsonify(mockUsers)

@app.route('/api/user/<int:uid>')
def getUser(uid):
  try:
    index = mockUsers.index(User(uid=uid))
    return jsonify(mockUsers[index])
  except ValueError as err:
    return jsonify(None)


  

##
# View route
##

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  '''Return index.html for all non-api routes'''
  #pylint: disable=unused-argument
  return send_from_directory(app.static_folder, 'index.html')