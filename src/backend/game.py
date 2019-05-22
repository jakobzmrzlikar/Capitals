import json
import random
from pprint import pprint

def load(mode):
    with open(mode + '.json', 'r') as f:
        return json.load(f)


def get_question(data, possible_answers=4):
    random_countries = random.sample(list(data), possible_answers)
    question = random_countries[0]
    answers = [data[country] for country in random_countries]
    random.shuffle(answers)
    return tuple([question, answers])
    

def guess(mode='data', possible_answers=4):
    data = load(mode)
    question = get_question(data, possible_answers)
    question_str = "What is the capital city of {}?".format(question[0])
    options_str = """
    Possible answers:
    1) {}
    2) {}
    3) {}
    4) {}
    """.format(*question[1])
    print(question_str)
    print(options_str)
    choice = input("Answer: ")
    while choice not in question[1]:
        print("Please choose one of the available options!")
        choice = input("Answer: ")
    if choice == data[question[0]]:
        print("You are correct!")
    else:
        print("You were wrong. The correct answer is {}.".format(data[question[0]]))

guess()
