import random
from make_board_each_level import *
import time
from hangman import *
from hangman_art import stages


def make_character():
    return {
        "Stat": {
            "HP": 500,
            "Current HP": 500,
            "Level": 1,
            "Exp": 0,
            "Heart": 10,
            "Hunger": 10
        },
        "Skill": {
            "Basic Attack": random.randint(10, 30),
            "Current Skills": {
                "Bark": random.randint(20, 50),
                "Scratch": random.randint(20, 50),
                "Digging": random.randint(20, 50),
                "Tail Whip": random.randint(20, 50),
                "Bite": random.randint(20, 50),
            }
        },
        "Inventory": {"Kibble": 2, "HP potion": 4}
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
            while True:
                use = input("which do you want to use? %s, q:quit" % character['Inventory'].keys())
                if use not in character['Inventory'].keys():
                    print("invalid input, try again")
                    continue
                if use == 'Kibble':
                    character['Inventory']['Kibble'] -= 1
                    character['Stat']['Hunger'] += 1
                    print("you eat 'Kibble' and your hunger +1")
                    continue
                if use == "HP Potion":
                    character['Stat']['Current HP'] += character['Stat']['HP'] - character['Stat']['Current HP']
                    character['Stat']['HP'] = character['Stat']['Current HP']
                    print("you use 'HP Potion' and your HP +%d" % (character['Stat']['HP'] - character['Stat']['Current HP']))
                    continue
                if use == "q":
                    break
                else:
                    print("invalid input, try again")
                    use = input("which do you want to use again? %s" % character['Inventory'].keys())
                    continue
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
        #보스만나고 이기면 true, 지면 False로 return
        return True


def is_alive(character):
    alive = True
    if character['Stat']['Heart'] == 0:
        alive = False
    return alive


def check_probability(rate):
    return random.random() <= rate


def reward(character, check_probability):
    character['Stat']['Exp'] += random.randint(100,300)
    if check_probability(0.3):
        print("reward!")
        print(" you get 'bone'")
        print(" it Increase basic attack damage  permanet +30")
        character['Skill']['Basic Attack'] += 30
    if check_probability(0.3):
        print('reward!1')
        print("you get 'Paw boots'")
        print(' increase HP permanet +100')
        character['Stat']['HP'] += 100
    if check_probability(0.3):
        print('reward!2')
        print("you get 'Kibble'")
        print(' increase hunger +1 when you use it')
        try:
            character['Inventory']['Kibble'] += 1
        except KeyError:
            character['Inventory']['Kibble'] = 1
    if check_probability(0.3):
        print('reward!3')
        print("you get 'Bowl collar'")
        print(' increase hunger +1 permanent')
        character['Stat']['Hunger'] += 1
    if check_probability(0.3):
        print('reward!4')
        print("you get 'key'")
        try:
            character['Inventory']['key'] += 1
        except KeyError:
            character['Inventory']['key'] = 1
    return character


def introduce_game(user_name):
    print("Welcome to Baekgu, %s! You are a loyal white jindo dog named Baekgu living with a happy family. Your owner's little son, Haru, has suddenly disappeared for a couple hours" % user_name)
    print("explain game story")


def check_user(user_name):
    # try except when file doesn't exist
    try:
        with open("players.txt") as players:
            player_list = players.readlines()
    except FileNotFoundError:
        with open("players.txt", "w") as players:
            players.write(f'{user_name}')
            print("New user is created!")
            return False
    else:
        if f'{user_name}\n' in player_list or user_name in player_list:
            print("You're already a player! Welcome back, %s!" % user_name)
            return True
        else:
            print("New user is created!")
            with open("players.txt", "a") as players:
                players.write(f'\n{user_name}')
                return False


def game():
    """
    Drive the game.
    """
    grid = make_board_lv1()
    user_name = input("Hi, there! What's your name? : ")

    if not check_user(user_name):
        introduce_game(user_name)

    first_location, prev_cell_content = make_character_location(grid)
    character = make_character()

    achieved_goal_lv1 = False
    while is_alive(character) and not achieved_goal_lv1:
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
        there_is_a_challenger = check_probability(0.8)
        if there_is_a_challenger:
            gamelist = ['battle', 'hangman', 'memory game']
            a = random.choice(gamelist)
            if a == 'battle':
                print("play battle")
            elif a == 'hangman':
                print("play hangman")
                level = check_character_level(character)
                i, j = hangman(level, stages, character)
                print(i, j)
                if i:
                    print("you win")
                    print("get reward")
                    reward(character, check_probability)
                else:
                    print("continue game")
            # gamelist에 게임함수들 불러와서 넣고 게임 이기면 보상받고 아님 말고

        goal_lv1 = check_character_1_level_location_exp(first_location, character)
        if goal_lv1:
            grid = make_board_lv2()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] += 200
            character['Stat']['Current HP'] = character['Stat']['HP']
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
        goal_lv2 = check_character_2_level_location_exp(first_location, character)
        if goal_lv2:
            grid = make_board_lv3()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] += 200
            character['Stat']['Current HP'] = character['Stat']['HP']
            character['Stat']['Level'] = 3
            character['Stat']['Exp'] = 0
            character['Stat']['Hunger'] = 100
            character['Skill'] = {"Basic Attack": random.randint(10, 30),
                                  "Level1": {"Bark": random.randint(20, 50)},
                                  "Level2": {
                                      "Scratch": random.randint(20, 50),
                                      "Digging": random.randint(20, 50),
                                  },
                                  "Level 3": {"Tail Whip": random.randint(20, 50),
                                              "Bite": random.randint(20, 50)}}
        final_goal = check_character_3_level_location_for_final(first_location, character)
        if final_goal:
            print("game clear! good job!")
            achieved_goal_lv1 = True
        elif final_goal is False:
            print('안녕 태초마을이야')

    if achieved_goal_lv1:
        print('Congratulations! You have reached the goal.')
    else:
        print('Game over! You have lost all your HP.')


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
