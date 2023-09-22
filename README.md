### Installation
```sh
# clone the repository to disk
git clone https://github.com/Cxmrykk/TikTok-server.git
cd TikTok-server

# create/enter the virtual environment
python -m venv venv
source ./venv/bin/activate

# install dependencies
pip install flask
pip install tiktokapi

# execute the program
python -m server
```

### API routes
| Route | Method | Description | Parameters |
| --- | --- | --- | --- |
| /trending/videos | GET | Returns a list of trending videos. | count (default: 30, type: int): The number of videos to return. |
| /user/\<username> | GET | Returns information about a specific user. |  |
| /user/\<username>/liked | GET | Returns a list of videos liked by a specific user. | count (default: 30, type: int): The number of videos to return. <br>cursor (default: 0, type: int): The pagination cursor. |
| /user/\<username>/videos | GET | Returns a list of videos posted by a specific user. | count (default: 30, type: int): The number of videos to return. <br>cursor (default: 0, type: int): The pagination cursor. |
| /search/user | GET | Searches for users based on a search term. | search_term (default: "", type: str): The search term to use. <br>count (default: 10, type: int): The number of results to return. <br>cursor (default: 0, type: int): The pagination cursor. |
| /search/type/\<obj_type> | GET | Searches for a specific type of object (e.g., hashtag, sound) based on a search term. | search_term (default: "", type: str): The search term to use. <br>count (default: 10, type: int): The number of results to return. <br>cursor (default: 0, type: int): The pagination cursor. |
| /tag/\<name> | GET | Returns information about a specific hashtag. |  |
| /tag/\<name>/videos | GET | Returns a list of videos related to a specific hashtag. | count (default: 30, type: int): The number of videos to return. <br>cursor (default: 0, type: int): The pagination cursor. |
| /song/\<id> | GET | Returns information about a specific sound. |  |
| /song/\<id>/videos | GET | Returns a list of videos related to a specific sound. | count (default: 30, type: int): The number of videos to return. <br>cursor (default: 0, type: int): The pagination cursor. |
| /video/\<id>/comments | GET | Returns a list of comments for a specific video. | count (default: 10, type: int): The number of comments to return. <br>cursor (default: 0, type: int): The pagination cursor. |
| /video/\<id>/related | GET | Returns a list of related videos for a specific video. | count (default: 30, type: int): The number of videos to return. <br>cursor (default: 0, type: int): The pagination cursor. |
