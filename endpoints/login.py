from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check
from uuid import uuid4

@app.post('/api/client-login')
def client_login():
    required = ['email', 'password']
    check_info = check(request.json, required)
    if check_info != None:
        return check_info
    token = uuid4().hex
    # creates random UUID
    email = request.json.get("email")
    password = request.json.get("password")
    results = run_statement("CALL user_login (?,?,?)", [email, password, token])
    if (type(results) == list):
        if results[0][0] == 1:
            return make_response(jsonify(results,"Login Successful!"), 200)
        elif results[0][0] == 0:
            return make_response(jsonify("Sign in Failed"), 403)
    else:
        return make_response(jsonify(results), 500)
