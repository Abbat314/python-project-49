import random


GAME_RULE = 'Answer "yes" if given number is prime. ' \
            'Otherwise answer "no".'


def get_game():
    number = random.randint(1, 1000)
    if is_prime(number):
        correct_answer = 'yes'
        return str(number), correct_answer
    else:
        correct_answer = 'no'
        return str(number), correct_answer


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            continue
    else:
        return True
