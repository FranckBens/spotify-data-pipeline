import pandas as pd
import psycopg2
import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

df = pd.read_csv("data/top_tracks.csv")

# CONNECTION
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

logging.info("Connection successful !!")

cur = conn.cursor()

# INSERT 
for _, row in df.iterrows():
    try:
        cur.execute("""
            INSERT INTO top_tracks (
                track_id, track_name, main_artist, artist_count,
                duration_ms, explicit, track_number, disc_number,
                album_name, album_type, release_date, album_total_tracks,
                is_playable, is_local, isrc, spotify_url
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            track_id TEXT PRIMARY KEY
        """, tuple(row))
    except Exception as e:
        logging.error(f"insertion error : {e}")

conn.commit()

cur.close()
conn.close()

logging.info("PostgreSQL import successful")