import random


GAME_RULE = 'Answer "yes" if the number is even, ' \
            'otherwise answer "no".'


def get_game():
    number = random.randint(0, 100)
    if is_even(number):
        correct_answer = 'yes'
        return str(number), correct_answer
    else:
        correct_answer = 'no'
        return str(number), correct_answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
