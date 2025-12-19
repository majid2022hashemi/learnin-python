# app/main.py

# app/main.py

from fastapi import FastAPI
from api.numbers import router as numbers_router
from api.strings import router as strings_router
from api.dynamic_typing import router as dynamic_typing_router
from api.strings_fundamentals import router as strings_fundamentals_router
from api.lists_dicts import router as lists_dicts_router
from api.tuples_files import router as tuples_files_router
from api.loops import router as loops_router

app = FastAPI(title="Python Tutorial API")

app.include_router(numbers_router, prefix="/numbers")
app.include_router(strings_router, prefix="/strings")
app.include_router(dynamic_typing_router, prefix="/dynamic-typing")
app.include_router(strings_fundamentals_router, prefix="/strings-fundamentals")
app.include_router(lists_dicts_router, prefix="/lists-dicts")
app.include_router(tuples_files_router,prefix="/tuples_files")
app.include_router(loops_router, prefix="/loops")


@app.get("/")
def root():
    return {"message": "Welcome to Python Tutorial API"}
