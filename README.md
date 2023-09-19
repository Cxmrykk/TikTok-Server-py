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
