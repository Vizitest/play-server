from flask import request
from server.app import app
from server.constants import CONTENT_TYPE_JSON
from server.utils import make_user_filter

from server.global_data import GLOBAL_DATA


@app.route('/server/<namespace>/check-credit', methods=['GET'])
def check_credit(namespace: str):  # put application's code here
    """
    get:
      summary: Gets all users in the given namespace, can be restricted with query params
      parameters:
        - in: path
          name: namespace
          required: true
        - in: query
          name: age
          required: true
        - in: query
          name: creditSought
          required: true
        - in: query
          name: duration
          required: true          
      responses:
        404:
          content:
            application/json:
        200:
          content:
            application/json:
    """

    age = int(request.args.get('age'))
    creditSought = float(request.args.get('credit-sought'))
    duration = int(request.args.get('duration'))

    if age<18:
        return {"msg": "We only offer credit to 18 and older"}, 400, CONTENT_TYPE_JSON

    if age>100:
        return {"msg": "We do not offer credit to anyone older than 100"}, 400, CONTENT_TYPE_JSON         
       
    if age<26: 
      if creditSought>1000: 
        return {"msg": "We only offer up to 1000 of credit for 18 to 25 year olds"}, 400, CONTENT_TYPE_JSON
      if duration>24:
         return {"msg": "We offer max 24 months of credit for 18 to 25 year olds" }, 400, CONTENT_TYPE_JSON
      return {"msg": "Credit approved!!!"}, 200, CONTENT_TYPE_JSON

    if creditSought>10000:
       return {"msg": "We only offer up to 10000 of credit if 26 or older"}, 400, CONTENT_TYPE_JSON
    if duration>48:
       return {"msg": "We offer max 48 months of credit if 26 or older" }, 400, CONTENT_TYPE_JSON
    
    return {"msg": "Credit approved!!!"}, 200, CONTENT_TYPE_JSON