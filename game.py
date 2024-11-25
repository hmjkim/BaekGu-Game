import random
from make_board_each_level import *
import time


def make_character():
    skill_set = {
        "Level 1": {
            "Bark": random.randint(20, 50),
        },
        "Level 2": {
            "Scratch": random.randint(20, 50),
            "Digging": random.randint(20, 50),
        },
        "Level 3": {
            "Tail Whip": random.randint(20, 50),
            "Bite": random.randint(20, 50),
        }
    }
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
            "Current Skills": skill_set["Level 1"],
            "Skill Set": skill_set
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
            character['Stat']['Hunger'] = 10
            character['Stat']['HP'] = 100
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
        while direction_input not in direction:
            print('again1')
            direction_input = input("enter the direction they wish to travel").lower()
        return direction_input


def move_character_valid_move(grid, position, direction, prev_cell_content, character):
    row, col = position
    new_row, new_col = row, col

    if direction == 'w':
        new_row -= 1
    elif direction == 's':
        new_row += 1
    elif direction == 'a':
        new_col -= 1
    elif direction == 'd':
        new_col += 1
    else:
        print("Invalid input.")

    if grid[new_row][new_col] != '#':
        grid[row][col] = prev_cell_content
        new_prev_cell_content = grid[new_row][new_col]
        grid[new_row][new_col] = '🐶'
        character["Stat"]["Hunger"] -= 1
        return (new_row, new_col), new_prev_cell_content, character
    else:
        print("can't move this way")
        return (row, col), prev_cell_content, character




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
        (new_row, new_col), prev_cell_content, character = move_character_valid_move(grid, first_location, direction, prev_cell_content, character)
        first_location = (new_row, new_col)



def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
