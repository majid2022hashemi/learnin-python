def string_basics():
    s = "spam"

    return {
        "description": "Strings are immutable ordered sequences of characters",
        "value": s,
        "type": type(s).__name__,
        "length": len(s)
    }
print(string_basics())