from source import app
from flask import request, make_response
from source.models.courses_model import courses_model
from flask_cors import CORS,cross_origin

obj=courses_model()

@app.route("/courses/create",methods=["POST"])
@cross_origin()
def add_course():
    try:
        data=request.form.to_dict()
        return obj.add_course_model(data)

    except Exception as e:
        print(e)
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/read")
@cross_origin()
def list_course():
    try:
        return obj.list_course_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/read2")
@cross_origin()
def list_course2():
    try:
        return obj.list_course2_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/update/<course_id>",methods=["POST"])
@cross_origin()
def update_course(course_id):
    try:
        data=request.form.to_dict()
        print(data)
        return obj.update_course_model(data,course_id)

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/delete/<course_id>")
@cross_origin()
def delete_course(course_id):
    try:
        return obj.delete_course_model(course_id)

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/read/deleted_courses")
@cross_origin()
def list_deleted_courses():
    try:
        return obj.list_deleted_courses_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/list_all_courses")
@cross_origin()
def list_all_courses():
    try:
        return obj.list_all_courses_model()

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/search_course/<search>")
@cross_origin()
def search_course(search):
    try:
        return obj.search_course_model(search)

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)

@app.route("/courses/publish_course/<course_id>",methods=["POST"])
@cross_origin()
def publish_course(course_id):
    try:
        return obj.publish_course_model(course_id)

    except Exception as e:
        return make_response({"Error":"Contact developer"},500)
