import pandas as pd
import psycopg2

# Charger CSV
df = pd.read_csv("data/top_tracks.csv")

# Nettoyage popularity
df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["popularity"] = df["popularity"].fillna(0).astype(int)

# Connexion PostgreSQL
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
        INSERT INTO top_tracks (track_name, artist, popularity)
        VALUES (%s, %s, %s)
    """, (
        row["track_name"],
        row["artist"],
        row["popularity"]
    ))

conn.commit()

cur.close()
conn.close()

print("Données importées dans PostgreSQL ✅")