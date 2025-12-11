# app/01_numbers.py

import sys
import math
import random

# عدد 0 یعنی "نامحدود" برای تعداد رقم‌های تبدیل به رشته
sys.set_int_max_str_digits(0)

# مقادیر محاسبه‌شده
int_add = 123 + 222
float_mul = 1.5 * 4
power_2_100 = 2 ** 100
big = 2 ** 1000000
digits_count = len(str(big))
pi_val = math.pi
sqrt_func = math.sqrt  # تابع، می‌تونی برای مثال math.sqrt(85) استفاده کنی
rand_val = random.random()
rand_choice = random.choice([1, 2, 3, 4])

# 1️⃣ خروجی به ترمینال
print("Integer addition:", int_add)
print("Float multiplication:", float_mul)
print("Power:", power_2_100)
print("Digits count of 2^1,000,000:", digits_count)
print("math.pi:", pi_val)
print("math.sqrt:", sqrt_func)
print("random.random():", rand_val)
print("random.choice([1,2,3,4]):", rand_choice)

# 2️⃣ خروجی به فایل لاگ
with open("numbers_output.log", "w") as f:
    f.write(f"Integer addition: {int_add}\n")
    f.write(f"Float multiplication: {float_mul}\n")
    f.write(f"Power: {power_2_100}\n")
    f.write(f"Digits count of 2^1,000,000: {digits_count}\n")
    f.write(f"math.pi: {pi_val}\n")
    f.write(f"math.sqrt: {sqrt_func}\n")
    f.write(f"random.random(): {rand_val}\n")
    f.write(f"random.choice([1,2,3,4]): {rand_choice}\n")

# 3️⃣ خروجی برای وب از طریق main.py
def get_numbers_info():
    return {
        "int_add": int_add,
        "float_mul": float_mul,
        "power_2_100": power_2_100,
        "digits_count": digits_count,
        "pi": pi_val,
        "sqrt_func": str(sqrt_func),  # توی JSON نمی‌تونیم تابع ارسال کنیم
        "random": rand_val,
        "random_choice": rand_choice
    }
