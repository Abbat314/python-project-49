import random


GAME_RULE = 'Answer "yes" if the number is even, ' \
            'otherwise answer "no".'


def get_question_and_right_answer():
    number = random.randint(0, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return str(number), correct_answer


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
