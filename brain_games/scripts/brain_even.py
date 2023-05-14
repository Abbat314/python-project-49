#!/usr/bin/env python3
import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    get_game(name)

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def get_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for t in range(3):
        number = random.randint(0, 100)
        correct = is_correct_answer(number)    
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if(answer == correct): 
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct}\'.')
            print(f'Let\'s try again, {name}!')
            break

def is_correct_answer(number):
    if(is_even(number)):
        return 'yes'
    if(not is_even(number)):
        return 'no'

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()