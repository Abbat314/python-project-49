#!/usr/bin/env python3
import prompt
import math
import random
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
    for t in range(3):
        print('Find the greatest common divisor of given numbers.')
        num_1 = random.randint(1, 50)
        num_2 = random.randint(1, 50)
        correct_answer = math.gcd(num_1, num_2)
        print(f'Question: ' + str(num_1) + ' ' + str(num_2))
        answer = prompt.string('Your answer: ')
        if not re.match(r"^\d+$", answer):
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            break
        if int(answer) == correct_answer:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            break


if __name__ == '__main__':
    main()
