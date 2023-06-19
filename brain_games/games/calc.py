from random import choice, randint
from operator import sub, mul, add


GAME_RULE = 'What is the result of the expression?'


def get_question_and_right_answer():
    num_1 = randint(10, 50)
    op = choice(['-', '+', '*'])
    num_2 = randint(1, 10)
    question = f"{num_1} {op} {num_2}"
    correct_answer = calculate_expression(num_1, num_2, op)
    return question, correct_answer


def calculate_expression(num_1, num_2, op):
    if op == '-':
        return sub(num_1, num_2)
    elif op == '+':
        return add(num_1, num_2)
    elif op == '*':
        return mul(num_1, num_2)
