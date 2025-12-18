import os

# =========================
# TUPLES
# =========================

def tuples_basics():
    T = (1, 2, 3, "spam")
    return {
        "description": "Tuples are ordered, immutable sequences",
        "tuple": T,
        "length": len(T),
        "first_element": T[0],
        "slice": T[1:3]
    }


def tuples_immutability():
    T = (1, 2, 3)
    try:
        T[0] = 99
        changed = True
    except TypeError:
        changed = False

    return {
        "tuple": T,
        "can_be_modified": changed,
        "note": "Tuples cannot be changed in place"
    }


def tuples_operations():
    T = (1, 2, 3)
    return {
        "original": T,
        "concatenation": T + (4, 5),
        "repetition": T * 2,
        "count_2": T.count(2),
        "index_3": T.index(3)
    }


def tuples_unpacking():
    T = (10, 20, 30)
    a, b, c = T

    return {
        "tuple": T,
        "unpacked": {
            "a": a,
            "b": b,
            "c": c
        },
        "note": "Tuple unpacking assigns by position"
    }


def tuples_vs_lists():
    L = [1, 2, 3]
    T = (1, 2, 3)

    L[0] = 99
    try:
        T[0] = 99
    except TypeError:
        pass

    return {
        "list_after_change": L,
        "tuple_after_attempted_change": T,
        "conclusion": "Lists are mutable, tuples are immutable"
    }


# =========================
# FILES
# =========================

FILE_PATH = "app/output.log"


def files_write_read():
    # write
    f = open(FILE_PATH, "w")
    f.write("Hello File\n")
    f.write("Second Line\n")
    f.close()

    # read
    f = open(FILE_PATH, "r")
    content = f.read()
    f.close()

    return {
        "description": "Writing and reading text files",
        "file_path": FILE_PATH,
        "content": content
    }


def files_readlines():
    f = open(FILE_PATH, "r")
    lines = f.readlines()
    f.close()

    return {
        "description": "readlines() reads all lines into a list",
        "lines": lines,
        "line_count": len(lines)
    }


def files_iterator():
    result = []
    for line in open(FILE_PATH):
        result.append(line.rstrip("\n"))

    return {
        "description": "File objects are iterators",
        "lines": result,
        "note": "This is the preferred way to read text files"
    }


def files_buffering():
    f = open(FILE_PATH, "w")
    f.write("Buffered text")
    # not closed yet

    exists_before_close = os.path.exists(FILE_PATH)

    f.close()

    return {
        "buffering": "Output is buffered until close()",
        "file_exists_before_close": exists_before_close,
        "note": "close() flushes buffered data to disk"
    }


def files_quiz():
    # Quiz 1
    f = open(FILE_PATH, "w")
    f.write("Quiz Line\n")
    f.close()

    # Quiz 2
    f = open(FILE_PATH, "r")
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()  # EOF
    f.close()

    return {
        "quiz_1": {
            "question": "Does write() add a newline automatically?",
            "answer": False,
            "reason": "Newlines must be added manually"
        },
        "quiz_2": {
            "line1": line1,
            "line2": line2,
            "line3": line3,
            "note": "EOF is an empty string"
        }
    }
