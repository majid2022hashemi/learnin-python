import os
import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="db",              # نام سرویس در docker-compose
        port=5432
    )
    return conn
