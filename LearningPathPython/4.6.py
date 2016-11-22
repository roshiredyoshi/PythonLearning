import sys

line = input()
split = line.split()

if len(split) != 3:
    print("Wrong format")

left = int(split[0])
op = split[1]
right = int(split[2])

val = 0

if op == '+':
    val = left + right
elif op == '-':
    val = left - right
elif op == '*':
    val = left * right
elif op == '/':
    if right == 0:
        print("Division by Zero. Halting")
        sys.exit()
    val = left / right
else:
    print("Unknown operator: {operator}".format(operator=op))

print("{line_expr} = {value:.2f}".format(line_expr=line, value=val))