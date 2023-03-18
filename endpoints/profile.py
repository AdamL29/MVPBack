from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

@app.get('/api/user')
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