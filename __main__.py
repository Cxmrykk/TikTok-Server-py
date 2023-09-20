from flask import Flask
from TikTokApi import TikTokApi

app = Flask(__name__)

'''
    TRENDING
'''

@app.route("/trending/videos")
def trending_videos():
    count = request.args.get('count', default=30, type=int)

'''
    USER ROUTES
'''

@app.route("/user/<username>")
def user(username):
    pass

@app.route("/user/<username>/liked")
def user_liked(username):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)

@app.route("/user/<username>/info")
def user_info(username):
    pass

@app.route("/user/<username>/videos")
def user_videos(username):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)

'''
    SEARCH
'''

@app.route("/search/user")
def search_user():
    search_term = request.args.get('search_term', default="", type=str)
    count = request.args.get('count', default=10, type=int)
    cursor = request.args.get('cursor', default=0, type=int)

# "you shouldn’t use this directly, use the other methods."
@app.route("/search/type/<obj_type>")
def search_type(obj_type):
    search_term = request.args.get('search_term', default="", type=str)
    count = request.args.get('count', default=10, type=int)
    cursor = request.args.get('cursor', default=0, type=int)

'''
    HASHTAG
'''

@app.route("/tag/<name>")
def tag(name):
    pass

@app.route("/tag/<name>/info")
def tag_info(name):
    pass

@app.route("/tag/<name>/videos")
def tag_videos(name):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)

'''
    SOUND
'''

@app.route("/song/<id>")
def song(id):
    pass

@app.route("/song/<id>/info")
def song_info(id):
    pass

@app.route("/song/<id>/videos")
def song_videos(id):
    count = request.args.get('count', default=30, type=int)
    cursor = request.args.get('cursor', default=0, type=int)

'''
    VIDEO
'''

'''
    todo: bytes (waiting for TikTokApi to implement)

    @app.route("/video/<id>/download")
    def video_download(id):
        pass
'''

@app.route("/video/<id>")
def video(id):
    pass

@app.route("/video/<id>/comments")
def video_comments(id):
    pass

@app.route("/video/<id>/info")
def video_info(id):
    pass

@app.route("/video/<id>/related")
def video_related(id):
    pass

if __name__ == "__main__":
    app.run(debug=True)