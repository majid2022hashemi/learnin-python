import sys, math, random
sys.set_int_max_str_digits(0)

def get_numbers_info():
    int_add = 123 + 222
    float_mul = 1.5 * 4
    power_2_100 = 2 ** 100
    big = 2 ** 1000000
    digits_count = len(str(big))

    return {
        "int_add": int_add,
        "float_mul": float_mul,
        "power_2_100": power_2_100,
        "digits_count": digits_count,
        "pi": math.pi,
        "rand": random.random(),
        "rand_choice": random.choice([1,2,3,4])
    }
