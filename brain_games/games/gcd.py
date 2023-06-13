import math
import random


GAME_RULE = 'Find the greatest common ' \
            'divisor of given numbers.'


def get_game():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    question = str(num_1) + ' ' + str(num_2)
    correct_answer = math.gcd(num_1, num_2)
    return question, correct_answer
