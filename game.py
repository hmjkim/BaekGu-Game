import random

total_skill = {
    "Level 1": {"Bark": random.randint(20, 50)},
    "Level 2": {
        "Scratch": random.randint(20, 50),
        "Digging": random.randint(20, 50),
    },
    "Level 3": {
        "Tail Whip": random.randint(20, 50),
        "Bite": random.randint(20, 50),
    }
}

def make_character():
    # Make Character
    # Exp full = 1000?
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


def game():
    pass


def main():
    game()


if __name__ == "__main__":
    main()