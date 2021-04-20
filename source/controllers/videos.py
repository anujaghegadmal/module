from source import app
from flask import request, make_response
from source.models.videos_model import videos_model
from flask_cors import CORS,cross_origin

obj=videos_model()

@app.route("/videos/create",methods=["POST"])
@cross_origin()
def add_video():
    try:
        data=request.form.to_dict()
        return obj.add_video_model(data)

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/read")
@cross_origin()
def list_video():
    try:
        return obj.list_video_model()

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/update/<video_id>",methods=["POST"])
@cross_origin()
def update_video(video_id):
    try:
        data=request.form.to_dict()
        print(data)
        return obj.update_video_model(data,video_id)

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/delete/<video_id>")
@cross_origin()
def delete_video(video_id):
    try:
        return obj.delete_video_model(video_id)

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/publish_video/<video_id>",methods=["POST"])
@cross_origin()
def publish_video(video_id):
    return obj.publish_video_model(video_id)

@app.route("/videos/active_videos")
@cross_origin()
def get_course_wise_videos():
    try:
        return obj.get_course_wise_videos_model()

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)

@app.route("/videos/video_details/<video_id>")
@cross_origin()
def get_video_details(video_id):
    try:
        return obj.get_video_details_model(video_id)

    except Exception as e:
            return make_response({"Error":"Contact developer"},500)