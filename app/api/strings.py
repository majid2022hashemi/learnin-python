from fastapi import APIRouter
from lessons.strings import get_string_info

router = APIRouter()

@router.get("/")
def strings_info():
    return get_string_info()
