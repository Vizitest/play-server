from flask import request
from server.app import app
from server.constants import CONTENT_TYPE_JSON
import json

from server.global_data import GLOBAL_DATA


@app.route('/server/<namespace>/user/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users(namespace, user_id):  # put application's code here
    """
    [put, post]:
      summary: | Changes or creates a user in the given namespace. if the method is POST,
                 it will not overwrite any existing users in the given namespace
      parameters:
        - in: path
          name: namespace
          required: true
        - in: path
          name: user_id
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - surname
              properties:
                name:
                  type: string
                surname:
                  type: string
              additionalProperties: true
      responses:
        404:
          content:
            application/json:
        200:
          content:
            application/json:
    delete:
      summary: Deletes a user in the given namespace
      parameters:
        - in: path
          name: namespace
          required: true
        - in: path
          name: user_id
          required: true
      responses:
        404:
          content:
            application/json:
        400:
          content:
            application/json:
        201:
    get:
      summary: Gets a user in the given namespace
      parameters:
        - in: path
          name: namespace
          required: true
        - in: path
          name: user_id
          required: true
      responses:
        404:
          content:
            application/json:
        202:
    """
    if request.method == "GET":
        if user_id in GLOBAL_DATA.get(namespace).keys():
            return json.dumps(GLOBAL_DATA.get(namespace)[user_id]), 200, CONTENT_TYPE_JSON
        else:
            return json.dumps({"message": "User not found"}), 404, CONTENT_TYPE_JSON

    if request.method in ['PUT', 'POST']:
        user = request.json
        if 'surname' not in user or 'name' not in user:
            fields = []
            if 'surname' not in user:
                fields.append('surname')
            if 'name' not in user:
                fields.append('name')

            return (json.dumps({"message": "User is missing the following fields: " + ",".join(fields)}), 400,
                    CONTENT_TYPE_JSON)

        if request.method == 'POST':
            if user_id in GLOBAL_DATA.get(namespace).keys():
                return json.dumps("User {} already exists".format(user_id)), 409, CONTENT_TYPE_JSON
        GLOBAL_DATA.add(namespace, user_id, user)

    elif request.method == "DELETE":
        if user_id in GLOBAL_DATA.get(namespace).keys():
            del GLOBAL_DATA.get(namespace)[user_id]
            GLOBAL_DATA.dump_to_file()
            return "", 204
        else:
            return json.dumps({"message": "User does not exist"}), 404, CONTENT_TYPE_JSON
    else:
        return json.dumps({"message": "Unknown method"}), 500, CONTENT_TYPE_JSON
    return json.dumps(GLOBAL_DATA.get(namespace)), 200, CONTENT_TYPE_JSON
