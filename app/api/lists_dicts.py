# app/api/lists_dicts.py

from fastapi import APIRouter
from lessons import lists_dicts

router = APIRouter(tags=["Lists & Dictionaries"])

@router.get("/lists-basics")
def lists_basics():
    return lists_dicts.lists_basics()

@router.get("/lists-mutation")
def lists_mutation():
    return lists_dicts.lists_mutation()

@router.get("/lists-methods")
def lists_methods():
    return lists_dicts.lists_methods()

@router.get("/dicts-basics")
def dicts_basics():
    return lists_dicts.dicts_basics()

@router.get("/dicts-mutation")
def dicts_mutation():
    return lists_dicts.dicts_mutation()

@router.get("/dicts-methods")
def dicts_methods():
    return lists_dicts.dicts_methods()

@router.get("/copy-vs-reference")
def copy_vs_reference():
    return lists_dicts.copy_vs_reference()

@router.get("/iteration")
def iteration():
    return lists_dicts.iteration()

@router.get("/quiz")
def quiz():
    return lists_dicts.quiz()
