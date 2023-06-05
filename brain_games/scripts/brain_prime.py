#!/usr/bin/env python3
import prompt
import random


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
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        number = random.randint(1, 100)
        print(f'Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer(number):
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer(number)}\'.')
            print(f'Let\'s try again, {name}!')
            break


def correct_answer(number):
    if is_prime(number):
        return 'yes'
    else:
        return 'no'


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            continue
    else:
        return True


if __name__ == '__main__':
    main()
