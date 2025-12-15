# app/lessons/strings_fundamentals.py

def basics():
    s = "spam"
    return {
        "description": "Strings are immutable sequences of characters",
        "value": s,
        "type": type(s).__name__,
        "length": len(s)
    }


def literals():
    return {
        "single_quotes": 'spam',
        "double_quotes": "spam",
        "triple_quotes": """multi
line
string""",
        "escape_sequences": "s\np\ta",
        "raw_string": r"C:\new\test.txt"
    }


def index_and_slice():
    s = "python"
    return {
        "string": s,
        "index_0": s[0],
        "index_minus_1": s[-1],
        "slice_1_4": s[1:4],
        "slice_all": s[:]
    }


def immutability():
    s = "spam"
    try:
        s[0] = "x"
        result = "changed"
    except TypeError as e:
        result = str(e)

    return {
        "description": "Strings cannot be changed in place",
        "error": result
    }


def operations():
    s = "spam"
    return {
        "concatenation": s + " eggs",
        "repetition": s * 3,
        "membership": "pa" in s
    }


def methods():
    s = " spam,Spam,SPAM "
    return {
        "original": s,
        "lower": s.lower(),
        "upper": s.upper(),
        "strip": s.strip(),
        "replace": s.replace("Spam", "eggs"),
        "split": s.split(","),
        "startswith": s.startswith(" "),
        "endswith": s.endswith(" ")
    }


def formatting():
    kind = "Norwegian Blue"
    return {
        "percent_formatting": "This is a %s parrot" % kind,
        "format_method": "This is a {} parrot".format(kind),
        "f_string": f"This is a {kind} parrot"
    }


def iteration():
    s = "spam"
    return {
        "characters": [c for c in s],
        "ord_values": list(map(ord, s))
    }


def quiz():
    # Quiz 1
    A1 = "spam"
    A1_new = A1 + "!"

    # Quiz 2
    A2 = "spam"
    B2 = A2
    B2 = "eggs"

    # Quiz 3
    A3 = "spam"
    B3 = A3
    same_object = A3 is B3

    return {
        "quiz_1": {
            "original": A1,
            "after_concat": A1_new,
            "changed": False,
            "reason": "Concatenation creates a new string"
        },
        "quiz_2": {
            "A": A2,
            "B": B2,
            "changed": False,
            "reason": "Reassignment does not affect other references"
        },
        "quiz_3": {
            "same_object": same_object,
            "note": "Small strings may be cached"
        }
    }
