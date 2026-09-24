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

# CREATE TABLE (UNE SEULE FOIS)
cur.execute("""
CREATE TABLE IF NOT EXISTS top_tracks (
    track_id TEXT PRIMARY KEY,
    track_name TEXT,
    main_artist TEXT,
    artist_count INT,
    duration_ms INT,
    explicit BOOLEAN,
    track_number INT,
    disc_number INT,
    album_name TEXT,
    album_type TEXT,
    release_date DATE,
    album_total_tracks INT,
    is_playable BOOLEAN,
    is_local BOOLEAN,
    isrc TEXT,
    spotify_url TEXT
);
""")
conn.commit()
logging.info("Table ready")

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
    ON CONFLICT (track_id) DO NOTHING
""", tuple(row))
    except Exception as e:
        logging.error(f"insertion error : {e}")

conn.commit()

cur.close()
conn.close()

logging.info("PostgreSQL import successful")