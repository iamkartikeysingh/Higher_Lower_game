from art import logo, vs
from game_data import data
import random
import os

print(logo)

game_over = False
score = 0
random_data_B = random.choice(data)

while not game_over:
    random_data_A = random_data_B
    print(f"Compare A: {random_data_A['name']}, a {random_data_A['description']}, from {random_data_A['country']}")
    print(vs)
    random_data_B = random.choice(data)
    print(f"Compare B: {random_data_B['name']}, a {random_data_B['description']}, from {random_data_B['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    os.system('cls')
    if choice == "a":
        if random_data_A["follower_count"] > random_data_B["follower_count"]:
            score += 1
            print(f"You are right! Your current score is: {score}")
        else:
            print(f"You Lost. Your score is: {score}")
            game_over = True

    if choice == "b":
        if random_data_B["follower_count"] > random_data_A["follower_count"]:
            score += 1
            print(f"You are right! Your current score is: {score}")
        else:
            print(f"You Lost. Your score is: {score}")
            game_over = True
