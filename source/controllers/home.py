from source import app, token_authenticator, token_data, roles
from flask import request, make_response, send_file
from flask_cors import CORS,cross_origin
import os
import time

@app.route("/")
@cross_origin()
def add_course():
    try:
        return send_file(app.root_path+"/static/index.html")
        # send_file("index.html")
        
    except Exception as e:
        return make_response({"Error":str(e)},500)

# @app.route("/assets",defaults={"path":''})
# @app.route("/assets/<path:path>")
# @cross_origin()
# def asset_handler(path):
#     try:
#         return send_file(app.root_path+"/assets/"+path)
        
#     except Exception as e:
#         return make_response({"Error":str(e)},500)
