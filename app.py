

import json
import requests 
from secrets import spotify_user_id, spotify_token


class CreatePlaylist():

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
    
    #log into youtube
    def get_youtube_client(self):
        pass

    #get liked vids
    def get_liked_vids(self):
        pass

    #create playlist
    def create_playlist(self):
        request_body = json.dumps({
            "name":"YouTube liked videos"
            "description": "All liked vid"
            "public": True
        })
    query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
    response = requests.post(
        query ,
        data=request_body
        headers={
            "Content-Type":"application/json"
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()

    return response_json["id"]

    
    #search song 
    def get spotify_url(self,song_name,artist):
        
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
        song_name,
        artist
    )

    reponse = requests.get(
        query,
        headers = {"Content-Type":"application/json"
                   "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json  = response.json()
    songs = response_json["tracks"]["items"]

    uri = songs[0]["uri"]


    #add song to playlist
    def add_song_to_playlist(self):
        pass
