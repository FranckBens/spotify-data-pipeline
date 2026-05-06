import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Spotify Analytics", layout="wide")

# SWITCH
USE_DATABASE = False

try:
    if USE_DATABASE:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )

        query = "SELECT * FROM top_tracks;"
        df = pd.read_sql(query, conn)

        conn.close()

    else:
        raise Exception("Force CSV mode")

except:
    st.warning("Using sample dataset (no database connection)")
    df = pd.read_csv("data/sample_top_tracks.csv")

st.title("🎧 Spotify Analytics Dashboard")

# KPI
col1, col2, col3, col4 = st.columns(4)

col1.metric("Tracks", len(df))
col2.metric("Artists", df["main_artist"].nunique())
col3.metric("Explicit %", round(df["explicit"].mean() * 100, 1))
col4.metric("Avg Duration", round(df["duration_ms"].mean()/60000, 2))

st.divider()

# CHARTS
st.subheader("🎤 Top Artists")
st.bar_chart(df["main_artist"].value_counts())

st.subheader("💿 Album Types")
st.bar_chart(df["album_type"].value_counts())

# DATES
df["release_date"] = pd.to_datetime(df["release_date"])
df["year"] = df["release_date"].dt.year

st.subheader("📅 Release Years")
st.bar_chart(df["year"].value_counts().sort_index())

# DATA
st.subheader("📋 Dataset")
st.dataframe(df)
