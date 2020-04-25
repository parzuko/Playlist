
import os
import json
import requests 
from secrets import spotify_user_id, spotify_token

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtube_dl

class CreatePlaylist():

    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = spotify_token
        self.get_youtube_client = self.get_youtube_client()
        self.all_songs_info = {}


    #log into youtube
    def get_youtube_client(self):
        """ Log Into Youtube, Copied from Youtube Data API """
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret.json"

        # Get credentials and create an API client
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        # from the Youtube DATA API
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        return youtube_client

    #get liked vids
    def get_liked_vids(self):
        request = self.youtube_client.videos().list(
            part = "snippet,contentDetails,statistics"
            myRating = "Like"
        )
        response = request.execute()

        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = "https://www.youtube.com/watch?v={}".format(item["id"])

            # use youtube_dl to collect the song name & artist name
            video = youtube_dl.YoutubeDL({}).extract_info(
                youtube_url, download=False)
            song_name = video["track"]
            artist = video["artist"]

            if song_name is not None and artist is not None:
                # save all important info and skip any missing song and artist
                self.all_song_info[video_title] = {
                    "youtube_url": youtube_url,
                    "song_name": song_name,
                    "artist": artist,

                    # add the uri, easy to get song to put into playlist
                    "spotify_uri": self.get_spotify_uri(song_name, artist)

                }    

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
