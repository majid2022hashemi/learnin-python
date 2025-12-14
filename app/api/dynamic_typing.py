# app/api/dynamic_typing.py

from fastapi import APIRouter
from lessons import dynamic_typing

router = APIRouter(tags=["Dynamic Typing"])

@router.get("/variables-and-objects")
def variables_and_objects():
    return dynamic_typing.variables_and_objects()

@router.get("/immutable-example")
def immutable_example():
    return dynamic_typing.immutable_example()

@router.get("/mutable-shared-reference")
def mutable_shared_reference():
    return dynamic_typing.mutable_shared_reference()

@router.get("/copy-vs-reference")
def copy_vs_reference():
    return dynamic_typing.copy_vs_reference()

@router.get("/equality-vs-identity")
def equality_vs_identity():
    return dynamic_typing.equality_vs_identity()

@router.get("/quiz")
def quiz_answers():
    return dynamic_typing.quiz_answers()
