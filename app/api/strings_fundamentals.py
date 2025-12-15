# app/api/strings_fundamentals.py

from fastapi import APIRouter
from lessons import strings_fundamentals

router = APIRouter(tags=["String Fundamentals"])

@router.get("/basics")
def basics():
    return strings_fundamentals.basics()

@router.get("/literals")
def literals():
    return strings_fundamentals.literals()

@router.get("/index-slice")
def index_and_slice():
    return strings_fundamentals.index_and_slice()

@router.get("/immutability")
def immutability():
    return strings_fundamentals.immutability()

@router.get("/operations")
def operations():
    return strings_fundamentals.operations()

@router.get("/methods")
def methods():
    return strings_fundamentals.methods()

@router.get("/formatting")
def formatting():
    return strings_fundamentals.formatting()

@router.get("/iteration")
def iteration():
    return strings_fundamentals.iteration()

@router.get("/quiz")
def quiz():
    return strings_fundamentals.quiz()
