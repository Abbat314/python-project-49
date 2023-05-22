#!/usr/bin/env python3
import prompt
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
        print('What number is missing in the progression?')
        progression = generation_progression()
        index_cut_number = random.choice(range(0, 9))
        correct_answer = progression[index_cut_number]
        question = ''
        for idx, num in enumerate(progression):
            if idx == index_cut_number:
                question += '.. '
            else:
                question += str(num) + ' '
        print(f'Question: ' + question)
        answer = prompt.string('Your answer: ')
        if not re.match(r"^\d+$", answer):
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            break
        if (int(answer) == correct_answer): 
            print('Correct!')
            if t == 2:
                print(f'Congratulations, ' + name + '!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            break


def generation_progression():
    num_1 = random.randint(0, 50)
    num_2 = random.randint(7, 20)
    progression = []
    for i in range(1, 11):
        num_1 += num_2
        progression.append(num_1)
    return progression


if __name__ == '__main__':
    main()
