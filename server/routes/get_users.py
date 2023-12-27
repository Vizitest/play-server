from flask import request
from server.app import app
from server.constants import CONTENT_TYPE_JSON
from server.utils import make_user_filter

from server.global_data import GLOBAL_DATA


@app.route('/server/<namespace>/users', methods=['GET'])
def get_users(namespace: str):  # put application's code here
    """
    get:
      summary: Gets all users in the given namespace, can be restricted with query params
      parameters:
        - in: path
          name: namespace
          required: true
        - in: query
          name: name
          required: false
        - in: query
          name: surname
          required: false
      responses:
        404:
          content:
            application/json:
        200:
          content:
            application/json:
    """
    name = request.args.get('name')
    surname = request.args.get('surname')
    users = dict(filter(make_user_filter(name, surname), GLOBAL_DATA.get(namespace).items()))
    if len(users) == 0:
        return users, 404, CONTENT_TYPE_JSON
    return users, 200, CONTENT_TYPE_JSON
