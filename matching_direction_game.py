import random
import time
from itertools import count

from game import make_character


def check_character_level_matching_game(character):
    if character['Stat']['Level'] == 1:
        matching_count = 5
        return matching_count
    if character['Stat']['Level'] == 2:
        matching_count = 7
        return matching_count
    else:
        matching_count = 9
        return matching_count



def play_game(level, character):
    #explain
    direction_list = ['A', 'D', 'S', 'W']
    strings = random.choices(direction_list, k=level)
    print("memorize this direiton:")
    print(strings)

    time.sleep(1)
    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print("Enter the answer")
    user_inputs = [input(f"{i+1} direction: ") for i in range(len(strings))]
    upper_inputs = [i.upper() for i in user_inputs]
    if upper_inputs == strings:
        print("correct")
        return True, character
    else:
        print("wrong")
        print("answer is ", strings)
        character['Stat']['Heart'] -= 1
        return False, character


def main():
    character = make_character()
    level_matching_game = check_character_level_matching_game(character)
    check, character = play_game(level_matching_game, character)
    print(check, character)


if __name__ == "__main__":
    main()

