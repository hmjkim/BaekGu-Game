import random
from make_board_each_level import *
import time


def check_probability(rate):
    return random.random() <= rate


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
            "HP": 500,
            "Current HP": 100,
            "Level": 1,
            "Exp": 1500,
            #나중에 바꾸끼
            "Heart": 10,
            "Hunger": 100
            #나중에 바꾸끼

        },
        "Skill": {
            "Basic Attack": random.randint(10, 30),
            "Current Skills": skill_set["Level 1"],
            "Skill Set": skill_set
        },
        "Inventory": {"key": 2}
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
            for i in range(15):
                time.sleep(1)
                print("%d sec" % i)
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
        direction_input = input("\nenter the direction they wish to travel\n").lower()
        while direction_input not in direction:
            print('again1')
            direction_input = input("\nenter the direction they wish to travel\n").lower()
        return direction_input, character


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


def check_character_hunger(character):
    if character["Stat"]['Hunger'] == 0:
        print("force to sleep for 30sec")
        for i in range(1, 31):
            time.sleep(1)
            print("%d sec" % i)
        character["Stat"]["Hunger"] = 10
        character["Stat"]["HP"] = 100
        return character


def check_character_1_level_location_exp(first_location, character):
    if first_location == (7, 1) and character['Inventory']['key'] > 1 and character['Stat']['Level'] == 1 and character['Stat']['Exp'] >= 1000 :
        print('1렙 claer! 1렙 up 다음 2렙 맵으로 move')
        return True


def check_character_2_level_location_exp(first_location, character):
    if first_location == (4, 8) and character['Inventory']['key'] > 1 and character['Stat']['Level'] == 2 and character['Stat']['Exp'] >= 1500 :
        print('2렙 claer! 1렙 up 다음 3렙 맵으로 move')
        return True


def check_character_3_level_location_for_final(first_location, character):
    if first_location == (4, 4) and character['Stat']['Level'] == 3:
        print('마지막 보스를 만나러 갑니다 화이팅!')
        print("bosee")
        return True


def game():
    """
    Drive the game.
    """
    grid = make_board_lv1()
    user_name = input("Hi, there! What's your name? : ")

    first_location, prev_cell_content = make_character_location(grid)
    character = make_character()

    achieved_goal_lv1 = False
    while not achieved_goal_lv1:
        display_grid(grid)

        if character["Stat"]['Hunger'] == 1:
            print('alert!!!!!!!!!!!!!!!!!!!! your hunger is now 1! u must sleep now')

        direction, character = get_user_choice(character)
        if direction == 'q':
            print("end")
            achieved_goal_lv1 = True
        (new_row, new_col), prev_cell_content, character = move_character_valid_move(grid, first_location, direction, prev_cell_content, character)
        first_location = (new_row, new_col)
        check_character_hunger(character)
        there_is_a_challenger = check_probability(0.5)
        if there_is_a_challenger:
            gamelist = ['battle', 'hangman', 'memory game']
            print(random.choice(gamelist))
            # gamelist에 게임함수들 불러와서 넣고 게임 이기면 보상받고, charater return.

        if check_character_1_level_location_exp(first_location, character):
            grid = make_board_lv2()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] = 150
            character['Stat']['Level'] = 2
            character['Stat']['Exp'] = 1500
            # 나중에 Exp = 0으로
            character['Stat']['Hunger'] = 100
            character['Skill'] = {"Basic Attack": random.randint(10, 30),
                                  "Level1": {"Bark": random.randint(20, 50)},
                                  "Level2": {
                                      "Scratch": random.randint(20, 50),
                                      "Digging": random.randint(20, 50),
                                  }}
        if check_character_2_level_location_exp(first_location, character):
            grid = make_board_lv3()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] = 200
            character['Stat']['Level'] = 3
            character['Stat']['Exp'] = 0
            character['Stat']['Hunger'] = 100
            character['Skill'] = {"Basic Attack": random.randint(10, 30),
                                  "Level1": {"Bark": random.randint(20, 50)},
                                  "Level2": {
                                      "Scratch": random.randint(20, 50),
                                      "Digging": random.randint(20, 50),
                                  }, "Level 3": {"Tail Whip": random.randint(20, 50), "Bite": random.randint(20, 50)}}

        if check_character_3_level_location_for_final(first_location, character):
            print("game clear! good job!")
            break


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
