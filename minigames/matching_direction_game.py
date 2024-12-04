import random
import time

from helpers import lose_heart


def check_character_level_matching_game(character: dict) -> int:
    """
    Check character's current level to determine the number of matches.

    :param character: a dictionary of character including 'Level' key in 'Stat'
    :precondition: character must be a dictionary containing a nested dictionary under key 'Stat' and 'Level'
    :postcondition: return the correct number of matches based on the character's level
    :return: number of matches based on the character's level

    >>> character1 = {'Stat': {'Level': 1}}
    >>> check_character_level_matching_game(character1)
    5
    >>> character2 = {'Stat': {'Level': 3}}
    >>> check_character_level_matching_game(character2)
    9
    """
    if character['Stat']['Level'] == 1:
        matching_count = 5
        return matching_count
    if character['Stat']['Level'] == 2:
        matching_count = 7
        return matching_count
    else:
        matching_count = 9
        return matching_count


def play_game(level: int, character: dict) -> tuple[bool, dict]:
    """
    Play a direction game where the player memorize and input a sequence of directions ('A', 'D', 'S', 'W').

    :param level: an integer representing the number of directions to memorize
    :param character: a dictionary including the character's status, which includes 'Heart' as key in 'Stat'
    :precondition: level must be a positive integer
    :precondition: character must be a dictionary containing a nested dictionary under key 'Stat' with 'Heart' as a key
    :postcondition: print the sequence of directions to memorize
    :postcondition: get user input and convert to uppercase to compare with the sequence of directions
    :postcondition: return a boolean indicating success or failure, and the updated character's heart
    :return: a True or False through result of game and the updated character dictionary
    """
    strings = random.choices(['A', 'D', 'S', 'W'], k=level)
    print("Memorize the given directions:")
    print(strings)
    for count in range(5):
        time.sleep(1)
        print(5 - count)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Enter the answer")
    user_inputs = [input(f"{number+1} direction: ") for number in range(len(strings))]
    upper_inputs = [user_input.upper() for user_input in user_inputs]
    if upper_inputs == strings:
        print("Correct!")
        return True, character
    else:
        print("Wrong!")
        print("The answer was ", strings)
        lose_heart(character)
        return False, character


def main():
    character = {'Stat': {'Level': 1, 'Heart': 5}}
    level_matching_game = check_character_level_matching_game(character)
    check, character = play_game(level_matching_game, character)
    print(check, character)


if __name__ == "__main__":
    main()

