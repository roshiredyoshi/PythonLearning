# class SharedData:
#     spam = 42
#
# x = SharedData()
# y = SharedData()
# x.spam = 88
# print(x.spam, y.spam, SharedData.spam)
#
# class MixedNames:
#         data = 'spam'
#         def __init__(self, value):
#             self.data = value
#         def display(self):
#             print(self.data, MixedNames.data)
# x = MixedNames(1)
# y = MixedNames(2)
# x.display(), y.display()
#
# class NextClass:
#     def printer(self, text):
#         self.message = text
#         print(self.message)
# x = NextClass()
# x.printer('instance call')
#
# #Specializing Inherited Methods
# class Super:
#     def method(self):
#         print('in Super method')
#
# class Sub(Super):
#     def method(self):
#         print('starting Sub.method')
#         Super.method(self)
#         print('ending Sub.method')
#
# x = Super()
# x.method()
#
# x = Sub()
# x.method()
#
class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')
X = Super()
X.delegate()

class Sub(Super): pass

X = Sub()
X.delegate()
