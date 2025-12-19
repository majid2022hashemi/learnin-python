# مطابق Learning Python 6E – Chapter 13 & 14

def for_basics():
    L = [1, 2, 3, 4]
    result = []

    for x in L:
        result.append(x ** 2)

    return {
        "concept": "for iterates over items, not indexes",
        "input": L,
        "output": result
    }


def while_basics():
    L = [1, 2, 3, 4]
    i = 0
    result = []

    while i < len(L):
        result.append(L[i] ** 2)
        i += 1

    return {
        "concept": "while is condition-based, manual control",
        "output": result
    }


def break_continue():
    data = []
    for x in range(1, 6):
        if x == 3:
            continue
        if x == 5:
            break
        data.append(x)

    return {
        "concept": "continue skips, break exits loop",
        "result": data
    }


def for_else():
    items = [1, 3, 5, 7]
    target = 4

    for x in items:
        if x == target:
            found = True
            break
    else:
        found = False

    return {
        "concept": "else runs only if loop ends without break",
        "found": found
    }


def range_usage():
    S = "abcdefghijk"

    by_range = [S[i] for i in range(0, len(S), 2)]
    by_slice = list(S[::2])

    return {
        "concept": "range vs slicing",
        "range_method": by_range,
        "slice_method": by_slice,
        "note": "Slicing is clearer, range may save memory"
    }


def zip_enumerate():
    L1 = [1, 2, 3]
    L2 = [10, 20, 30]

    zipped = []
    for x, y in zip(L1, L2):
        zipped.append(x + y)

    enumerated = []
    for i, c in enumerate("hack"):
        enumerated.append(f"{i}:{c}")

    return {
        "zip_result": zipped,
        "enumerate_result": enumerated
    }


def file_iteration():
    lines = []

    for line in open("app/output.log"):
        lines.append(line.rstrip())

    return {
        "concept": "file objects are iterators",
        "lines_read": lines,
        "best_practice": "for line in open(file)"
    }


def quiz():
    # Quiz 1
    L = [10, 20, 30]
    for x in L:
        x += 1

    # Quiz 2
    L2 = [10, 20, 30]
    for i in range(len(L2)):
        L2[i] += 1

    return {
        "quiz_1": {
            "result": L,
            "changed": False,
            "reason": "x is a copy, not a reference"
        },
        "quiz_2": {
            "result": L2,
            "changed": True,
            "reason": "range gives indexes"
        }
    }
