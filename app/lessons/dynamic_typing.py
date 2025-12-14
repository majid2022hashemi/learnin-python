# app/lessons/dynamic_typing.py

import sys

def variables_and_objects():
    a = 3
    b = a

    return {
        "description": "Variables reference objects, variables have no type",
        "a_value": a,
        "b_value": b,
        "a_is_b": a is b,
        "a_type": type(a).__name__
    }


def immutable_example():
    a = "spam"
    b = a
    b = "shrubbery"

    return {
        "description": "Immutable objects: reassignment does not affect other references",
        "a": a,
        "b": b
    }


def mutable_shared_reference():
    L1 = [2, 3, 4]
    L2 = L1
    L1[0] = 24

    return {
        "description": "Mutable object with shared references (in-place change)",
        "L1": L1,
        "L2": L2,
        "same_object": L1 is L2
    }


def copy_vs_reference():
    L1 = [2, 3, 4]
    L2 = L1[:]
    L1[0] = 24

    return {
        "description": "Copy breaks shared references",
        "L1": L1,
        "L2": L2,
        "same_object": L1 is L2
    }


def equality_vs_identity():
    L1 = [1, 2, 3]
    L2 = [1, 2, 3]

    X = 42
    Y = 42

    return {
        "list_equality": L1 == L2,
        "list_identity": L1 is L2,
        "int_equality": X == Y,
        "int_identity": X is Y,
        "note": "Small integers are cached in Python"
    }


def quiz_answers():
    # Quiz 1
    A1 = "spam"
    B1 = A1
    B1 = "shrubbery"

    # Quiz 2
    A2 = ["spam"]
    B2 = A2
    B2[0] = "shrubbery"

    # Quiz 3
    A3 = ["spam"]
    B3 = A3[:]
    B3[0] = "shrubbery"

    return {
        "quiz_1": {
            "A": A1,
            "changed": False,
            "reason": "Strings are immutable"
        },
        "quiz_2": {
            "A": A2,
            "changed": True,
            "reason": "Lists are mutable and shared by reference"
        },
        "quiz_3": {
            "A": A3,
            "changed": False,
            "reason": "List copy breaks shared reference"
        }
    }
