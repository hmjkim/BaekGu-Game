import random
from make_board_each_level import *
import time

def make_character():
    return {
        "Stat": {
            "HP": 100,
            "Level": 1,
            "Exp": 0,
            "Heart": 10,
            "Hunger": 10
        },
        "Skill": {
            "Basic Attack": random.randint(10, 30),
            "Level 1": {"Bark": random.randint(20, 50)},
            "Level 2": {
                "Scratch": random.randint(20, 50),
                "Digging": random.randint(20, 50),
            },
            "Level 3": {
                "Tail Whip": random.randint(20, 50),
                "Bite": random.randint(20, 50),
            }
        },
        "Inventory": {}
    }


def make_character_location(grid):
    first_location = (1, 1)
    prev_cell_content = grid[first_location[0]][first_location[1]]
    grid[first_location[0]][first_location[1]] = '🐶'
    return first_location, prev_cell_content


def get_user_choice(character):
    types_input = ['1', '2', '3', '4']
    user_wanted_input = input("which do you want to do? ['1: Direction','2: Inventory','3: Stat','4: Sleep']")
    while user_wanted_input != '1':
        if user_wanted_input == '2':
            print(character['Inventory'])
            user_wanted_input = input("which do you want to do again? ['1: Direction','2: Inventory','3: Stat','4: Sleep']")
        if user_wanted_input == '3':
            print("stats = ", character['Stat'])
            print("skills = ", character['Skill'])
            user_wanted_input = input("which do you want to do again? ['1: Direction','2: Inventory','3: Stat','4: Sleep']")
        if user_wanted_input == '4':
            print("go to sleep for 15sec")
            time.sleep(15)
            user_wanted_input = input("which do you want to do again? ['1: Direction','2: Inventory','3: Stat','4: Sleep']")
        if user_wanted_input not in types_input:
            print("invalid input")
            user_wanted_input = input("which do you want to do again? ['1: Direction','2: Inventory','3: Stat','4: Sleep']")
    if user_wanted_input == '1':
        direction = ['w', 'a', 's', 'd', 'q']
        full_direction = ['North', 'West', 'South', 'East', 'Quit']
        for count, element in enumerate(direction):
            print("%s : %s." % (full_direction[count], element), end=' ')
        direction_input = input("\nenter the direction they wish to travel").lower()
        return direction_input


def game():
    """
    Drive the game.
    """
    grid = make_board_lv1()
    grid_lv2 = make_board_lv2()
    grid_lv3 = make_board_lv3()

    user_name = input("Hi, there! What's your name? : ")


    first_location, prev_cell_content = make_character_location(grid)
    character = make_character()

    achieved_goal_lv1 = False
    while not achieved_goal_lv1:
        display_grid(grid)
        direction = get_user_choice(character)
        if direction == 'q':
            print("end")
            achieved_goal_lv1 = True



def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
