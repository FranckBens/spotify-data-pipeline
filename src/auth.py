import os
import pandas as pd
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    scope="user-top-read"
))

results = sp.current_user_top_tracks(limit=20)

tracks = []

for item in results["items"]:

    tracks.append({
        "track_id": item["id"],
        "track_name": item["name"],
        "main_artist": item["artists"][0]["name"],
        "artist_count": len(item["artists"]),
        "duration_ms": item["duration_ms"],
        "explicit": item["explicit"],
        "track_number": item["track_number"],
        "disc_number": item["disc_number"],
        "album_name": item["album"]["name"],
        "album_type": item["album"]["album_type"],
        "release_date": item["album"]["release_date"],
        "album_total_tracks": item["album"]["total_tracks"],
        "is_playable": item["is_playable"],
        "is_local": item["is_local"],
        "isrc": item["external_ids"]["isrc"],
        "spotify_url": item["external_urls"]["spotify"]
    })

df = pd.DataFrame(tracks)

df.to_csv("data/top_tracks.csv", index=False)

print("CSV créé !")
print(df.head())