# Learning Python 6E – Chapter 14

def iterables():
    return {
        "definition": "Iterable = sequence or object producing values on demand",
        "examples": {
            "sequence": ["list", "tuple", "string"],
            "iterable_only": ["range", "zip", "enumerate", "file"]
        }
    }


def iteration_protocol():
    data = [1, 2, 3]
    it = iter(data)

    steps = [
        next(it),
        next(it),
        next(it)
    ]

    return {
        "iter_call": "iter(data) -> iterator",
        "next_calls": steps,
        "note": "StopIteration raised after last item"
    }


def range_vs_list():
    r = range(5)
    l = list(range(5))

    return {
        "range": {
            "type": str(type(r)),
            "memory": "lazy, no full list in memory",
            "supports_slice": False
        },
        "list": {
            "type": str(type(l)),
            "memory": "fully materialized",
            "supports_slice": True
        }
    }


def file_iterator():
    lines = []

    for line in open("app/output.log"):
        lines.append(line.rstrip())

    return {
        "concept": "Files are iterators",
        "best_practice": "for line in open(file)",
        "lines_read": lines
    }


def list_comprehension():
    L = [1, 2, 3, 4]

    for_loop = []
    for x in L:
        for_loop.append(x ** 2)

    comprehension = [x ** 2 for x in L]

    return {
        "for_loop": for_loop,
        "comprehension": comprehension,
        "note": "Comprehensions are expression-based"
    }


def dict_comprehension():
    keys = ["a", "b", "c"]
    vals = [1, 2, 3]

    D = {k: v for (k, v) in zip(keys, vals)}

    return {
        "dict": D,
        "concept": "zip + comprehension"
    }


def quiz():
    r = range(3)
    try:
        r + r
        works = True
    except TypeError:
        works = False

    comp = [x * 2 for x in range(4)]

    return {
        "quiz_1": {
            "range_plus_range": works,
            "reason": "range is iterable, not sequence"
        },
        "quiz_2": {
            "result": comp,
            "type": str(type(comp))
        }
    }
