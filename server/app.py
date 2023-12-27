from flask import Flask
app = Flask(__name__)

# noinspection PyUnresolvedReferences
import server.routes
