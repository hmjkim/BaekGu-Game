import random
from game import make_character

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


def make_enemies(name, description, hp_range, basic_attack, skill_damage, skill_name):
    return {
            "Name": name,
            "Description": description,
            "Level": 1,
            "HP": random.randint(*hp_range),
            "MP": 50,
            "Attack":
                {
                    f"{skill_name}": random.randint(*skill_damage),
                    "Basic Attack": random.randint(*basic_attack)
                }
            }


def battle(character):
    enemy_stat = configure_enemy_stat()

    # Create enemies
    if character["Stat"]["Level"] == 1:
        # Low Level Mobs (Underground)
        mouse = make_enemies('Mouse',
                             "A tiny mouse nibbling on a piece of cheese. It looks harmless, "
                             "but don't let your guard down!",
                             enemy_stat["HP Range"]["Level 1"],
                             enemy_stat["Basic Attack"]["Level 1"],
                             enemy_stat["Skill Damage"]["Level 1"],
                             'Nibble'
                             )
        spider = make_enemies('Spider',
                              'Spider Description',
                              enemy_stat["HP Range"]["Level 2"],
                              enemy_stat["Basic Attack"]["Level 2"],
                              enemy_stat["Skill Damage"]["Level 2"],
                              'Web Trap')

        enemy = random.choice([mouse, spider])

    elif character["Stat"]["Level"] == 2:
        # Mid-Level Mobs (Ground Level)
        robotic_vacuum = make_enemies('Robotic Vacuum',
                                      'Robotic Vacuum Description',
                                      enemy_stat["HP Range"]["Level 2"],
                                      enemy_stat["Basic Attack"]["Level 2"],
                                      enemy_stat["Skill Damage"]["Level 2"],
                                      'Suction')
        guard_cat = make_enemies('Guard Cat',
                                 'Guard Cat Description',
                                 enemy_stat["HP Range"]["Level 3"],
                                 enemy_stat["Basic Attack"]["Level 3"],
                                 enemy_stat["Skill Damage"]["Level 3"],
                                 'Hiss')
        enemy = random.choice[robotic_vacuum, guard_cat]
    else:
        # High Level Mobs (Upper Level - Attic)
        giant_moth = make_enemies('Giant Moth',
                                  'Giant Moth Description',
                                  enemy_stat["HP Range"]["Level 3"],
                                  enemy_stat["Basic Attack"]["Level 3"],
                                  enemy_stat["Skill Damage"]["Level 3"],
                                  'Wing Flap')
        ghost = make_enemies('Ghost',
                             'Ghost Description',
                             enemy_stat["HP Range"]["Level 4"],
                             enemy_stat["Basic Attack"]["Level 4"],
                             enemy_stat["Skill Damage"]["Level 4"],
                             'Chill Touch')
        enemy = random.choice[giant_moth, ghost]

    # Display enemy information
    print("--------------------------------------------\n"
          "!!! ENEMY ENCOUNTERED !!!\n"
          "--------------------------------------------\n"
          f"{enemy['Name']}\n"
          f"{enemy['Description']}\n"
          f"Level: {enemy['Level']}\n"
          f"HP: currentHP/{enemy['HP']}\n"
          "--------------------------------------------")
    while character["Stat"]["HP"] > 0 and enemy["HP"] > 0:
        input('Enter battle options ("Attack", "Skill", or "Flee" to run away):')

def main():
    character = make_character()
    battle(character)


if __name__ == '__main__':
    main()

