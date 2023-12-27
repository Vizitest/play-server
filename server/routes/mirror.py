from flask import request
from server.app import app
from server.constants import CONTENT_TYPE_JSON
import json


@app.route('/mirror/<int:response_code>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def mirror(response_code: int, path: str):  # put application's code here
    """
    This endpoint is special. It sends you back exactly what you sent to it.
    The response code is the same as the first path parameter. The complete remaining path is collected into
    a string and also returned.
    """
    method = request.method
    query = dict(request.args)
    headers = dict(request.headers)
    cookies = dict(request.cookies)
    body = request.get_data(as_text=True)
    return json.dumps({"path": f"/mirror/{response_code}/{path}",
                       "body": {
                           "mime_type": request.content_type,
                           "encoding": request.content_encoding,
                           "content": body
                       },
                       "method": method,
                       "query": query,
                       "headers": headers,
                       "cookies": cookies
                       }), response_code, CONTENT_TYPE_JSON
