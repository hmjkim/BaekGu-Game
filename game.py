from make_board_each_level import *
from minigames.hangman import *
from minigames.matching_direction_game import *
from minigames.battle import battle
from helpers import is_alive, display_skills, display_inventory, display_stats, get_item_choice


def configure_skills():
    """
    Configure skills for each character level, including skill name, damage, and description.

    Skill damage values are randomly assigned within the specified range.

    :postcondition: return a dictionary containing skill information for different character levels
    :return: a dictionary with keys as character levels and values as dictionaries of skills

    >>> from pprint import pprint
    >>> pprint(configure_skills()) # doctest: +SKIP
    {'Level 1': {'Bark': {'Damage': 25,
                          'Description': 'A loud bark that stuns the enemy'}},
     'Level 2': {'Digging': {'Damage': 40,
                             'Description': 'Kick up dirt to blind the enemy'},
                 'Scratch': {'Damage': 45,
                             'Description': 'A swift paw swipe leaving deep '
                                            'marks'}},
     'Level 3': {'Bite': {'Damage': 56,
                          'Description': 'A strong bite with a headshake'},
                 'Tail Whip': {'Damage': 57,
                               'Description': 'A powerful tail swing that knocks '
                                              'the enemy off balance'}}}
    """
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
    """
    Make the character sleep for the specified duration.

    Hunger level will be fully restored after.

    :param character: a well-formed character dictionary
    :param total_time: an integer representing the time in seconds
    :precondition: character must be a dictionary containing a key "Stat" that holds another dictionary with
    "Hunger" key and its value
    :precondition: total_time must be a positive integer greater than 0
    :postcondition: restore the player's Hunger level fully after sleeping for the given time

    >>> skill_set = configure_skills()
    >>> character_with_low_hunger = {"Stat": { "Hunger": 1, "Max Hunger": 10}}
    >>> go_to_sleep(character_with_low_hunger, 10)
    <BLANKLINE>
    💤 You are going to sleep for 10 second(s) to regain energy.
    1 sec
    2 sec
    3 sec
    4 sec
    5 sec
    6 sec
    7 sec
    8 sec
    9 sec
    10 sec
    You feel well-rested! Your Hunger has been fully restored.
    >>> print(character_with_low_hunger)
    {'Stat': {'Hunger': 10, 'Max Hunger': 10}}
    >>> character_with_full_hunger = {"Stat": { "Hunger": 10, "Max Hunger": 10}}
    >>> go_to_sleep(character_with_full_hunger, 1)
    <BLANKLINE>
    💤 You are going to sleep for 1 second(s) to regain energy.
    1 sec
    You feel well-rested! Your Hunger has been fully restored.
    >>> print(character_with_full_hunger)
    {'Stat': {'Hunger': 10, 'Max Hunger': 10}}
    """
    print(f"\n💤 You are going to sleep for %d second(s) to regain energy." % total_time)
    for count in range(1, total_time + 1):
        time.sleep(1)
        print("%d sec" % count)
    character['Stat']['Hunger'] = 10
    print("You feel well-rested! Your Hunger has been fully restored.")


def make_character(skill_set):
    """
    Create a character with initial stats, skills, and inventory.

    Basic stats include HP, Level, Exp, Hearts, and Hunger. The character is also equipped with basic and
    level-specific skills and an empty inventory.

    :param skill_set: a dictionary containing skills for different character levels
    :precondition: skill_set must be a dictionary with keys as character levels and values as dictionaries of skills
    :postcondition: create a character dictionary containing HP, level, exp, hearts, hunger, and skills
    with basic attack and Level 1 skills
    :return: a character dictionary with current stats, skills, and inventory as key-value pairs

    >>> from pprint import pprint
    >>> skills = configure_skills()
    >>> pprint(make_character(skills), sort_dicts=False) # doctest: +SKIP
    {'Stat': {'HP': 250,
              'Current HP': 250,
              'Level': 1,
              'Exp': 0,
              'Max Exp': {'Level 1': 1000, 'Level 2': 1300, 'Level 3': 1500},
              'Heart': 10,
              'Max Heart': 10,
              'Hunger': 10,
              'Max Hunger': 10},
     'Skill': {'Basic Attack': 28,
               'Current Skills': {'Bark': {'Damage': 25,
                                           'Description': 'A loud bark that stuns '
                                                          'the enemy'}}},
     'Inventory': {'Key': 0, 'HP Potion': 0, 'Kibble': 0}}

    """
    inventory_items = ['Key', 'HP Potion', 'Kibble']
    inventory = {item: 0 for item in inventory_items}

    return {
        "Stat": {
            "HP": 250,
            "Current HP": 250,
            "Level": 1,
            "Exp": 0,
            "Max Exp": {
                "Level 1": 1000,
                "Level 2": 1300,
                "Level 3": 1500
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
            }
        },
        "Inventory": inventory
        #     {
        #     "Key": 0,
        #     "HP Potion": 0,
        #     "Kibble": 0
        # }
    }


def make_character_location(grid):
    first_location = (1, 1)
    prev_cell_content = grid[first_location[0]][first_location[1]]
    grid[first_location[0]][first_location[1]] = '🐶'
    return first_location, prev_cell_content


def get_user_choice(character, grid):
    types_input = ['1', '2', '3', '4', '5', '6']

    # Main game loop to handle user choices
    while True:
        display_grid(grid)
        user_choice = input(
            "\nWhat would you like to do?\n"
            "--------------------------------------------------------\n"
            " 1: 🐕 Directions  - Move around\n"
            " 2: 🎒 Inventory   - Check your inventory\n"
            " 3: 📊 Stats       - View your current stats\n"
            " 4: ⚔️ Skills      - View your skills you have\n"
            " 5: 💤 Sleep       - Rest to regain energy\n"
            " 6: ℹ️ Help        - Read about How to play\n"
            "--------------------------------------------------------\n"
            "Enter the number of your choice: "
        )

        if user_choice == '1':
            movement_keys = ['w', 'a', 's', 'd']
            movement_directions = ['Up', 'Left', 'Down', 'Right']
            print("\n🐕 Directions Available:")
            for count, element in enumerate(movement_keys):
                print(f"{element.upper()} : {movement_directions[count]}")
            while True:
                direction_input = input("\nEnter the direction you wish to travel "
                                        f"({'/'.join(movement_keys).upper()}): ").strip().lower()
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
        elif user_choice == '6':
            for line in load_text('intro.txt'):
                print(line)
        elif user_choice not in types_input:
            print("❌ Invalid input. Please enter a valid choice (1-6).\n")


def move_character_valid_move(grid, position, direction, prev_cell_content, character):
    row, col = position
    new_row, new_col = row, col
    valid_check = True

    if direction == 'w':
        new_row -= 1
        print("You moved one step up. Everything seems quiet.")
    elif direction == 's':
        new_row += 1
        print("You moved one step down. Everything seems quiet.")
    elif direction == 'a':
        new_col -= 1
        print("You moved one step left. Everything seems quiet.")
    elif direction == 'd':
        new_col += 1
        print("You moved one step right. Everything seems quiet.")
    else:
        print("❌ Invalid input.")

    if grid[new_row][new_col] != '#':
        grid[row][col] = prev_cell_content
        new_prev_cell_content = grid[new_row][new_col]
        grid[new_row][new_col] = '🐶'
        character["Stat"]["Hunger"] -= 1
        return (new_row, new_col), new_prev_cell_content, character, valid_check
    else:
        print("❌ You can't move that way.")
        valid_check = False
        return (row, col), prev_cell_content, character, valid_check


def check_character_hunger(character: dict) -> dict:
    """
    Force the character to go to sleep when Hunger level reaches 0.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary containing a key "Stat" that holds another dictionary with a "Hunger"
    key and a "Max Hunger" key
    :precondition: character must have "Hunger" and "Max Hunger" values that are greater than or equal to 0
    :postcondition: make character sleep to restore their Hunger to the Max Hunger value when Hunger becomes 0
    :return: a character dictionary with updated Hunger level

    >>> starving_character = {"Stat": {"Hunger": 0, "Max Hunger": 10}}
    >>> check_character_hunger(starving_character) # doctest: +ELLIPSIS
    ⚠️⚠️⚠️ Oops! You have run out of energy. It's a nap time, Baekgu ⚠️⚠️⚠️
    <BLANKLINE>
    💤 You are going to sleep for 20 second(s) to regain energy.
    1 sec
    2 sec
    3 sec
    ...
    19 sec
    20 sec
    You feel well-rested! Your Hunger has been fully restored.
    {'Stat': {'Hunger': 10, 'Max Hunger': 10}}
    >>> less_hungry_character = {"Stat": {"Hunger": 2, "Max Hunger": 10}}
    >>> check_character_hunger(less_hungry_character)
    {'Stat': {'Hunger': 2, 'Max Hunger': 10}}
    >>> full_character = {"Stat": {"Hunger": 10, "Max Hunger": 10}}
    >>> check_character_hunger(full_character)
    {'Stat': {'Hunger': 10, 'Max Hunger': 10}}
    """
    if character["Stat"]['Hunger'] == 0:
        print("⚠️⚠️⚠️ Oops! You have run out of energy. It's a nap time, Baekgu ⚠️⚠️⚠️")
        go_to_sleep(character, 20)
    return character


def check_character_1_level_location_exp(first_location, character):
    if (first_location == (7, 1) and character['Inventory']['Key'] >= 1 and character['Stat']['Level'] == 1 and
            character['Stat']['Exp'] >= character['Stat']['Max Exp']['Level 1']):
        # print('1렙 claer! 1렙 up 다음 2렙 맵으로 move')
        print("⬆️⬆️⬆️ Level UP ⬆️⬆️⬆️\n"
              "1st Level clear! You are moving to Level 2.")
        return True


def check_character_2_level_location_exp(first_location, character):
    if (first_location == (4, 8) and character['Inventory']['Key'] >= 1 and character['Stat']['Level'] == 2 and
            character['Stat']['Exp'] >= character['Stat']['Max Exp']['Level 2']):
        # print('2렙 claer! 1렙 up 다음 3렙 맵으로 move')
        print("⬆️⬆️⬆️ Level UP ⬆️⬆️⬆️\n"
              "2nd Level clear! You are moving to Level 3.")
        return True


def check_character_3_level_location_for_final(first_location, character):
    if first_location == (4, 4) and character['Stat']['Level'] == 3 and character['Stat']['Exp'] >= \
            character['Stat']['Max Exp']['Level 3']:
        print('You are going to fight the boss to save Haru. Good luck!')
        character, has_won = battle(character, True)
        return has_won


def check_probability(rate):
    """
    Check if an event occurs based on a given rate.

    :param rate: a floating point number
    :precondition: rate must be a floating point number between 0.0 and 1.0 inclusive
    :postcondition: determine whether the event occurs based on the given rate
    :return: a boolean that is True if the event occurs based on the specified probability

    >>> check_probability(0.5) # doctest: +SKIP
    True
    >>> check_probability(0) # doctest: +SKIP
    False
    >>> check_probability(1) # doctest: +SKIP
    True
    """
    return random.random() <= rate


def get_reward(character):
    exp = random.randint(200, 400)
    character['Stat']['Exp'] += exp
    max_exp = character['Stat']['Max Exp']['Level 1'] if character['Stat']['Level'] == 1 else (
        character)['Stat']['Max Exp']['Level 2']
    print("🏆 Reward Earned 🏆\n"
          f"{' - Exp +%d':<20}({character['Stat']['Exp']}/{max_exp})" % exp)
    if check_probability(0.1):
        print(f"{' - Bone +1':<20} Permanently increases Basic Attack damage by +30")
        character['Skill']['Basic Attack'] += 30
    if check_probability(0.3):
        print(f"{' - HP Potion +1':<20} Fully restores current HP (saved to inventory)")
        try:
            character['Inventory']['HP Potion'] += 1
        except KeyError:
            character['Inventory']['HP Potion'] = 1
    if check_probability(0.1):
        print(f"{' - Paw Boots +1':<20} Permanently increases maximum HP by +100")
        character['Stat']['HP'] += 100
    if check_probability(0.3):
        print(f"{' - Kibble +1':<20} Increases Hunger by +1 (saved to inventory)")
        try:
            character['Inventory']['Kibble'] += 1
        except KeyError:
            character['Inventory']['Kibble'] = 1
    if check_probability(0.3):
        print(f"{' - Bowl Collar':<20} Increases Hunger by +1 now")
        character['Stat']['Hunger'] += 1
    if check_probability(0.5):
        print(f"{' - Key +1':<20} Used to move to the next level (saved to inventory)")
        try:
            character['Inventory']['Key'] += 1
        except KeyError:
            character['Inventory']['Key'] = 1
    return character


def load_text(file: str) -> list:
    """
    Load a list of lines of text read from a text file.

    Whitespaces at the end of each line will be removed.

    :param file: a string representing a path to a text file
    :precondition: file must be a valid path to a text file containing Unicode characters or an empty file
    :postcondition: return a list of strings representing each line of text, with trailing whitespaces removed
    :return: a list of strings or an empty list if invalid file path

    >>> content = load_text('intro.txt')
    >>> content[:4] # doctest: +NORMALIZE_WHITESPACE
    ['You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond with your family.',
    'Life has always been happy, full of love and play, until today—something is terribly wrong.',
    "Using your extraordinary sense of smell and intuition, you've realized that your family's little boy, Haru, has
    suddenly gone missing.", "Your mission is clear - Find Haru and bring him back home safely before it's too late."]
    >>> load_text('')
    Error: The file  was not found.
    []
    """
    try:
        with open(file, 'r') as file:
            texts = file.readlines()
        return [text.rstrip() for text in texts]
    except FileNotFoundError:
        print(f"Error: The file {file} was not found.")
        return []


def introduce_game(user_name):
    """
    Provide an introduction to the game, including a personalized greeting and how-to-play instructions.

    Each line of text will be displayed with a delay to give the player time to follow along.

    :param user_name: a string representing a player's name
    :precondition: user_name must be a non-empty string registered in the game
    :postcondition: print an introductory story with a personalized greeting and explaination on how to play the game

    >>> introduce_game('Heather') # doctest: +ELLIPSIS
    Welcome to Baekgu, Heather!
    You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond with your family.
    Life has always been happy, full of love and play, until today—something is terribly wrong.
    ...
    Time to save Haru, Baekgu!
    >>> introduce_game('Young Bin') # doctest: +ELLIPSIS
    Welcome to Baekgu, Young Bin!
    You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond with your family.
    Life has always been happy, full of love and play, until today—something is terribly wrong.
    ...
    Time to save Haru, Baekgu!
    >>> introduce_game('   ') # doctest: +ELLIPSIS
    Welcome to Baekgu,    !
    You are Baekgu, a loyal white Jindo dog with a brave heart and a strong bond with your family.
    Life has always been happy, full of love and play, until today—something is terribly wrong.
    ...
    Time to save Haru, Baekgu!
    """
    file_path = "intro.txt"
    texts = load_text(file_path)
    if not texts:
        return
    print(f"Welcome to Baekgu, {user_name}!")
    time.sleep(1)
    for line in texts:
        print(line)
        time.sleep(3)


def check_user(user_name):
    """
    Check if a user is registered in the game.

    If the user is not found in the players list, they are added to the list. If the user already exists, they are
    notified as a returning player.

    :param user_name: a string representing a player's name
    :precondition: user_name must be a non-empty string
    :postcondition: add the name of the new user to a file
    :postcondition: print an informative message if the user is already registered
    :return: a boolean indicating if the user is a returning player (True) or a new player (False)

    >>> check_user('Heather')
    You're already a player! Welcome back, Heather!
    True
    >>> check_user('Young Bin') # doctest: +SKIP
    ✅ New user is created!
    False
    >>> check_user('     ')
    You're already a player! Welcome back,      !
    True
    """
    try:
        with open("players.txt") as players:
            player_list = players.readlines()
    except FileNotFoundError:
        with open("players.txt", "w") as players:
            players.write(f'{user_name}')
            print("✅ New user is created!")
            return False
    else:
        if f'{user_name}\n' in player_list or user_name in player_list:
            print("You're already a player! Welcome back, %s!" % user_name)
            return True
        else:
            print("✅ New user is created!")
            with open("players.txt", "a") as players:
                players.write(f'\n{user_name}')
                return False


def describe_map_based_on_level(character):
    """
    Display a description of the current map based on the character's level.

    :param character: a well-formed character dictionary
    :precondition: character must be a dictionary containing a "Level" key representing the current character level
    :postcondition: print a map description based on the current character's level

    >>> level_1_character = {"Stat": { "Level": 1}}
    >>> describe_map_based_on_level(level_1_character) # doctest: +NORMALIZE_WHITESPACE
    🕸️ UNDERGROUND - THE GARAGE 🕸️
    A dark space is filled with stacked boxes, tools, and the smell of dust. It is dead quiet,
    but you know you are not alone. You can sense some sneaky creatures watching your every move.
    >>> level_2_character = {"Stat": { "Level": 2}}
    >>> describe_map_based_on_level(level_2_character) # doctest: +NORMALIZE_WHITESPACE
    🏠 GROUND FLOOR - LIVING ROOM 🏠
    The once lively living room now feels quiet. Stay alert for obstacles that will try to keep you away.
    >>> level_3_character = {"Stat": { "Level": 3}}
    >>> describe_map_based_on_level(level_3_character) # doctest: +NORMALIZE_WHITESPACE
    🚪 UPPER FLOOR - THE ATTIC 🚪
    The attic is filled with forgotten toys and old memories. Someone seems to be standing guard,
    ready to protect these treasures. Proceed with caution.
    """
    if character['Stat']['Level'] == 1:
        print("\n🕸️ UNDERGROUND - THE GARAGE 🕸️\n"
              "A dark space is filled with stacked boxes, tools, and the smell of dust. It is dead quiet, \n"
              "but you know you are not alone. You can sense some sneaky creatures watching your every move.")
    elif character['Stat']['Level'] == 2:
        print("\n🏠 GROUND FLOOR - LIVING ROOM 🏠\n"
              "The once lively living room now feels quiet. Stay alert for obstacles that will try to keep you away.")
    else:
        print("\n🚪 UPPER FLOOR - THE ATTIC 🚪\n"
              "The attic is filled with forgotten toys and old memories. Someone seems to be standing guard,\n"
              "ready to protect these treasures. Proceed with caution.")


def level_up(character, hp, level, skill_set):
    character['Stat']['HP'] += hp
    character['Stat']['Current HP'] = character['Stat']['HP']
    character['Stat']['Level'] = level
    character['Stat']['Exp'] = 0
    character['Stat']['Hunger'] = 10
    character['Inventory']['Key'] = 0
    character['Skill']['Basic Attack'] += 5
    character['Skill']['Current Skills'].update(skill_set[f'Level {level}'])
    print(f"Your maximum HP has been increased by {hp}. "
          f"You earned two new skills ({','.join(skill_set[f'Level {level}'].keys())}). (max HP +{hp})\n")


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

        if character["Stat"]['Hunger'] == 1:
            print('🚨🚨🚨 You only have 1 Hunger! You must sleep now. 🚨🚨🚨')

        direction, character = get_user_choice(character, grid)
        (new_row, new_col), prev_cell_content, character, valid_checking = (
            move_character_valid_move(grid, first_location, direction, prev_cell_content, character))
        first_location = (new_row, new_col)
        if not valid_checking:
            continue
        check_character_hunger(character)
        there_is_a_challenger = check_probability(0.25)
        if there_is_a_challenger:
            game_list = ['battle', 'hangman', 'memory game']
            challenge = random.choice(game_list)
            if challenge == 'battle':
                print("You are going to battle! Prepare yourself.")
                character, has_won = battle(character)
                # print(has_won, character)
                if has_won:
                    get_reward(character)
            elif challenge == 'hangman':
                print("You are about to play Hangman!\n\n"
                      "📖 How to Play 📖\n"
                      "Try to guess the secret word, one letter at a time. You have limited tries. "
                      "Remember: every key counts as a guess, so be careful. Good luck!")
                input("Press any key to continue...")
                level = check_character_level_hangman(character)
                has_won, character = hangman(level, character)
                # print(has_won, character)
                if has_won:
                    print("Congratulations! You have won!")
                    get_reward(character)
            elif challenge == 'memory game':
                print("You are about to play Memory Game!\n\n"
                      "📖 How to Play 📖\n"
                      "You'll be shown a sequence of letters. You have 5 seconds to memorize it. Then, enter each "
                      "letter one at a time in the correct order. Good luck!")
                input("Press any key to continue...")
                level_matching_game = check_character_level_matching_game(character)
                has_won, character = play_game(level_matching_game, character)
                if has_won:
                    print("Congratulations! You have won!")
                    get_reward(character)

        goal_lv1 = check_character_1_level_location_exp(first_location, character)
        if goal_lv1:
            grid = make_board_lv2()
            first_location, prev_cell_content = make_character_location(grid)
            level_up(character, 200, 2, skill_set)
            # level_up_2(character, skill_set)
            # character['Stat']['HP'] += 200
            # character['Stat']['Current HP'] = character['Stat']['HP']
            # character['Stat']['Level'] = 2
            # character['Stat']['Exp'] = 0
            # character['Stat']['Hunger'] = 10
            # character['Skill']['Current Skills'].update(skill_set['Level 2'])
            # # character['Skill'] = {
            # #     "Basic Attack": random.randint(10, 30),
            # #     "Current Skills": {
            # #             "Bark": random.randint(20, 50),
            # #             "Scratch": random.randint(20, 50),
            # #             "Digging": random.randint(20, 50)}}
            # print(f"Your maximum HP has been increased by 200. "
            #       f"You earned two new skills ({','.join(skill_set['Level 2'].keys())}). (max HP +200)\n")
            describe_map_based_on_level(character)

        goal_lv2 = check_character_2_level_location_exp(first_location, character)
        if goal_lv2:
            grid = make_board_lv3()
            first_location, prev_cell_content = make_character_location(grid)
            level_up(character, 250, 3, skill_set)
            # level_up_3(character, skill_set)
            # character['Stat']['HP'] += 250
            # character['Stat']['Current HP'] = character['Stat']['HP']
            # character['Stat']['Level'] = 3
            # character['Stat']['Exp'] = 0
            # character['Stat']['Hunger'] = 10
            # character['Skill']['Current Skills'].update(skill_set['Level 3'])
            # character['Skill'] = {
            #     "Basic Attack": random.randint(10, 30),
            #     "Current Skills": {
            #         "Bark": random.randint(20, 50),
            #         "Scratch": random.randint(20, 50),
            #         "Digging": random.randint(20, 50),
            #         "Tail Whip": random.randint(20, 50),
            #         "Bite": random.randint(20, 50)}}
            # print(f"Your maximum HP has been increased by 250. "
            #       f"You earned two new skills ({','.join(skill_set['Level 3'].keys())}). (max HP +250)\n")
            # print("당신의 hp 200상승, level up, skill을 얻으셧습니다(Tail whip, bite)")
            describe_map_based_on_level(character)
        final_goal = check_character_3_level_location_for_final(first_location, character)
        if final_goal is not None:
            if final_goal:
                print("🎉 Victory! You defeated the boss, but soon realized it was all a misunderstanding "
                      "with Majestic Fluffy BunBun. With Haru safe, it's time to return home.")
                achieved_goal = True
            else:
                print("😞 Oh no! You weren't strong enough to defeat the boss this time. Train harder and grow "
                      "stronger! Returning to checkpoint - the start of Level 3. Keep going, you can do this!\n"
                      "(Exp reset to 0)")
                character['Stat']['Exp'] = 0
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
