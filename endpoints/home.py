from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

@app.get('/api/pins')
def get_pins():
    pins = request.args.get()
    keys = ["title", "bio", "created_at", "photo", "resource"]
    # results = run_statement("CALL get_pins(?)", [pins?)
    results = run_statement("CALL get_pins")
    response = []
    if (type(results) == list):
        for client in results:
            response.append(dict(zip(keys, client)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 500)