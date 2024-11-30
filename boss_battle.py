import random
import time
from battle import *

# from game import make_character, is_alive


def boss_battle(character):
    enemy_stat = configure_enemy_stat()
    # BOSS
    enemy = make_enemies('Majestic Fluffy BunBun',
                             '🐰',
                             'An old and tattered bunny plushie, once loved but now abandoned in the attic. '
                             'Majestic Fluffy BunBun believes he is the noble protector of all the forgotten treasures here. You must fight to get the ',
                             '10',
                             enemy_stat["HP Range"]["Boss"],
                             enemy_stat["Basic Attack"]["Boss"],
                             enemy_stat["Skill Damage"]["Boss"],
                             'Cuddle Crush')
    enemy_copy = enemy.copy()

    # Display enemy information
    print("--------------------------------------------\n"
          "‼️‼️ BOSS ENCOUNTERED ‼️‼️\n"
          "--------------------------------------------\n"
          f"{enemy['Icon']} {enemy['Name']}\n"
          f"{enemy['Description']}\n"
          f"Level: {enemy['Level']}\n"
          f"HP: {enemy_copy['HP']}/{enemy['HP']}\n"
          "--------------------------------------------")

    # Get user choice
    # Skill usage
    total_skill_use = 5
    skill_usage_limit = 5
    current_skill_usage = 0
    in_battle = True
    has_won = False

    while is_alive(character) and enemy_copy["HP"] > 0 and in_battle:
        options = ['Attack', 'Skill', 'Flee', 'Stat', 'Inventory']
        while True:
            user_choice = input(f'Enter battle options ("%s", "%s", "%s" to run away, "%s" to see your current condition, or "%s" to use items):' % (options[0], options[1], options[2], options[3], options[4]))

            if user_choice.lower() == "attack":
                display_attack_description(enemy["Name"])
                enemy_copy['HP'] -= character["Skill"]['Basic Attack']

                have_break = show_current_hp(enemy_copy['HP'], enemy['HP'], enemy_copy['Name'])
                if have_break:
                    break
            elif user_choice.lower() == "skill":
                if skill_usage_limit > 0:
                    current_skills = character['Skill']['Current Skills']
                    formatted_skill = '\n'.join(current_skills.keys())

                    print(f"In each battle, you are allowed a total of {total_skill_use} skill uses.")
                    display_skill_uses(current_skill_usage, skill_usage_limit)
                    skill_choice = input("--------------------------------------------\n"
                                         "⚔️ Skills: \n"
                                         f"{formatted_skill}\n"
                                         "--------------------------------------------\n"
                                         "Choose skill you would like to use:")

                    display_attack_description(enemy["Name"])
                    selected_skill_damage = current_skills[skill_choice.title()]
                    enemy_copy['HP'] -= selected_skill_damage
                    have_break = show_current_hp(enemy_copy['HP'], enemy['HP'], enemy_copy['Name'])
                    if have_break:
                        break
                    skill_usage_limit -= 1
                    current_skill_usage += 1
                else:
                    print("Sorry. You used all the available skill uses.")
                    display_skill_uses(current_skill_usage, skill_usage_limit)
                    break

            elif user_choice.lower() == "flee":
                print(f"{enemy["Name"]} seems to be too strong for me.. Let me retreat before it's too late!")
                lose_heart(character)
                in_battle = False
                break
            elif user_choice.lower() == "stat":
                print("stats = ", character['Stat'])
                print("skills = ", character['Skill'])
                continue
            elif user_choice.lower() == "inventory":
                print("inventory = ", character['Inventory'])
                print("--------------------------------------------\n"
                         "🎒️ Items: \n"
                         f"1. HP Potion : {character['Inventory']['HP Potion']}\n"
                         f"2. Kibble : {character['Inventory']['Kibble']}\n"
                         "--------------------------------------------\n")
                item_to_use = input("Enter item to use: ")
                if item_to_use.lower() == '1' or item_to_use.lower() == 'hp potion':
                    character["Stat"]["Current HP"] = character["Stat"]["HP"]
                    print(f"Your HP is full now. (HP: {character['Stat']['Current HP']}/{character['Stat']['HP']})")
                    character['Inventory']['HP Potion'] -= 1
                    continue
                elif item_to_use.lower() == '2' or item_to_use.lower() == 'kibble':
                    character["Stat"]["Hunger"] += 1
                    print(f"Hunger increased by 1. (Hunger: {character['Stat']['Current HP']}/{character['Stat']['HP']})")
                    character['Inventory']['Hunger'] -= 1
                    continue
            else:
                print("Invalid input. Please try again.")
                continue

            if enemy_copy["HP"] > 0:
                time.sleep(1.5)
                enemy_skill = random.choice(list(enemy_copy['Attack'].items()))
                character["Stat"]["Current HP"] -= enemy_skill[1]
                print(f"Ouch! {enemy["Name"]} attacked you!")

                have_break = show_current_hp(character["Stat"]["Current HP"], character['Stat']['HP'], 'Your')
                if have_break:
                    break
    if not is_alive(character):
        print("I collapsed on the floor. The enemy stands victorious as my vision fades to darkness...")
        lose_heart(character)
        has_won = False
    elif enemy_copy["HP"] < 0:
        print("Woo hoo! You won against a ruff battle. Time for a treat!")
        has_won = True

    return character, has_won

#
# def main():
#     character = make_character()
#     battle(character)
#
#
# if __name__ == '__main__':
#     main()

