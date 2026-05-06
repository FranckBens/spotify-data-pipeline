# 🎧 Spotify Data Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## 📌 Overview

End-to-end data pipeline simulating a real-world data engineering workflow using Spotify data.  

This project extracts, transforms, stores, and visualizes user listening data.

---

## 🎬 Demo

Run the dashboard instantly using sample data:


## 🎯 Why this project

This project was built to practice real-world data engineering concepts:
- API integration
- Data pipeline design
- Database modeling  
- Data visualization  
Being passionate about music, I have always had a great interest in musical data.  
This project helped me understand how to structure a real-world data pipeline from scratch.  

## 📊 Dashboard Preview

<p align="center">
  <img src="assets/dashboard.gif" width="800"/>
</p>

---

## ⚙️ Tech Stack
- Python (data extraction & processing)
- PostgreSQL (data storage)
- SQL (data analysis)
- Streamlit (data visualization)
- Git & GitHub (version control)

---

## 🔄 Pipeline Architecture

Spotify API (OAuth)  
          ↓  
Python (Extract)  
        ↓  
CSV (Raw data)  
        ↓  
PostgreSQL (Load)  
        ↓  
SQL (Transform & Analysis)  
        ↓  
Streamlit Dashboard  

---

## 🚀 Features
- OAuth authentication with Spotify API
- Extraction of user's Top Tracks
- Data transformation and cleaning
- Storage in PostgreSQL
- Analytical SQL queries
- Interactive Streamlit dashboard
- Automated pipeline execution (Windows Task Scheduler)
- Secure environment variables management (.env)

---

## 🔐 Data Privacy

This project does not include personal listening data.  

A sample dataset is provided for demonstration purposes.   

---

## 📊 Sample Insights  
- Percentage of explicit tracks  
- Average track duration  
- Albums vs Singles distribution  
- Top artists ranking  
- Release year trends  

---

## 🚀 Quick Start (No Setup Required)  

Run the dashboard instantly using sample data:  
</> Bash  
  
pip install -r requirements.txt  
  
python -m streamlit run src/dashboard.py  

## 🛠️ How to Run (Step by step)  

### 1. Clone the repository  
</> Bash  
git clone https://github.com/FranckBens/spotify-data-pipeline.git  

cd spotify-data-pipeline  

### 2. Creat and Setup a virtual environment  
</> Bash  
 Windows:    
python -m venv venv  
  
 Mac/Linux:  
python3 -m venv venv  

-Activate it:  
</> Bash  
 Windows:   
venv/Scripts/activate  

 Mac/Linux:    
source venv/bin/activate  

### 3. Install dependencies  
</> Bash  
pip install -r requirements.txt  

### 4. Run the project (no database required)  
</> Bash  
 Windows:  
python -m streamlit run src/dashboard.py  

 Mac/Linux:    
python3 -m streamlit run src/dashboard.py  

|-Make sure "USE_DATABASE = False" line 12 in dashboard.py-|   

### 🧪 Optional: Run full pipeline (with PostgreSQL)  

### 5. Install and Create PostgreSQL database  

Download PostgreSQL:  
https://www.enterprisedb.com/download-postgresql-binaries  

Open PostgreSQL and run:  
</> SQL  
CREATE DATABASE spotify_db;  
|-Choose your password-|

### 6. Create table  
</> SQL  
CREATE TABLE top_tracks (  
    track_name TEXT,  
    main_artist TEXT,  
    artist_count INT,  
    album_name TEXT,  
    release_date DATE,  
    duration_ms INT,  
    explicit BOOLEAN,  
    popularity INT,  
    album_type TEXT  
);  

### 7. Configuration

Configure .env file:
</> env
- Go to: https//developer.spotify.com/ -> Log in -> Dashboard -> Create app
   
CLIENT_ID=your_spotify_client_id  
CLIENT_SECRET=your_spotify_client_secret  
  
DB_NAME=spotify_db  
DB_USER=postgres  
DB_PASSWORD=your_password  
DB_HOST=localhost  
DB_PORT=5432  
  

- Don't forget to update your information for this to work:  
CLIENT_ID=your_spotify_client_id  
CLIENT_SECRET=your_spotify_client_secret  
DB_PASSWORD=your_password_from_postgres_db  
  
  
### 8. Run pipeline and Launch dashboard  
</> Bash   
python src/auth.py   
python src/load_to_postgres.py  
  
Windows:
python -m streamlit run src/dashboard.py

Mac/Linux:
python3 -m streamlit run src/dashboard.py

---

📂 **Project Structure**

spotify-data-pipeline/  
│  
├── data/  
│   └── sample_top_tracks.csv  
│  
├── src/  
│   ├── auth.py  
│   ├── load_to_postgres.py  
│   └── dashboard.py  
│  
├── assets/  
│   └── dashboard.gif  
│  
├── .env.example  
├── README.md  
├── requirements.txt   
└── run_etl.bat  

----

## 🎯 Key Learnings
- Building an end-to-end ETL pipeline
- Working with REST APIs and OAuth
- Designing relational data models
- Writing analytical SQL queries
- Automating workflows
- Managing secrets securely

## 📌 Future Improvements
- Improve sample_top_tracks.csv
- Add Airflow for orchestration
- Interactions with the user
- Deploy dashboard online
- Add historical tracking over time
- Integrate more Spotify endpoints (audio features)
