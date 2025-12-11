from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/")
def root():
    conn = get_connection()
    return {"message": "Connected to PostgreSQL successfully!"}
