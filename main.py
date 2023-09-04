import time
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from instagrapi import Client
from dotenv import load_dotenv

load_dotenv()


def in_docker() -> bool:
    try:
        with open('/.dockerenv', 'r'):
            return True
    except FileNotFoundError:
        pass

    try:
        with open('/proc/self/cgroup', 'r') as f:
            if 'docker' in f.read():
                return True
    except FileNotFoundError:
        pass

    return False

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIFY_CLIENT_ID'),
                                               client_secret=os.getenv(
                                                   'SPOTIFY_CLIENT_SECRET'),
                                               redirect_uri=os.getenv(
                                                   'SPOTIFY_REDIRECT_URI'),
                                               scope='user-read-currently-playing'))

print("Running in docker:", in_docker())

cl = Client()
cl.login(os.getenv("INSTAGRAM_USERNAME"), os.getenv("INSTAGRAM_PASSWORD"))
last_playing_song = None

while True:
    try:
        current_song = sp.current_user_playing_track()
        if current_song is not None:
            current_song_name = current_song['item']['name']
            current_song_artist = current_song['item']['artists'][0]['name']

            if last_playing_song != current_song_name:
                print(
                    f"Currently playing: {current_song_name} by {current_song_artist}")
                cl.send_note(
                    f"🎵 {current_song_name} by {current_song_artist}", 0)

                last_playing_song = current_song_name
    except Exception as e:
        print("Error", e)
        if in_docker():
            raise e
    time.sleep(5)
