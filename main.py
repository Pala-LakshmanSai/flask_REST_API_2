from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort 

app = Flask(__name__)

api = Api(app)

def abort_if_video_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message = "could not find video")


video_put_args = reqparse.RequestParser();
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("views", type=int, help="views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="likes of the video")

videos = {1: {"name": "pushpa2 movie", "views": 500}}

class Video(Resource):
    def get(self, video_id):
        abort_if_video_doesnt_exist(video_id)
        return videos[video_id]
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

print(videos)

api.add_resource(Video, "/videos/<int:video_id>")

if (__name__ == '__main__'):
    app.run(debug=True)