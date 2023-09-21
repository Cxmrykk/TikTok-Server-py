from TikTokApi import TikTokApi
from TikTokApi.exceptions import InvalidResponseException
import asyncio

def sound_to_dict(sound):
    if sound is None:
        return sound

    return {
        "author": user_to_dict(getattr(sound, "author", None)),
        "duration": getattr(sound, "duration", None),
        "id": sound.id,
        "original": getattr(sound, "original", None),
        "title": getattr(sound, "title", None)
    }

def hashtag_to_dict(hashtag):
    if hashtag is None:
        return hashtag

    return {
        "id": getattr(hashtag, "id", None),
        "name": getattr(hashtag, "name", None)
    }

def comment_to_dict(comment):
    if comment is None:
        return comment

    return {
        "author": user_to_dict(comment.author),
        "id": comment.id,
        "likes_count": comment.likes_count,
        "text": comment.text
    }

def user_to_dict(user):
    if user is None:
        return user

    return {
        "sec_uid": user.sec_uid,
        "user_id": user.user_id,
        "username": user.username
    }

def video_to_dict(video):
    if video is None:
        return video

    return {
        "author": user_to_dict(getattr(video, "author", None)),
        "create_time": getattr(video, "create_time", None),
        "hashtags": list(map(hashtag_to_dict, getattr(video, "hashtags", []))),
        "id": getattr(video, "id", None),
        "sound": sound_to_dict(getattr(video, "sound", None)),
        "stats": getattr(video, "stats", None),
        "url": getattr(video, "url", None)
    }

'''
    Known issues:
    - "count" is acting as a minimum instead of being absolute
'''

class TikTok:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.api = TikTokApi()

    def run(self):
        self.loop.run_until_complete(self.api.create_sessions(
            num_sessions=1,
            headless=True
        ))

    '''
        TRENDING
    '''
    
    def get_trending_videos(self, count):
        async def query():
            return [video_to_dict(video) async for video in self.api.trending.videos()]
            
        return self.loop.run_until_complete(query())
    
    '''
        USER
    '''

    def get_user(self, username):
        return self.loop.run_until_complete(self.api.user(username).info())

    # currently broken; future hangs if users liked videos are private (expected behaviour: InvalidResponseException)
    def get_user_liked(self, username, count, cursor):
        async def query():
            return [video_to_dict(video) async for video in self.api.user(username).liked(count, cursor)]

        return self.loop.run_until_complete(query())

    def get_user_videos(self, username, count, cursor):
        async def query():
            return [video_to_dict(video) async for video in self.api.user(username).videos(count, cursor)]
        
        return self.loop.run_until_complete(query())

    '''
        SEARCH
    '''

    def search_user(self, search_term, count, cursor):
        async def query():
            return [user_to_dict(user) async for user in self.api.search.users(search_term, count, cursor)]

        return self.loop.run_until_complete(query())

    def search_type(self, obj_type, search_term, count, cursor):
        async def query():
            return [user_to_dict(user) async for user in self.api.search.search_type(search_term, obj_type, count, cursor)]

        return self.loop.run_until_complete(query())

    '''
        HASHTAG
    '''

    def get_tag(self, name):
        return self.loop.run_until_complete(self.api.hashtag(name).info())

    def get_tag_videos(self, name, count, cursor):
        async def query():
            return [video_to_dict(video) async for video in self.api.hashtag(name).videos(count, cursor)]

        return self.loop.run_until_complete(query())

    '''
        SOUND
    '''

    def get_song(self, id):
        return self.loop.run_until_complete(self.api.sound(id).info())

    def get_song_videos(self, id, count, cursor):
        async def query():
            return [video_to_dict(video) async for video in self.api.song(id).videos(count, cursor)]

        return self.loop.run_until_complete(query())

    '''
        VIDEO
    '''

    def get_video(self, url):
        return self.loop.run_until_complete(self.api.video(url=url).info())

    def get_video_comments(self, id, count, cursor):
        async def query():
            return [comment_to_dict(comment) async for comment in self.api.video(id).comments(count, cursor)]

        return self.loop.run_until_complete(query())

    def get_video_related(self, id, count, cursor):
        async def query():
            return [video_to_dict(video) async for video in self.api.video(id).related_videos(count, cursor)]

        return self.loop.run_until_complete(query())