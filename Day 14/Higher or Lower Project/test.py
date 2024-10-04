from game_data import data
import random
dict_A = random.choice(data)
dict_B = random.choice(data)
score = 0
value = 0
final_score = 0


def continue_play():
    dict_A = dict_B
    dict_B = random.choice(data)
    print(f"Compare A: {dict_A['name']}, {dict_A['description']}, from {dict_A['country']}")
    print(vs)
    print(f"Compare B: {dict_B['name']}, {dict_B['description']}, from {dict_B['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")

base = "f"
self1=23
self2 =98
def nort():
    if base =="f":
        return self1
    else:
        return self2

def calc(function):
    result = function+10
    print(result)

nort()
calc(nort())