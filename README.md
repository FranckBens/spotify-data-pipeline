# 🎧 Spotify Data Pipeline


## 🎯 Project Overcview
This project is an end-to-end data pipeline that extracts personal listening data from the Spotify API, processes it, stores it in a PostgreSQL database, and visualizes insights through an interactive dashboard.

The goal is to simulate a real-world data engineering workflow on a small scale.

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

## 📊 Sample Insights
- Percentage of explicit tracks
- Average track duration
- Albums vs Singles distribution
- Top artists ranking
- Listening trends by release year

---

## 🛠️ How to Run

### 1. Clone the repository
</> Bash

git clone https://github.com/FranckBens/spotify-data-pipeline.git
cd spotify-data-pipeline

### 2. Setup environment
</> Bash

python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
pip install -r requirements.txt

### 3. Configure environment variables
Create a .env file:

DB_NAME=spotify_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

### 4. Run pipeline
</> Bash

python src/auth.py
python src/load_to_postgres.py

### 5. Launch dashboard
</> Bash

python -m streamlit run src/dashboard.py

📂 **Project Structure**

spotify-data-pipeline/
│
├── src/
│   ├── auth.py
│   ├── load_to_postgres.py
│   └── dashboard.py
│
├── data/
├── .env (not committed)
├── README.md
└── requirements.txt

---

🎯 **Key Learnings**
- Building an end-to-end ETL pipeline
- Working with REST APIs and OAuth
- Designing relational data models
- Writing analytical SQL queries
- Automating workflows
- Managing secrets securely

📌 **Future Improvements**
- Add Airflow for orchestration
- Deploy dashboard online
- Add historical tracking over time
- Integrate more Spotify endpoints (audio features)
