import random


def configure_enemy_stat():
    # Configure enemies
    # HP, Attack damage, Skill damage random
    return {
        "HP Range": {
            "Level 1": (80, 100),
            "Level 2": (101, 200),
            "Level 3": (201, 300),
            "Level 4": (301, 400),
            "Boss": (500, 600)
        },
        "Basic Attack": {
            "Level 1": (5, 10),
            "Level 2": (15, 30),
            "Level 3": (35, 50),
            "Level 4": (60, 90),
            "Boss": (100, 300)
        },
        "Skill Damage": {
            "Level 1": (10, 25),
            "Level 2": (26, 45),
            "Level 3": (46, 70),
            "Level 4": (75, 100),
            "Boss": (130, 300)
        }
    }


def make_enemies(hp_range, basic_attack, skill_damage, skill_name):
    return {"Level": 1,
            "HP": random.randint(*hp_range),
            "MP": 50,
            "Attack":
                {
                    f"{skill_name}": random.randint(*skill_damage),
                    "Basic Attack": random.randint(*basic_attack)
                }
            }


def battle(character):
    pass

def main():
    battle()


if __name__ == '__main__':
    main()

