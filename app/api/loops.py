from fastapi import APIRouter
from lessons import loops

router = APIRouter(tags=["Loops"])

@router.get("/for-basics")
def for_basics():
    return loops.for_basics()

@router.get("/while-basics")
def while_basics():
    return loops.while_basics()

@router.get("/break-continue")
def break_continue():
    return loops.break_continue()

@router.get("/for-else")
def for_else():
    return loops.for_else()

@router.get("/range-usage")
def range_usage():
    return loops.range_usage()

@router.get("/zip-enumerate")
def zip_enumerate():
    return loops.zip_enumerate()

@router.get("/file-iteration")
def file_iteration():
    return loops.file_iteration()

@router.get("/quiz")
def quiz():
    return loops.quiz()
