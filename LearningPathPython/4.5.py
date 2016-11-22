#=================================
a,b = int(input("a = ")), int(input("b = "))
if a % b == 0 or b % a == 0:
    print('divisible')

#===============================
a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
if b != 0:
    print (a / b)

#==================================
name1 = input("Enter name 1")
name2 = input("Enter name 2")
name3 = input("Enter name 3")

if name1.lower() == name2.lower() and name1.lower() == name3.lower():
    print("equal")