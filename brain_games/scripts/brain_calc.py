#!/usr/bin/env python3
import prompt
from random import choice, randint
from operator import add, sub, mul
import re


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    get_game(name)

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def get_game(name):
    print('What is the result of the expression?')

    for t in range(3):
        num_1 = randint(10, 25)
        op = choice(['-', '+', '*'])
        num_2 = randint(1, 10)
        correct_answer = calculate_expression(num_1, num_2, op)
        print(f'Question: ' + str(num_1) + ' ' + str(op) + ' ' + str(num_2))
        answer = prompt.string('Your answer: ')
        if not re.match(r"^\d+$", answer):
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            break
        if (int(answer) == correct_answer): 
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            break



def calculate_expression(num_1, num_2, op):
    if op == '-':
        return sub(num_1, num_2)
    elif op == '+':
        return add(num_1, num_2)
    elif op == '*':
        return mul(num_1, num_2)
    

if __name__ == '__main__':
    main()
