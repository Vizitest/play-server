from server.app import app
from server.constants import CONTENT_TYPE_JSON
import json


@app.route('/brew-coffee', methods=['GET'])
def teapot():  # put application's code here
    """
    May make a cup of coffee
    """
    return json.dumps({"message": "I'm a teapot"}), 418, CONTENT_TYPE_JSON
