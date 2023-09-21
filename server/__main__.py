from flask import Flask, request, jsonify
from .api import TikTok

app = Flask(__name__)
tiktok = TikTok()

'''
    TRENDING
'''

@app.route("/trending/videos")
def trending_videos():
    count = request.args.get('count', default=30, type=int)
    return jsonify(tiktok.get_trending_videos(count))

'''
    USER ROUTES
'''

@app.route("/user/<username>")
def user(username):
    return jsonify(tiktok.get_user(username))

@app.route("/user/<username>/liked")
def user_liked(username):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.get_user_liked(username, count, cursor))

@app.route("/user/<username>/videos")
def user_videos(username):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.get_user_videos(username, count, cursor))

'''
    SEARCH
'''

@app.route("/search/user")
def search_user():
    search_term = request.args.get('search_term', default="", type=str)
    count = request.args.get('count', default=10, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.search_user(search_term, count, cursor))

# "you shouldn’t use this directly, use the other methods."
@app.route("/search/type/<obj_type>")
def search_type(obj_type):
    search_term = request.args.get('search_term', default="", type=str)
    count = request.args.get('count', default=10, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.search_type(obj_type, search_term, count, cursor))

'''
    HASHTAG
'''

@app.route("/tag/<name>")
def tag(name):
    return jsonify(tiktok.get_tag(name))

@app.route("/tag/<name>/videos")
def tag_videos(name):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.get_tag_videos(name, count, cursor))

'''
    SOUND
'''

@app.route("/song/<id>")
def song(id):
    return jsonify(tiktok.get_song(id))

@app.route("/song/<id>/videos")
def song_videos(id):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.get_song_videos(id, count, cursor))

'''
    VIDEO
'''

'''
    todo: bytes (waiting for TikTokApi to implement)

    @app.route("/video/<id>/download")
    def video_download(id):
        pass
'''

@app.route("/video")
def video():
    url = request.args.get('url', default=None, type=str)
    return jsonify(tiktok.get_video(url))

@app.route("/video/<id>/comments")
def video_comments(id):
    count = request.args.get('count', default=10, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.get_video_comments(id, count, cursor))

@app.route("/video/<id>/related")
def video_related(id):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)
    return jsonify(tiktok.get_video_related(id, count, cursor))

if __name__ == "__main__":
    tiktok.run()
    app.run()