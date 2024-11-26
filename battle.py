import random
from pprint import pprint
import time

from game import make_character

attack_descriptions = [
    "You strike fiercely, leaving a mark on the enemy!",
    "Your attack lands cleanly, leaving the enemy struggling to recover!",
    "With a focused attack, you manage to break through the enemy's guard, causing visible pain!"
    "Your powerful attack stunned the enemy.",
    "Your strike pierced through the enemy with precision."
]

def attack_description(enemy):
    description = random.choice(attack_descriptions)
    print(description.replace("enemy", enemy))

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
            # "MP": 50,
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
        enemy_copy = enemy.copy()
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

        enemy = random.choice([robotic_vacuum, guard_cat])
        enemy_copy = enemy.copy()
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
        enemy = random.choice([giant_moth, ghost])
        enemy_copy = enemy.copy()

    # Display enemy information
    print("--------------------------------------------\n"
          "!!! ENEMY ENCOUNTERED !!!\n"
          "--------------------------------------------\n"
          f"{enemy['Name']}\n"
          f"{enemy['Description']}\n"
          f"Level: {enemy['Level']}\n"
          f"HP: {enemy_copy['HP']}/{enemy['HP']}\n"
          "--------------------------------------------")

    # Get user choice
    character_hp = character["Stat"]["Current HP"]
    while character_hp > 0:
        options = ['Attack', 'Skill', 'Flee']
        user_choice = input(f'Enter battle options ("%s", "%s", or "%s" to run away):' % (options[0], options[1], options[2]))
        if user_choice.lower() == "attack":
            print("basic attack description")
            enemy_copy['HP'] -= character["Skill"]['Basic Attack']
            print("TODO: You attacked the enemy")
            print(f'*** {enemy_copy['Name']} HP is now {enemy_copy['HP']}/{enemy['HP']} ***')
        elif user_choice.lower() == "skill":
            print("skill description")

            current_skills = character['Skill']['Current Skills']
            formatted_skill = '\n'.join(current_skills.keys())
            skill_choice = input("--------------------------------------------\n"
                                 "⚔️ Skills: \n"
                                 f"{formatted_skill}\n"
                                 "--------------------------------------------\n"
                                 "Choose skill you would like to use:")
            print("TODO(Update this description): You used this {skill} on the enemy")
            selected_skill_damage = current_skills[skill_choice.title()]
            enemy_copy['HP'] -= selected_skill_damage
            print(f'*** {enemy_copy['Name']}\'s HP is now {enemy_copy['HP']}/{enemy['HP']} ***')
        elif user_choice.lower() == "flee":
            print(f"{enemy["Name"]} seems to be too strong for me.. Let me retreat before it's too late!")
            character["Heart"] -= 1

        else:
            print("Invalid input")
        if enemy_copy["HP"] > 0:
            # ADD TIME HERE
            time.sleep(2)
            enemy_skill = random.choice(list(enemy_copy['Attack'].items()))
            character_hp -= enemy_skill[1]
            print("TODO: Ouch! Enemy attacked you!")
            print(f'*** Your HP is now {character_hp}/{character['Stat']['HP']} ***')


def main():
    character = make_character()
    battle(character)


if __name__ == '__main__':
    main()

