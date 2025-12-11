
# app/02_strings.py

S = "Hello, Python!"

# 1️⃣ خروجی به ترمینال
print("Original string:", S)
print("Uppercase:", S.upper())
print("Length:", len(S))

# 2️⃣ خروجی به فایل لاگ
with open("output.log", "w") as f:
    f.write(f"Original string: {S}\n")
    f.write(f"Uppercase: {S.upper()}\n")
    f.write(f"Length: {len(S)}\n")

# 3️⃣ خروجی برای وب از طریق main.py
def get_string_info():
    return {
        "original": S,
        "uppercase": S.upper(),
        "length": len(S)
    }
