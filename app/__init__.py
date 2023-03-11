from flask import Flask

app = Flask(__name__)

from endpoints import home, login, pins, profile, signup, support