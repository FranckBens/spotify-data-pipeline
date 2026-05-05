@echo off
cd C:\Users\Bens\spotify-data-pipeline

echo Running Spotify ETL pipeline...

python src/auth.py
python src/load_to_postgres.py

echo Pipeline finished !
pause