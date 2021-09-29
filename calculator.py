"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("Enter your equation > ").rstrip()
    tokens = user_input.split(" ")
    for i in range(1,len(tokens)):
        print(tokens[i])
        tokens[i] = float(tokens[i])
    for token in tokens:
        print(f"in for loop {type(token)}")
    if tokens[0] == "q":
        break
    elif tokens[0] == '+':
        print(add(tokens[1],tokens[2]))
    elif tokens[0] == '-':
        print(subtract(tokens[1],tokens[2]))
    elif tokens[0] == '*':
        print(multiply(tokens[1],tokens[2]))
    elif tokens[0] == '/':
        print(divide(tokens[1],tokens[2]))
    elif tokens[0] == 'square':
        print(square(tokens[1]))
    elif tokens[0] == 'cube':
        print(cube(tokens[1]))
    elif tokens[0] == 'pow':
        print(power(tokens[1],tokens[2]))
    elif tokens[0] == 'mod':
        print(mod(tokens[1],tokens[2]))
    else:
        print("in else")
  