X = 1
def nester():
    X = 2
    print(X)
    class C:
        print(X)
        def method1(self):
            X = 3
            print(X)
        def method2(self):
            X = 4
            print(X)

    I = C()
    I.method1()
    I.method2()

print(X)
nester()
print('-'*40)
