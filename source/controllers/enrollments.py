from source import app
from flask import request,make_response
from source.models.enrollments_model import enrollments_model
from flask_cors import CORS,cross_origin

obj=enrollments_model()

@app.route("/enrollments/create",methods=["POST"])
@cross_origin()
def add_enrollment():
    try:
        data=request.form.to_dict()
        return obj.add_enrollment_model(data)

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/read")
@cross_origin()
def list_enrollment():
    try:
        return obj.list_enrollment_model()

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/update",methods=["POST"])
@cross_origin()
def update_enrollment():
    try:
        return obj.update_enrollment_model()

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/delete/<id>")
@cross_origin()
def delete_enrollment(id):
    try:
        return obj.delete_enrollment_model(id)

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/enrollments/my_enrollments/<user_id>")
@cross_origin()
def my_enrollments(user_id):
    return obj.my_enrollments_model(user_id)