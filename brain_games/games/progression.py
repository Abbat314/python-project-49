import random


GAME_RULE = 'What number is missing ' \
            'in the progression?'


def get_question_and_right_answer():
    progression = generation_progression()
    index_cut_number = random.choice(range(0, 10))
    correct_answer = progression[index_cut_number]
    question = ''
    for i in progression:
        if i == correct_answer:
            question += '.. '
        else:
            question += str(i) + ' '
    return question, correct_answer


def generation_progression():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(7, 20)
    progression = []
    for i in range(1, 11):
        num_1 += num_2
        progression.append(num_1)
    return progression
