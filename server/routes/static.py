from server.app import app
from flask import send_from_directory

@app.route("/server/<namespace>/static/<path:path>", methods=["GET"])
def get_static(namespace, path):
    return send_from_directory('static', path)
