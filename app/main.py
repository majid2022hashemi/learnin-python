# app/main.py
from fastapi import FastAPI
from _02_strings import get_string_info   # تابع خروجی وب از 02_strings.py
from _01_numbers import get_numbers_info  # تابع خروجی وب از 01_numbers.py

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Visit /string for string info or /numbers for numbers info"}

@app.get("/string")
def string_info():
    return get_string_info()

@app.get("/numbers")
def numbers_info():
    return get_numbers_info()
