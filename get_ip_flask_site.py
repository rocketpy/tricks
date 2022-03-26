from flask import request
from flask import jsonify


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200


# get client ip flask 
request.environ['HTTP_X_FORWARDED_FOR']


# get flask client ip 
from flask import request


@app.route("/route")
def get_my_ip():
    ip = request.remote_addr
    ...
