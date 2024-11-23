import random
from make_board_each_level import *

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


def game():
    pass


def main():
    game()


if __name__ == "__main__":
    main()
