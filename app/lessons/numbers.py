# app/lessons/numbers.py


from decimal import Decimal, getcontext
from fractions import Fraction
import math


def int_examples():
    return {
        "addition": 2 + 3,
        "multiplication": 4 * 5,
        "power": 2 ** 4,
        "floor_division": 7 // 3,
        "modulus": 7 % 3,
    }


def bitwise_examples():
    x = 1
    return {
        "left_shift": x << 2,   # 1 << 2 = 4
        "right_shift": 8 >> 2,  # 8 >> 2 = 2
        "and": 5 & 3,           # 101 & 011 = 001
        "or": 5 | 3,            # 101 | 011 = 111
        "xor": 5 ^ 3,           # 101 ^ 011 = 110
    }


def float_examples():
    return {
        "division": 1 / 3,
        "round_2_digits": round(2.567, 2),
        "sqrt": math.sqrt(144),
    }


def complex_examples():
    z = 2 + 3j
    return {
        "complex_number": str(z),
        "real_part": z.real,
        "imag_part": z.imag,
        "magnitude": abs(z),
    }


def boolean_examples():
    return {
        "true_is_int": isinstance(True, int),
        "true_equals_1": True == 1,
        "true_plus_4": True + 4,
        "logic_and": True and False,
        "logic_or": True or False,
    }


def decimal_examples():
    getcontext().prec = 4
    return {
        "decimal_division": str(Decimal(1) / Decimal(7)),
        "money_example": str(Decimal("1999.00") + Decimal("1.33")),
    }


def fraction_examples():
    x = Fraction(1, 3)
    y = Fraction(4, 6)
    return {
        "fraction_x": str(x),
        "fraction_y": str(y),
        "addition": str(x + y),
        "multiplication": str(x * y),
        "exact_zero": str(
            Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
        ),
    }


def get_numbers_info():
    return {
        "int": int_examples(),
        "bitwise": bitwise_examples(),
        "float": float_examples(),
        "complex": complex_examples(),
        "boolean": boolean_examples(),
        "decimal": decimal_examples(),
        "fraction": fraction_examples(),
    }

