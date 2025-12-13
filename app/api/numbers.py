# app/api/numbers.py

from fastapi import APIRouter
from lessons.numbers import get_numbers_info

router = APIRouter()

@router.get("/")
def numbers_info():
    return get_numbers_info()

