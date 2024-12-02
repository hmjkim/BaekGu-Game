import random
from make_board_each_level import *
import time
from hangman import *
from hangman_art import stages
from matching_direction_game import *
from battle import battle
from helpers import is_alive, display_skills, display_inventory, display_stats, get_item_choice


def configure_skills():
    return {
        "Level 1": {
            "Bark": {
                "Damage": random.randint(20, 30),
                "Description": "A loud bark that stuns the enemy"
            }
        },
        "Level 2": {
            "Scratch": {
                "Damage": random.randint(40, 50),
                "Description": "A swift paw swipe leaving deep marks"
            },
            "Digging": {
                "Damage": random.randint(40, 50),
                "Description": "Kick up dirt to blind the enemy"
            },
        },
        "Level 3": {
            "Tail Whip": {
                "Damage": random.randint(51, 60),
                "Description": "A powerful tail swing that knocks the enemy off balance"
            },
            "Bite": {
                "Damage": random.randint(51, 60),
                "Description": "A strong bite with a headshake"
            },
        }
    }


def go_to_sleep(character, total_time):
    print(f"\n💤 You are going to sleep for %d seconds to regain energy." % total_time)
    for count in range(1, total_time + 1):
        time.sleep(1)
        print("%d sec" % count)
    character['Stat']['Hunger'] = 10
    character['Stat']['Current HP'] = character['Stat']['HP']
    print("You feel well-rested! Your Hunger and HP have been fully restored.")


def make_character(skill_set):
    return {
        "Stat": {
            "HP": 250,
            "Current HP": 250,
            "Level": 1,
            "Exp": 0,
            "Max Exp": {
                "Level 1": 1000,
                "Level 2": 1300
            },
            "Heart": 10,
            "Max Heart": 10,
            "Hunger": 10,
            "Max Hunger": 10
        },
        "Skill": {
            "Basic Attack": random.randint(10, 30),
            "Current Skills": {
                **skill_set["Level 1"],
                **skill_set["Level 2"],
                **skill_set["Level 3"]
            }
        },
        "Inventory": {
            "Key": 1,
            "HP Potion": 3,
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

    # Main game loop to handle user choices
    while True:
        user_choice = input(
            "\nWhat would you like to do?\n"
            "--------------------------------------------------------\n"
            " 1: 🐕 Directions  - Move around\n"
            " 2: 🎒 Inventory   - Check your inventory\n"
            " 3: 📊 Stats       - View your current stats\n"
            " 4: ⚔️ Skills      - View your skills you have\n"
            " 5: 💤 Sleep       - Rest to regain energy\n"
            "--------------------------------------------------------\n"
            "Enter the number of your choice: "
        )

        if user_choice == '1':
            movement_keys = ['w', 'a', 's', 'd']
            movement_directions = ['North', 'West', 'South', 'East']
            print("\n🐕 Directions Available:")
            for count, element in enumerate(movement_keys):
                print(f"{element.upper()} : {movement_directions[count]}.")

            while True:
                direction_input = input("\nEnter the direction you wish to travel "
                                        f"({'/'.join(movement_keys).upper()}): ").lower()
                if direction_input in movement_keys:
                    return direction_input, character
                else:
                    print("❌ Invalid direction.")
        elif user_choice == '2':
            while True:
                display_inventory(character)
                have_break = get_item_choice(character)
                if have_break:
                    break
        elif user_choice == '3':
            display_stats(character)
        elif user_choice == '4':
            display_skills(character)
        elif user_choice == '5':
            go_to_sleep(character, 10)
        elif user_choice not in types_input:
            print("\n❌ Invalid input. Please enter a valid choice (1-4).")


def move_character_valid_move(grid, position, direction, prev_cell_content, character):
    row, col = position
    new_row, new_col = row, col
    valid_check = True

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
        return (new_row, new_col), new_prev_cell_content, character, valid_check
    else:
        print("can't move this way")
        valid_check = False
        return (row, col), prev_cell_content, character, valid_check


def check_character_hunger(character):
    if character["Stat"]['Hunger'] == 0:
        print("⚠️⚠️⚠️ Oops! You have run out of energy. It's a nap time, Baekgu ⚠️⚠️⚠️")
        go_to_sleep(character, 20)
    return character


def check_character_1_level_location_exp(first_location, character):
    if (first_location == (7, 1) and character['Inventory']['Key'] >= 1 and character['Stat']['Level'] == 1 and
            character['Stat']['Exp'] >= character['Max Exp']['Level 1']):
        # print('1렙 claer! 1렙 up 다음 2렙 맵으로 move')
        print("⬆️⬆️⬆️ Level UP ⬆️⬆️⬆️"
              "1st Level Clear! You are moving to Level 2.\n")
        return True


def check_character_2_level_location_exp(first_location, character):
    if (first_location == (4, 8) and character['Inventory']['Key'] >= 1 and character['Stat']['Level'] == 2 and
            character['Stat']['Exp'] >= character['Max Exp']['Level 2']) :
        # print('2렙 claer! 1렙 up 다음 3렙 맵으로 move')
        print("⬆️⬆️⬆️ Level UP ⬆️⬆️⬆️"
              "2nd Level Clear! You are moving to Level 3.\n")
        return True


def check_character_3_level_location_for_final(first_location, character):
    if first_location == (4, 4) and character['Stat']['Level'] == 3:
        print('You are going to fight the boss to save Haru. Good luck!')
        character, has_won = battle(character, True)
        return has_won


def check_probability(rate):
    return random.random() <= rate


def reward(character):
    exp = random.randint(200, 400)
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
    if check_probability(0.1):
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
        character['Stat']['Hunger'] += 1
    if check_probability(0.5):
        print('reward!4')
        print("you get 'key'")
        try:
            character['Inventory']['key'] += 1
        except KeyError:
            character['Inventory']['key'] = 1
    return character


def load_texts(file):
    try:
        with open(file, 'r') as file:
            texts = file.readlines()
        return [text.strip() for text in texts]
    except FileNotFoundError:
        print(f"Error: The file {file} was not found.")
        return []


def introduce_game(user_name):
    file_path = "intro.txt"
    texts = load_texts(file_path)
    if not texts:
        return
    print(f"Welcome to Baekgu, {user_name}!")
    time.sleep(1)
    for line in texts:
        print(line)
        time.sleep(3)

# def introduce_game(user_name):
#     print("Welcome to Baekgu, %s!" % user_name)
#     time.sleep(1)
#     print("You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond with your family."
#           "Life has always been happy, full of love and play, until today—something is terribly wrong.")
#     time.sleep(4)
#     print("Using your extraordinary sense of smell and intuition, you've realized that your family's little boy, Haru, "
#           "has suddenly gone missing.")
#     time.sleep(3)
#     print("Your mission is clear - Find Haru and bring him back home safely before it's too late.\n")
#     time.sleep(3)
#     print("Important Rules:")
#     time.sleep(2)
#     print('- Keep an eye on "Hunger" level. On every move, you will lose 1 Hunger and '
#           'need to “Sleep” to recharge your stamina before it runs out.')
#     time.sleep(3)
#     print('- You have 10 Hearts to start with.')
#     time.sleep(2)
#     print("- There are 3 maps to explore to reach your goal.")
#     time.sleep(3)
#     print('- You need to reach Level 3 and find the door marked with a "!" on the map.')
#     time.sleep(3)
#     print("- To level up, you'll need:")
#     time.sleep(2)
#     print("  - To stand in front of the door (!).")
#     time.sleep(2)
#     print("  - A key in your inventory to unlock the way.")
#     time.sleep(2)
#     print("  - Full Exp level (varies by level).\n")
#     time.sleep(3)
#     print("Your ultimate objective:")
#     time.sleep(2)
#     print("Defeat the boss who is holding Haru captive and bring him back home to your loving family!!!!!")
#     time.sleep(3)
#     print("Your journey may be filled with dangers, but with your sharp senses and loyalty, you are Haru's only hope.")
#     time.sleep(3)
#     print("Without further ado, let the rescue begin!")
#     time.sleep(2)
#     print("Time to save Haru, Baekgu!\n")


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

def describe_map_based_on_level(character):
    if character['Stat']['Level'] == 1:
        print("🕸️ UNDERGROUND - THE GARAGE 🕸️\n"
              "A dark space is filled with stacked boxes, tools, and the smell of dust. It is dead quiet, \n"
              "but you know you are not alone. You can sense some sneaky creatures watching your every move.")
    elif character['Stat']['Level'] == 2:
        print("🏠 GROUND FLOOR - LIVING ROOM 🏠\n"
              "The once lively living room now feels quiet. Stay alert for obstacles that will try to keep you away.")
    else:
        print("🚪 UPPER FLOOR - THE ATTIC 🚪\n"
              "The attic is filled with forgotten toys and old memories. Someone seems to be standing guard,\n"
              "ready to protect these treasures. Proceed with caution.")

def game():
    """
    Drive the game.
    """
    grid = make_board_lv1()
    user_name = input("Hi, there! What's your name? : ")

    if not check_user(user_name):
        introduce_game(user_name)

    first_location, prev_cell_content = make_character_location(grid)
    skill_set = configure_skills()
    character = make_character(skill_set)

    describe_map_based_on_level(character)
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        display_grid(grid)

        if character["Stat"]['Hunger'] == 1:
            print('🚨🚨🚨You only have 1 Hunger! You must sleep now.🚨🚨🚨')

        direction, character = get_user_choice(character)
        (new_row, new_col), prev_cell_content, character, valid_checking = move_character_valid_move(grid, first_location, direction, prev_cell_content, character)
        first_location = (new_row, new_col)
        if not valid_checking:
            continue
        check_character_hunger(character)
        there_is_a_challenger = check_probability(1)
        if there_is_a_challenger:
            # game_list = ['battle', 'hangman', 'memory game']
            game_list = ['battle']
            challenge = random.choice(game_list)
            if challenge == 'battle':
                print("You are going to battle! Prepare yourself.")
                character, has_won = battle(character)
                # print(has_won, character)
                if has_won:
                    reward(character)
            elif challenge == 'hangman':
                print("play hangman")
                level = check_character_level_hangman(character)
                has_won, j = hangman(level, character)
                print(has_won, j)
                if has_won:
                    print("you win")
                    print("get reward")
                    reward(character)
                else:
                    print("continue game")
            elif challenge == 'memory game':
                print("play memory game")
                level_matching_game = check_character_level_matching_game(character)
                check, character = play_game(level_matching_game, character)
                print(check, character)
                if check:
                    print("you win")
                    print("get reward")
                    reward(character)
                else:
                    print("continue game")

        goal_lv1 = check_character_1_level_location_exp(first_location, character)
        if goal_lv1:
            grid = make_board_lv2()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] += 200
            character['Stat']['Current HP'] = character['Stat']['HP']
            character['Stat']['Level'] = 2
            character['Stat']['Exp'] = 0
            character['Stat']['Hunger'] = 10
            character['Skill']['Current Skills'].update(skill_set['Level 2'])
            # character['Skill'] = {
            #     "Basic Attack": random.randint(10, 30),
            #     "Current Skills": {
            #             "Bark": random.randint(20, 50),
            #             "Scratch": random.randint(20, 50),
            #             "Digging": random.randint(20, 50)}}
            print(f"Your maximum HP has been increased by 200. "
                  f"You earned two new skills({','.join(skill_set['Level 2'].keys())}). (max HP +200)")
            describe_map_based_on_level(character)


        goal_lv2 = check_character_2_level_location_exp(first_location, character)
        if goal_lv2:
            grid = make_board_lv3()
            first_location, prev_cell_content = make_character_location(grid)
            character['Stat']['HP'] += 250
            character['Stat']['Current HP'] = character['Stat']['HP']
            character['Stat']['Level'] = 3
            character['Stat']['Exp'] = 0
            character['Stat']['Hunger'] = 10
            character['Skill']['Current Skills'].update(skill_set['Level 3'])
            # character['Skill'] = {
            #     "Basic Attack": random.randint(10, 30),
            #     "Current Skills": {
            #         "Bark": random.randint(20, 50),
            #         "Scratch": random.randint(20, 50),
            #         "Digging": random.randint(20, 50),
            #         "Tail Whip": random.randint(20, 50),
            #         "Bite": random.randint(20, 50)}}
            print(f"Your maximum HP has been increased by 250. "
                  f"You earned two new skills({','.join(skill_set['Level 3'].keys())}). (max HP +250)")
            # print("당신의 hp 200상승, level up, skill을 얻으셧습니다(Tail whip, bite)")
            describe_map_based_on_level(character)
        final_goal = check_character_3_level_location_for_final(first_location, character)
        if final_goal:
            print("🎉 Victory! You defeated the boss, but soon realized it was all a misunderstanding "
                  "with Majestic Fluffy BunBun. With Haru safe, it's time to return home.")
            achieved_goal = True
        else:
            print("😞 Oh no! You weren't strong enough to defeat the boss this time. Train harder and grow stronger! "
                  "Returning to checkpoint - the start of Level 3. Keep going, you can do this!")
            grid = make_board_lv3()
            first_location, prev_cell_content = make_character_location(grid)

    if achieved_goal:
        print("Congratulations! You made it home safely with Haru. Your pawrents and Haru shower you with "
              "love and kisses. Great job, hero! 🐾")
    else:
        print("Game over! You have lost all your Hearts. Try again and show your courage once more!")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
