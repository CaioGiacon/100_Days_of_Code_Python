import os 
from art import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    print(art)
    should_continue = True
    n1 = float(input('What\'s the first number?: '))

    while should_continue:
        print('+\n-\n*\n/')
        operation = (input('Pick an operation: '))
        n2 = float(input('What\'s the next number?: '))

        final_value = operations_dict[operation](n1, n2)
        print(f'{n1} {operation} {n2} = {final_value}')

        try_again = input(f'Type "y" to continue calculating with {final_value}, or type "n" to start a new calculation: ')
        if try_again == 'y':
            n1 = final_value
        else:
            should_continue = False
            os.system('cls')
            calculator()

calculator()