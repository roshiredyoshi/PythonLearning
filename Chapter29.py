class SharedData:
    spam = 42

x = SharedData()
y = SharedData()
print(x.spam, y.spam)
