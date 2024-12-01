import random
from make_board_each_level import *
import time
from hangman import *
from hangman_art import stages
from battle import battle
from matching_direction_game import *
from helpers import is_alive


def make_character():
    return {
        "Stat": {
            "HP": 250,
            "Current HP": 250,
            "Level": 1,
            "Exp": 0,
            "Heart": 10,
            "Hunger": 10
        },
        "Skill": {
            "Basic Attack": random.randint(10, 30),
            "Current Skills": {
                "Bark": random.randint(20, 50)
            }
        },
        "Inventory": {
            "key": 0,
            "HP Potion": 0,
            "Kibble": 0
        }
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
                # if use not in character['Inventory'].keys():
                #     print("invalid input, try again")
                #     continue
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
            print("go to sleep for 10sec")
            for i in range(1,11):
                time.sleep(1)
                print("%d sec" % i)
            character['Stat']['Hunger'] = 10
            character['Stat']['Current HP'] = character['Stat']['HP']
            user_wanted_input = input("which do you want to do again? ['1: Direction','2: Inventory','3: Stat','4: Sleep']")
        if user_wanted_input not in types_input:
            print("invalid input")
            user_wanted_input = input("which do you want to do again? ['1: Direction','2: Inventory','3: Stat','4: Sleep']")
    if user_wanted_input == '1':
        direction = ['w', 'a', 's', 'd']
        full_direction = ['North', 'West', 'South', 'East']
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
    vaild_checking = True

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
        return (new_row, new_col), new_prev_cell_content, character, vaild_checking
    else:
        print("can't move this way")
        vaild_checking = False
        return (row, col), prev_cell_content, character, vaild_checking


def check_character_hunger(character):
    if character["Stat"]['Hunger'] == 0:
        print("force to sleep for 20sec")
        for i in range(1, 21):
            time.sleep(1)
            print("%d sec" % i)
        character["Stat"]["Hunger"] = 10
        character["Stat"]["HP"] = 100
        return character


def check_character_1_level_location_exp(first_location, character):
    if first_location == (7, 1) and character['Inventory']['key'] >= 1 and character['Stat']['Level'] == 1 and character['Stat']['Exp'] >= 1000 :
        print('1렙 claer! 1렙 up 다음 2렙 맵으로 move')
        return True


def check_character_2_level_location_exp(first_location, character):
    if first_location == (4, 8) and character['Inventory']['key'] >= 1 and character['Stat']['Level'] == 2 and character['Stat']['Exp'] >= 1300 :
        print('2렙 claer! 1렙 up 다음 3렙 맵으로 move')
        return True


def check_character_3_level_location_for_final(first_location, character):
    if first_location == (4, 4) and character['Stat']['Level'] == 3:
        print('마지막 보스를 만나러 갑니다 화이팅!')
        i, j = battle(character, True)
        if j:
            print("you win")
            return True
        else:
            print("you lose")
            return False





def check_probability(rate):
    return random.random() <= rate


def reward(character, check_probability):
    exp = random.randint(200,400)
    character['Stat']['Exp'] += exp
    print("Exp +=", exp)
    if check_probability(0.1):
        print("reward!")
        print(" you get 'bone'")
        print(" it Increase basic attack damage  permanet +30")
        character['Skill']['Basic Attack'] += 30
    if check_probability(0.3):
        print("reward!")
        print(" you get 'HP Potion'")
        print("full hp when you use it")
        try:
            character['Inventory']['HP potion'] += 1
        except KeyError:
            character['Inventory']['HP potion'] = 1
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
        print(' increase hunger +1 now')
        #permanet로 채우는거 해줘
        character['Stat']['Hunger'] += 1
    if check_probability(0.5):
        print('reward!4')
        print("you get 'key'")
        try:
            character['Inventory']['key'] += 1
        except KeyError:
            character['Inventory']['key'] = 1
    return character


def introduce_game(user_name):
    print("Welcome to Baekgu, %s!" % user_name)
    time.sleep(1)
    print("You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond with your family."
          "Life has always been happy, full of love and play, until today—something is terribly wrong.")
    time.sleep(4)
    print("Using your extraordinary sense of smell and intuition, you've realized that your family's little boy, Haru, "
          "has suddenly gone missing.")
    time.sleep(3)
    print("Your mission is clear - Find Haru and bring him back home safely before it's too late.\n")
    time.sleep(3)
    print("Important Rules:")
    time.sleep(2)
    print('- Keep an eye on "Hunger" level. On every move, you will lose 1 Hunger and '
          'need to “Sleep” to recharge your stamina before it runs out.')
    time.sleep(3)
    print('- You have 10 Hearts to start with.')
    time.sleep(2)
    print("- There are 3 maps to explore to reach your goal.")
    time.sleep(3)
    print('- You need to reach Level 3 and find the door marked with a "!" on the map.')
    time.sleep(3)
    print("- To level up, you'll need:")
    time.sleep(2)
    print("  - To stand in front of the door (!).")
    time.sleep(2)
    print("  - A key in your inventory to unlock the way.")
    time.sleep(2)
    print("  - Full Exp level (varies by level).\n")
    time.sleep(3)
    print("Your ultimate objective:")
    time.sleep(2)
    print("Defeat the boss who is holding Haru captive and bring him back home to your loving family!!!!!")
    time.sleep(3)
    print("Your journey may be filled with dangers, but with your sharp senses and loyalty, you are Haru's only hope.")
    time.sleep(3)
    print("Without further ado, let the rescue begin!")
    time.sleep(2)
    print("Time to save Haru, Baekgu!\n")


def check_user(user_name):
    # try except when file doesn't exist
    try:
        with open("players.txt") as players:
            player_list = players.readlines()
    except FileNotFoundError:
        with open("players.txt", "w") as players:
            players.write(f'{user_name}')
            print("✅New user is created!")
            return False
    else:
        if f'{user_name}\n' in player_list or user_name in player_list:
            print("You're already a player! Welcome back, %s!" % user_name)
            return True
        else:
            print("✅New user is created!")
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
            print('🚨🚨🚨You only have 1 Hunger! You must sleep now.🚨🚨🚨')

        direction, character = get_user_choice(character)
        (new_row, new_col), prev_cell_content, character, valid_checking = move_character_valid_move(grid, first_location, direction, prev_cell_content, character)
        first_location = (new_row, new_col)
        if not valid_checking:
            continue
        check_character_hunger(character)
        there_is_a_challenger = check_probability(0.25)
        if there_is_a_challenger:
            gamelist = ['battle', 'hangman', 'memory game']
            a = random.choice(gamelist)
            if a == 'battle':
                print("play battle")
                character, i = battle(character)
                print(i, character)
                if i:
                    print("you win")
                    print("get reward")
                    reward(character, check_probability)
                else:
                    print("continue game")
            elif a == 'hangman':
                print("play hangman")
                level = check_character_level_hangman(character)
                i, j = hangman(level, stages, character)
                print(i, j)
                if i:
                    print("you win")
                    print("get reward")
                    reward(character, check_probability)
                else:
                    print("continue game")
            elif a == 'memory game':
                print("play memory game")
                level_matching_game = check_character_level_matching_game(character)
                check, character = play_game(level_matching_game, character)
                print(check, character)
                if check:
                    print("you win")
                    print("get reward")
                    reward(character, check_probability)
                else:
                    print("continue game")

        goal_lv1 = check_character_1_level_location_exp(first_location, character)
        if goal_lv1:
            grid = make_board_lv2()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] += 250
            character['Stat']['Current HP'] = character['Stat']['HP']
            character['Stat']['Level'] = 2
            character['Stat']['Exp'] = 0
            character['Stat']['Hunger'] = 10
            character['Skill'] = {
                "Basic Attack": random.randint(10, 30),
                "Current Skills": {
                        "Bark": random.randint(20, 50),
                        "Scratch": random.randint(20, 50),
                        "Digging": random.randint(20, 50)}}
            print("당신의 hp 200상승, level up, skill을 얻으셧습니다(scratch, digging)")

        goal_lv2 = check_character_2_level_location_exp(first_location, character)
        if goal_lv2:
            grid = make_board_lv3()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] += 250
            character['Stat']['Current HP'] = character['Stat']['HP']
            character['Stat']['Level'] = 3
            character['Stat']['Exp'] = 0
            character['Stat']['Hunger'] = 10
            character['Skill'] = {
                "Basic Attack": random.randint(10, 30),
                "Current Skills": {
                    "Bark": random.randint(20, 50),
                    "Scratch": random.randint(20, 50),
                    "Digging": random.randint(20, 50),
                    "Tail Whip": random.randint(20, 50),
                    "Bite": random.randint(20, 50)}}
            print("당신의 hp 200상승, level up, skill을 얻으셧습니다(Tail whip, bite)")
        final_goal = check_character_3_level_location_for_final(first_location, character)
        if final_goal:
            print("game clear! good job!")
            achieved_goal_lv1 = True
        elif final_goal is False:
            print('안녕 태초마을이야')
            grid = make_board_lv3()
            first_location, prev_cell_content = make_character_location(grid)

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
