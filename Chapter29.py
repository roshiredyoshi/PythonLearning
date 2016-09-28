class SharedData:
    spam = 42

x = SharedData()
y = SharedData()
x.spam = 88
print(x.spam, y.spam, SharedData.spam)

class MixedNames:
        data = 'spam'
        def __init__(self, value):
            self.data = value
        def display(self):
            print(self.data, MixedNames.data)
x = MixedNames(1)
y = MixedNames(2)
x.display(), y.display()

class NextClass:
    def printer(self, text):
        self.message = text
        print(self.message)
x = NextClass()
x.printer('instance call')
x.message



#Hello
