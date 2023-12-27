from server.app import app
from server.utils import build_api_info


@app.route("/api", methods=["GET"])
def get_api():
    """
    get:
      summary: Retrieve the api endpoints
      responses:
        200:
          content:
            application/json:
    """
    return build_api_info()
