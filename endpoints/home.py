from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

@app.post('/api/user')
def add_user():
    keys = ["username", "firstName", "email", "password", "city", "bio"]
    userName = request.json.get('username')
    firstName = request.json.get('firstName')
    email = request.json.get('email')
    password = request.json.get('password')
    city = request.json.get('city')
    bio = request.json.get('bio')
    results = run_statement("CALL create_client (?,?,?,?,?,?)", [userName, firstName, email, password, city, bio])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 403)
    
@app.patch('/api/user')
def update_user():
    keys = ["username", "firstName", "email"]
    id = request.json.get('userId')
    userName = request.json.get('username')
    firstName = request.json.get('firstName')
    email = request.json.get('email')
    password = request.json.get('password')
    results = run_statement("CALL update_client (?,?,?,?,?)", [id, userName, firstName, email, password])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 403)