from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

@app.get('/user')
def get_user():
    required = ['token']
    check_info = check(request.json, required)
    if check_info != None:
        return check_info
    username = request.args.get('userName')
    keys = ["username", "firstName", "email", "createdAt"]
    results = run_statement("CALL get_user(?)", [username])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 403)
    
@app.patch('/user')
def update_user():
    keys = ["username", "firstName", "email"]
    id = request.json.get('userId')
    userName = request.json.get('username')
    firstName = request.json.get('firstName')
    email = request.json.get('email')
    password = request.json.get('password')
    results = run_statement("CALL update_user (?,?,?,?,?)", [id, userName, firstName, email, password])
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify(results), 403)