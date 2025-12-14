# app/main.py

from fastapi import FastAPI
from api.numbers import router as numbers_router
from api.strings import router as strings_router
from api.dynamic_typing import router as dynamic_typing_router

app = FastAPI(title="Python Tutorial API")

app.include_router(numbers_router, prefix="/numbers")
app.include_router(strings_router, prefix="/strings")
app.include_router(dynamic_typing_router, prefix="/dynamic-typing")

@app.get("/")
def root():
    return {"message": "Welcome to Python Tutorial API"}
