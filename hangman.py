import random

from hangman_art import stages
import warnings
warnings.filterwarnings("ignore")


def lists_of_words():
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


def check_character_level(character, lists=lists_of_words()):
    if character['Stat']['Level'] == 1:
        return lists[2]
    if character['Stat']['Level'] == 2:
        return lists[1]
    else:
        return lists[0]


def word_strike(text):
    return ' '.join([u'\u0336{}'.format(c) for c in text])


def hangman(word_list, stages, character):
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 8
    display = []
    for _ in range(word_length):
        display += "_"

    print("Current lives: %d" % lives)
    empty_incorrect = []

    end_of_game = False
    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        if guess in display or guess in empty_incorrect:
            print(f"You've already guessed '{guess}'")
            continue

        correct_guess = False
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print("Current lives: %d" % lives)
                correct_guess = True

        if not correct_guess:
            lives -= 1
            print("-1 life")
            print("Current lives: %d" % lives)
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            empty_incorrect.append(guess)
            print("Incorrect answers: %s" % word_strike(empty_incorrect))
            if lives == 0:
                print("You lose.")
                print(f"The word was: '{chosen_word}'")
                character['Stat']['Heart'] -= 1
                break

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win!")

        print(stages[lives])
    return end_of_game, character


def main():
    character = {'Stat': {'Level': 1, 'Heart': 1}}
    list = check_character_level(character)
    i, j = hangman(list, stages, character)
    print(i,j)



if __name__ == "__main__":
    main()
