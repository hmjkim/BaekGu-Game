import random

from helpers import lose_heart
from minigames.hangman_art import stage
import warnings
warnings.filterwarnings("ignore")


def lists_of_words() -> tuple[list[str], list[str], list[str]]:
    """
    Generate three lists of words categorized by their lengths.

    :postconditions: return three lists based on the number of words
    :return: three lists of words
    """
    word_4_list = [
        "book", "tree", "blue", "love", "care", "hope", "door", "jump",
        "play", "work", "fish", "swim", "ball", "hand", "cake", "sing",
        "walk", "rain", "star", "wind", "read", "rock", "band", "ship",
        "moon", "face", "line", "ride", "time", "life"
    ]
    word_5_list = [
        "apple", "grape", "pearl", "chair", "table", "drink", "watch", "plant",
        "beach", "smile", "light", "stone", "bread", "glass", "truck", "train",
        "shoes", "knife", "piano", "candy", "house", "cloud", "music", "paint",
        "dream", "flame", "brain", "spark", "bloom", "sweet"
    ]
    word_6_list = [
        "garden", "silver", "branch", "butter", "turtle", "bridge", "rabbit", "pebble",
        "button", "stream", "travel", "bottle", "winter", "flower", "basket", "orange",
        "desert", "magnet", "planet", "frozen", "safety", "forest", "guitar", "friend",
        "yellow", "ticket", "pencil", "bridge", "jungle", "school"
    ]
    return word_4_list, word_5_list, word_6_list


def check_character_level_hangman(character: dict, lists: list = lists_of_words()) -> list:
    """
    Determine the appropriate word list based on the character's level.

    :param character: a dictionary including character stats including level
    :param lists: a list of word lists
    :precondition: character must be a dictionary with a 'Stat' key that contains a 'Level' key
    :postcondition: return a list of words appropriate for the character's level
    :return: A list of words

    >>> character1 = {'Stat': {'Level': 1}}
    >>> words = lists_of_words()
    >>> check_character_level_hangman(character1, words)
    ['garden', 'silver', 'branch', 'butter', 'turtle', 'bridge', 'rabbit', 'pebble', 'button', 'stream', 'travel', 'bottle', 'winter', 'flower', 'basket', 'orange', 'desert', 'magnet', 'planet', 'frozen', 'safety', 'forest', 'guitar', 'friend', 'yellow', 'ticket', 'pencil', 'bridge', 'jungle', 'school']
    >>> character2 = {'Stat': {'Level': 3}}
    >>> check_character_level_hangman(character2, words)
    ['book', 'tree', 'blue', 'love', 'care', 'hope', 'door', 'jump', 'play', 'work', 'fish', 'swim', 'ball', 'hand', 'cake', 'sing', 'walk', 'rain', 'star', 'wind', 'read', 'rock', 'band', 'ship', 'moon', 'face', 'line', 'ride', 'time', 'life']
    """
    if character['Stat']['Level'] == 1:
        return lists[2]
    if character['Stat']['Level'] == 2:
        return lists[1]
    else:
        return lists[0]


def word_strike(text: str) -> str:
    """
    Applies a strikethrough effect to each character in the strings.

    :param text: a string
    :precondition: text must be a string
    :postcondition: return a string with strikethrough effects applied to each character
    :return: strings with a strikethrough effect

    >>> word_strike('hello')
    '̶h ̶e ̶l ̶l ̶o'
    >>> word_strike('!')
    '̶!'
    >>> word_strike('A')
    '̶A'
    """
    return ' '.join([u'\u0336{}'.format(c) for c in text])


def handle_incorrect_guess(guess: str, incorrect_guesses, remaining_lives: int) -> None:
    """
    Print the wrong guess and remaining lives and update incorrect guess
    
    :param guess: a string
    :param incorrect_guesses: a list that holds all the incorrect guesses
    :param remaining_lives: the player's remaining lives
    :precondition: guess must be a string
    :precondition: incorrect_guesses must be a list
    :precondition: remaining_lives must be an integer
    :postcondition: print remaining lives and the incorrect guess with word strike effect
    :postcondition: update incorrect_guesses by appending the guess
    """
    print("-1 life")
    print(f"Current lives: {remaining_lives}")
    print(f"You guessed '{guess}', that's not in the word. You lose a life.")
    incorrect_guesses.append(guess)
    print("Incorrect answers: " + word_strike(incorrect_guesses))


def hangman(word_list: list[str], character: dict) -> tuple[bool, dict]:
    """
    Drive the hangman game.
    """
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 8
    display = []
    [display.append("_") for _ in range(word_length)]
    print("Current lives: %d" % lives)
    empty_incorrect = []
    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").strip().lower()
        if guess in display or guess in empty_incorrect:
            print(f"You've already guessed '{guess}'")
            continue

        correct_guess = False
        for position, letter in enumerate(chosen_word):
            if letter == guess:
                display[position] = letter
                correct_guess = True

        if not correct_guess:
            lives -= 1
            handle_incorrect_guess(guess, empty_incorrect, lives)
            if lives == 0:
                print("You lose.")
                print(f"The word was: '{chosen_word}'")
                lose_heart(character)
                break

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win!")
        stages = stage()
        print(stages[lives])
    return end_of_game, character
