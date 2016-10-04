X = 11

def g1():
    print(X)

def g2():
    global X
    X = 22

def h1():
    X = 33
    def nested():
        print(X)

def h2():
    X = 33
    def nested():
        nonlocal X
        X = 44

if __name__ == '__main__':
    print("This is the base variable")
    print(X)
    print("This is g1()")
    g1()
    print("This is g2()")
    g2()
    print(X)
    print("This is h1()")
    h1()
    print(X)
    print("This is h2()")
    h2()
