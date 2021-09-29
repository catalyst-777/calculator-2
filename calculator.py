"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
from functools import reduce
while True:
    user_input = input("Enter your equation > ").rstrip()
    tokens = user_input.split(" ")
    for i in range(1,len(tokens)):
        print(tokens[i])
        #if type(tokens[i]) is not str:
        tokens[i] = float(tokens[i])
        #else:
        #   print("Must enter numbers after the operator\n")
        #   break
      
    if tokens[0] not in ['+', '-', '*', '/','square','cube','pow','mod','q']:
        print("Please check for correct operator\n")
        continue
    if tokens[0] == "q":
        break
    elif tokens[0] == '+':
        result = reduce(add,tokens[1:])
        print(f"running + = {result}")
        print(add(tokens[1],tokens[2]))
    elif tokens[0] == '-':
        print(subtract(tokens[1],tokens[2]))
    elif tokens[0] == '*':
        result = reduce(multiply,tokens[1:])
        print(f"running + = {result}")
        print(multiply(tokens[1],tokens[2]))
    elif tokens[0] == '/':
        print(divide(tokens[1],tokens[2]))
    elif tokens[0] == 'square':
        print(square(tokens[1]))
    elif tokens[0] == 'cube':
        result = reduce(cube,tokens[1:])
        print(f"running cube = {result}")
        print(cube(tokens[1]))
    elif tokens[0] == 'pow':
        print(power(tokens[1],tokens[2]))
    elif tokens[0] == 'mod':
        print(mod(tokens[1],tokens[2]))
    else:
        print("in else")
  