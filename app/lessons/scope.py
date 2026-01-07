# /home/majid/Python/python_master_project/app/lessons/scope.py

var = 99

def local():
    var = 0

def glob1():
    global var
    var += 1

def glob2():
    var = 0
    import scope
    scope.var += 1

def glob3():
    var = 0
    import sys
    thismod = sys.modules[__name__]
    thismod.var += 1

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)


x = 'global'

def outer():
    x = 'enclosing'
    def inner():
        x = 'local'
        print(x)
    inner()

outer()


if __name__ == "__main__":
    test()
