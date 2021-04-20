from source import app
from flask import request, make_response
from source.models.users_model import users_model
from flask_cors import CORS,cross_origin

obj=users_model()

@app.route("/users/create",methods=["POST"])
@cross_origin()
def add_user():
    try:
        # Getting values sent from postman in request.form
        # Converting Key values in dictionary using to_dict()
        data=request.form.to_dict()
        return obj.add_user_model(data)
        
    except Exception as e:
        print(e)
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/read")
@cross_origin()
def list_user():
    try:
        return obj.list_user_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/update",methods=["POST"])
@cross_origin()
def update_user():
    try:
        return obj.update_user_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/delete/<user_id>")
@cross_origin()
def delete_user(user_id):
    try:
        return obj.delete_user_model(user_id)

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/users/get_single_user_details/<user_id>")
@cross_origin()
def single_user_details(user_id):
    try:
        return obj.single_user_details_model(user_id)

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)