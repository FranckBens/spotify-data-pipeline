import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    scope="user-library-read playlist-read-private user-top-read"
))

user = sp.current_user()

print("Connecté à :", user["display_name"])
print("\n🎵 Tes Top Tracks :\n")

results = sp.current_user_top_tracks(limit=10)

for track in results["items"]:
    print(track["name"], "-", track["artists"][0]["name"])