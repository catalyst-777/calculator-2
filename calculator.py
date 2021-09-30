"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
from functools import reduce

while True:
    user_input = input("Enter your equation > ").rstrip()
    tokens = user_input.split(" ")
    for i in range(1,len(tokens)):
        tokens[i] = float(tokens[i])
    
      
    if tokens[0] not in ['+', '-', '*', '/','square','cube','pow','mod','q']:
        print("Please check for correct operator\n")
        continue

    if tokens[0] == "q":
        break
    elif tokens[0] == '+':
        result = reduce(add,tokens[1:])
    elif tokens[0] == '-':
        result = reduce(subtract,tokens[1:])
    elif tokens[0] == '*':
        result = reduce(multiply,tokens[1:])
    elif tokens[0] == '/':
        result = reduce(divide, tokens[1:])
    elif tokens[0] == 'square':
        result = square(tokens[1])
    elif tokens[0] == 'cube':
        result = cube(tokens[1])
    elif tokens[0] == 'pow':
        result = reduce(power, tokens[1:])
    elif tokens[0] == 'mod':
        result = reduce(mod, tokens[1:])
    else:
        print("Please enter a valid operator followed by the appropriate number of integers.")
    
    print(result)

  