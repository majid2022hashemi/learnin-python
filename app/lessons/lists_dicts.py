# app/lessons/lists_dicts.py

import copy

def lists_basics():
    L = [1, 2, 3, "spam"]
    return {
        "description": "Lists are ordered, mutable sequences",
        "list": L,
        "length": len(L),
        "first_element": L[0],
        "slice": L[1:3]
    }


def lists_mutation():
    L = [1, 2, 3]
    L[0] = 99
    L.append(4)

    return {
        "description": "Lists can be changed in place",
        "result": L
    }


def lists_methods():
    L = [3, 1, 2]
    return {
        "original": L,
        "sorted": sorted(L),
        "append": L + [4],
        "count_1": L.count(1),
        "index_2": L.index(2)
    }


def dicts_basics():
    D = {"name": "Majid", "lang": "Python"}
    return {
        "description": "Dictionaries store key-value pairs",
        "dict": D,
        "keys": list(D.keys()),
        "values": list(D.values()),
        "get_existing": D.get("name"),
        "get_missing": D.get("age", "not found")
    }


def dicts_mutation():
    D = {"a": 1, "b": 2}
    D["c"] = 3
    D["a"] = 99

    return {
        "description": "Dictionaries are mutable",
        "result": D
    }


def dicts_methods():
    D = {"x": 1, "y": 2}
    removed = D.pop("x")

    return {
        "after_pop": D,
        "removed_value": removed,
        "items": list(D.items())
    }


def copy_vs_reference():
    L1 = [1, 2, [3, 4]]
    L2 = L1
    L3 = L1[:]
    L4 = copy.deepcopy(L1)

    L1[2][0] = 99

    return {
        "shared_reference": L2,
        "shallow_copy": L3,
        "deep_copy": L4,
        "note": "Nested objects require deep copy"
    }


def iteration():
    L = [1, 2, 3]
    D = {"a": 1, "b": 2}

    return {
        "list_iteration": [x * 2 for x in L],
        "dict_keys": [k for k in D],
        "dict_items": [(k, v) for k, v in D.items()]
    }


def quiz():
    # Quiz 1: list mutation
    A1 = [1, 2, 3]
    B1 = A1
    B1.append(4)

    # Quiz 2: dict copy
    A2 = {"x": 1}
    B2 = A2.copy()
    B2["x"] = 99

    # Quiz 3: nested list
    A3 = [[1, 2], [3, 4]]
    B3 = A3[:]
    B3[0][0] = 99

    return {
        "quiz_1": {
            "A": A1,
            "changed": True,
            "reason": "List is mutable and shared by reference"
        },
        "quiz_2": {
            "A": A2,
            "changed": False,
            "reason": "dict.copy() breaks top-level reference"
        },
        "quiz_3": {
            "A": A3,
            "changed": True,
            "reason": "Shallow copy does not copy nested objects"
        }
    }
