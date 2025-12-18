from fastapi import APIRouter
from lessons import tuples_files

router = APIRouter(tags=["Tuples & Files"])

# ---------- TUPLES ----------

@router.get("/tuples-basics")
def tuples_basics():
    return tuples_files.tuples_basics()

@router.get("/tuples-immutability")
def tuples_immutability():
    return tuples_files.tuples_immutability()

@router.get("/tuples-operations")
def tuples_operations():
    return tuples_files.tuples_operations()

@router.get("/tuples-unpacking")
def tuples_unpacking():
    return tuples_files.tuples_unpacking()

@router.get("/tuples-vs-lists")
def tuples_vs_lists():
    return tuples_files.tuples_vs_lists()


# ---------- FILES ----------

@router.get("/files-write-read")
def files_write_read():
    return tuples_files.files_write_read()

@router.get("/files-readlines")
def files_readlines():
    return tuples_files.files_readlines()

@router.get("/files-iterator")
def files_iterator():
    return tuples_files.files_iterator()

@router.get("/files-buffering")
def files_buffering():
    return tuples_files.files_buffering()

@router.get("/files-quiz")
def files_quiz():
    return tuples_files.files_quiz()
