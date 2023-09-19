#### TikTok API Example
```python
from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("ms_token", None) # get your own ms_token from your cookies on tiktok.com

async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        async for video in api.trending.videos(count=30):
            print(video)
            print(video.as_dict)

if __name__ == "__main__":
    asyncio.run(trending_videos())
```

### Comment
The Comment class in the TikTokApi.api.comment module represents a TikTok comment. Here's a summary of its attributes:
- as_dict: This is a dictionary that contains the raw data associated with the comment.
- author: This is a User object that represents the author of the comment.
- id: This is a string that represents the id of the comment.
- likes_count: This is an integer that represents the number of likes of the comment.
- parent: This is a TikTokApi object.
- text: This is a string that represents the contents of the comment.

### User
The User class in the TikTokApi.api.user module represents a TikTok user. Here's a summary of its attributes and methods:
- as_dict: This is a dictionary that contains the raw data associated with the user.
- info: This asynchronous method returns a dictionary of information associated with the user. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.
- liked: This asynchronous method returns a user’s liked posts if they are public. It takes two parameters: count which is the amount of recent likes you want returned, and cursor which is the offset of likes from 0 you want to get. It raises an InvalidResponseException if TikTok returns an invalid response, the user’s likes are private, or one that is not understood.
- parent: This is a TikTokApi object.
- sec_uid: This is a string that represents the sec UID of the user.
- user_id: This is a string that represents the ID of the user.
- username: This is a string that represents the username of the user.
- videos: This asynchronous method returns a user’s videos. It takes two parameters: count which is the amount of videos you want returned, and cursor which is the offset of videos from 0 you want to get. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.

### Trending
The Trending class in the TikTokApi.api.trending module contains static methods related to trending objects on TikTok. Here's a summary of its attributes and methods:
- parent: This is a TikTokApi object.
- videos: This static method returns videos that are trending on TikTok. It takes one parameter: count which is the amount of videos you want returned. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.

### Search
The Search class in the TikTokApi.api.search module contains static methods about searching TikTok for a phrase. Here's a summary of its attributes and methods:
- parent: This is a TikTokApi object.
- search_type: This static method searches for a specific type of object. It takes four parameters: search_term which is the phrase you want to search for, obj_type which is the type of object you want to search for (user), count which is the amount of users you want returned, and cursor which is the offset of users from 0 you want to get. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.
- users: This static method searches for users. It takes three parameters: search_term which is the phrase you want to search for, count which is the amount of users you want returned, and cursor which is the offset of users from 0 you want to get. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.

### Hashtag
The Hashtag class in the TikTokApi.api.hashtag module represents a TikTok Hashtag/Challenge. Here's a summary of its attributes and methods:
- as_dict: This is a dictionary that contains the raw data associated with the hashtag.
- id: This is a string that represents the ID of the hashtag.
- info: This asynchronous method returns all information sent by TikTok related to this hashtag.
- name: This is a string that represents the name of the hashtag (omitting the #).
- parent: This is a TikTokApi object.
- videos: This asynchronous method returns TikTok videos that have this hashtag in the caption. It takes two parameters: count which is the amount of videos you want returned, and cursor which is the offset of videos from 0 you want to get. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.

### Sound
The Sound class in the TikTokApi.api.sound module represents a TikTok Sound/Music/Song. Here's a summary of its attributes and methods:
- author: This is a User object that represents the author of the song, if it exists.
- duration: This is an integer that represents the duration of the song in seconds.
- id: This is a string that represents TikTok’s ID for the sound.
- info: This asynchronous method returns all information sent by TikTok related to this sound. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.
- original: This is a boolean that indicates whether the song is original or not.
- parent: This is a TikTokApi object.
- title: This is a string that represents the title of the song.
- videos: This asynchronous method returns Video objects of videos created with this sound. It takes two parameters: count which is the amount of videos you want returned, and cursor which is the offset of videos from 0 you want to get. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.

### Video
The Video class in the TikTokApi.api.video module represents a TikTok Video. Here's a summary of its attributes and methods:
- as_dict: This is a dictionary that contains the raw data associated with the video.
- author: This is a User object that represents the User who created the video.
- bytes: This asynchronous method returns the bytes of a TikTok Video.
- comments: This asynchronous method returns the comments of a TikTok Video. It takes two parameters: count which is the amount of comments you want returned, and cursor which is the offset of comments from 0 you want to get.
- create_time: This is a datetime object that represents the creation time of the video.
- hashtags: This is a list of Hashtag objects on the video.
- id: This is a string that represents TikTok’s ID of the video.
- info: This asynchronous method returns a dictionary of all data associated with a TikTok Video. It raises an InvalidResponseException if TikTok returns an invalid response or one that is not understood.
- parent: This is a TikTokApi object.
- related_videos: This asynchronous method returns related videos of a TikTok Video. It takes two parameters: count which is the amount of comments you want returned, and cursor which is the offset of comments from 0 you want to get.
- sound: This is a Sound object that is associated with the video.
- stats: This is a dictionary that represents TikTok’s stats of the video.
- url: This is a string that represents the URL of the video.
