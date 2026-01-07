class C2:
    x = "x from C2"

    def z(self):
        return "z from C2"


class C3:
    def w(self):
        return "w from C3"


class C1(C2, C3):
    x = "x from C1"   # override

    def y(self):
        return "y from C1"


# ساخت instance
i1 = C1()
i2 = C1()

print(i1.x)       # C1.x
print(i1.w())     # lookup → C3.w → call
print(i1.y())     # C1.y

# ----------bound method---------------
print('----------bound method---------------')
m = i1.w

print(m)            # bound method
print(m.__func__)   # <function C3.w>
print(m.__self__)   # i1

print('------------')
print(i1.w())
print(C3.w(i1))
