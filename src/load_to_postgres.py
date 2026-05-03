import pandas as pd
import psycopg2

df = pd.read_csv("data/top_tracks.csv")

conn = psycopg2.connect(
    dbname="spotify_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
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