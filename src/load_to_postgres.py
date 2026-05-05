import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

df = pd.read_csv("data/top_tracks.csv")

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO top_tracks (
            track_id, track_name, main_artist, artist_count,
            duration_ms, explicit, track_number, disc_number,
            album_name, album_type, release_date, album_total_tracks,
            is_playable, is_local, isrc, spotify_url
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (track_id) DO NOTHING
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("Import PostgreSQL réussi")