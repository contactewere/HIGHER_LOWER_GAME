from art import logo, vs
from game_data import data
import random
print(logo)
score = 0
value = 0
flag = True
dict_B = random.choice(data)

def result():
    print(dict_A['follower_count'])
    print(dict_B['follower_count'])
    if answer == "a" and dict_A['follower_count']>dict_B['follower_count']:
        global score
        score += 1
        print(f"You are right! Current score is: {score}")
    elif answer=="b" and dict_A['follower_count']< dict_B['follower_count']:
        score += 1
        print(f"You are right! Current score is: {score}")
    else:
        print('Game Over')
        print(f'Final Score: {score}')
        global flag
        flag = False
while flag:
    dict_A = dict_B
    dict_B = random.choice(data)
    print(f"Compare A: {dict_A['name']}, a {dict_A['description']}, from {dict_A['country']}")
    print(vs)
    print(f"Against B: {dict_B['name']}, a {dict_B['description']}, from {dict_B['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    result()

