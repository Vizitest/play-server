from server.app import app
from server.constants import CONTENT_TYPE_JSON
import json

from server.global_data import GLOBAL_DATA


@app.route("/server/<namespace>/reset", methods=["POST"])
def reset(namespace):
    """
    post:
      summary: Reset the given namespace
      parameters:
        - in: path
          name: namespace
          required: true
      responses:
        200:
          content:
            application/json:
    """
    GLOBAL_DATA.create_or_clear_namespace(namespace)
    return json.dumps({"message": "Data was reset"}), 200, CONTENT_TYPE_JSON
