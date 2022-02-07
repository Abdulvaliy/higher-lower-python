import random
from art import logo, vs
from game_data import data
import pyautogui
# from replit import clear

def format_data(account):
    """"Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """"Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
# Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    pyautogui.hotkey('ctrl', 'l')
    # clear()
    # print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score is {score}.")


# n=0
# a = data[n]['follower_count']
# print(a)
#
# b = data[n+1]['follower_count']
# print(b)
#
# is_game_end = False
# # while not is_game_end:
#
#
# user_input = (input("Who has more followers? Type 'a' or 'b' for your answer: ").lower()
#
# if b > a:
#     if user_input == "b":
#         a = b
#     else:
#         is_game_end = True
#         print("You lose")
# elif:
#   print("")
    # if user_input == 'b':
    #     if b > a:
    #         a = b
    #     else:
    #         is_game_end = True
    # elif user_input == 'a':
    #     if a > b:
    #         a = b
    #     else:
    #         is_game_end = True
    # else:
    #     print("Wrong input! Please check your answer.")
    # is_game_end = True