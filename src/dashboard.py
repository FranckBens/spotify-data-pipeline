import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# Page config
st.set_page_config(page_title="Spotify Dashboard", layout="wide")

st.title("🎧 Spotify Data Dashboard")
st.write("Analyse de mes Top Tracks Spotify")

# Connexion PostgreSQL
conn = psycopg2.connect(
    dbname="spotify_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

# Charger données
query = "SELECT track_name, artist, popularity FROM top_tracks;"
df = pd.read_sql(query, conn)

conn.close()

# KPI
col1, col2, col3 = st.columns(3)

col1.metric("🎵 Nombre de Tracks", len(df))
col2.metric("📈 Popularité Moyenne", round(df["popularity"].mean(), 2))
col3.metric("🎤 Nombre d'Artistes", df["artist"].nunique())

st.divider()

# Top artistes
artist_count = df["artist"].value_counts().reset_index()
artist_count.columns = ["artist", "nb_tracks"]

fig1 = px.bar(
    artist_count.head(10),
    x="artist",
    y="nb_tracks",
    title="Top 10 artistes les plus présents"
)

st.plotly_chart(fig1, use_container_width=True)

# Popularité morceaux
fig2 = px.bar(
    df.sort_values("popularity", ascending=False).head(10),
    x="track_name",
    y="popularity",
    title="Top 10 tracks les plus populaires"
)

st.plotly_chart(fig2, use_container_width=True)

# Tableau données
st.subheader("📄 Données brutes")
st.dataframe(df)