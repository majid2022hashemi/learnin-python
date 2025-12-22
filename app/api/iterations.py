from fastapi import APIRouter
from lessons import iterations

router = APIRouter(tags=["Iterations & Comprehensions"])

@router.get("/iterables")
def iterables():
    return iterations.iterables()

@router.get("/iteration-protocol")
def iteration_protocol():
    return iterations.iteration_protocol()

@router.get("/range-vs-list")
def range_vs_list():
    return iterations.range_vs_list()

@router.get("/file-iterator")
def file_iterator():
    return iterations.file_iterator()

@router.get("/list-comprehension")
def list_comprehension():
    return iterations.list_comprehension()

@router.get("/dict-comprehension")
def dict_comprehension():
    return iterations.dict_comprehension()

@router.get("/quiz")
def quiz():
    return iterations.quiz()
