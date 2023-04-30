from app import app
from flask import make_response, jsonify, request
from dbhelpers import run_statement
from check import check

# Unaware of what should be here if you don't need to be signed in.
# This is due to the factor of guests/visitors just being able to few pins.
# Support should receive request and send to email address.
# Need procedure made for selecting the email address the support goes to.
# Need to sort out axios call to make pins show the proper details when clicked.