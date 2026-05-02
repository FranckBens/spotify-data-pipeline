import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    scope="user-library-read playlist-read-private user-top-read"
))

results = sp.current_user_top_tracks(limit=20)

tracks = []

for track in results["items"]:
    tracks.append({
        "track_name": track["name"],
        "artist": track["artists"][0]["name"],
        "popularity": track["popularity"]
    })

df = pd.DataFrame(tracks)

df.to_csv("data/top_tracks.csv", index=False)

print("CSV créé : data/top_tracks.csv")