

import json
from secrets import spotify_user_id
class CreatePlaylist():

    def init(self):
        self.user_id = spotify_user_id
    
    
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
    def get spotify_url(self):
        pass

    #add song to playlist
    def add_song_to_playlist(self):
        pass
