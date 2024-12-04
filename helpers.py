def is_alive(character):
    """
    Check a character's heart stat.

    :param character: a dictionary including 'Stat' as key including heart
    :precondition: character must have a 'Stat' key with a 'Heart' sub key
    :postcondition: return a boolean whether the heart stat is greater than zero or not
    :return: a boolean

    >>> character_3 = {'Stat': {'Heart': 3}}
    >>> is_alive(character_3)
    True
    >>> character_0 = {'Stat': {'Heart': 0}}
    >>> is_alive(character_0)
    False
    """
    return character['Stat']['Heart'] > 0


def lose_heart(character):
    """
    Reduce the character's heart count by one and reset their Current HP to the HP value.

    :param character: a dictionary including 'Stat' as key including 'Heart', 'Current HP' and 'HP'
    :precondition: character must have a 'Stat' key with a 'Heart', 'Current HP', and 'HP' sub keys
    :postcondition: character's 'Heart' count is reduced by one, and 'Current HP' is set to 'HP'

    >>> character_3_10_20 = {'Stat': {'Heart': 3, 'Current HP': 10, 'HP': 20}}
    >>> lose_heart(character_3_10_20)
    💔 You lost 1 Heart. You have 2 Heart(s) left.
    >>> character_3_10_20['Stat']['Heart']
    2
    >>> character_3_10_20['Stat']['Current HP']
    20
    """
    character["Stat"]["Heart"] -= 1
    print(f"💔 You lost 1 Heart. You have {character['Stat']['Heart']} Heart(s) left.")
    character['Stat']['Current HP'] = character['Stat']['HP']


def use_hp_potion(character):
    """
    Check the count of HP potions in inventory, and if any are available, use it to restore the character's current HP.

    :param character: a dictionary including the keys 'Inventory' and 'Stat' including 'HP Potion' and 'Current HP'
    :precondition: character must have 'Inventory' and 'Stat' keys with 'HP Potion' and 'Current HP' sub keys
    :postcondition: character's current HP is restored if an HP potion are available
    :postcondition: HP potion's count is reduced by one
    :postcondition: Print that the user has used an HP potion, showing the restored HP and the remaining HP potions
    :postcondition: if HP potion is not available, print that the user doesn't have any HP potions

    >>> character_with_potions = {'Inventory': {'HP Potion': 1}, 'Stat': {'Current HP': 50, 'HP': 100}}
    >>> use_hp_potion(character_with_potions)
    You used '🩸HP Potion'. Your HP is fully restored now. (HP 100/100) - Remaining quantity: 0
    >>> character_with_potions['Inventory']['HP Potion']
    0
    >>> character_with_potions['Stat']['Current HP']
    100
    """
    if character["Inventory"]["HP Potion"] > 0:
        character['Stat']['Current HP'] = character['Stat']['HP']
        character['Inventory']['HP Potion'] -= 1
        print("You used '🩸HP Potion'. Your HP is fully restored now. (HP %s/%s) - Remaining quantity: %s"
              % (character['Stat']['Current HP'], character['Stat']['HP'], character['Inventory']['HP Potion']))
    else:
        print("❌ You don't have any HP Potion.")


def use_kibble(character):
    if character['Inventory']['Kibble'] > 0:
        character['Inventory']['Kibble'] -= 1
        character['Stat']['Hunger'] += 1
        print(f"You ate '🍽️Kibble'. Hunger increased by +1. - Remaining quantity: %s"
              % character['Inventory']['Kibble'])
    else:
        print("❌ You don't have any Kibble.")


def get_item_choice(character):
    while True:
        item_use = (input("Which item would you like to use? (Enter the item number or type 'q' to quit): ")
                    .strip().lower())

        # if item_use == '1' or item_use == 'hp potion':
        if item_use in ['1', 'hp potion']:
            use_hp_potion(character)
            # if character["Inventory"]["HP Potion"] > 0:
            #     character['Stat']['Current HP'] = character['Stat']['HP']
            #     character['Inventory']['HP Potion'] -= 1
            #     print("You used '🩸HP Potion'. Your HP is fully restored now. (HP %s/%s) - Remaining quantity: %s"
            #           % (character['Stat']['Current HP'], character['Stat']['HP'], character['Inventory']['HP Potion']))
            # else:
            #     print("❌ You don't have any HP Potion.")
        # elif item_use == "2" or item_use == 'kibble':
        elif item_use in ['2', 'kibble']:
            use_kibble(character)
            # if character['Inventory']['Kibble'] > 0:
            #     character['Inventory']['Kibble'] -= 1
            #     character['Stat']['Hunger'] += 1
            #     print(f"You ate '🍽️Kibble'. Hunger increased by +1. - Remaining quantity: %s"
            #           % character['Inventory']['Kibble'])
            # else:
            #     print("❌ You don't have any Kibble.")
        # elif item_use == "3" or item_use == 'key':
        elif item_use in ['3', 'key']:
            print("❌ You cannot directly use the key. The key will be automatically used at the door.")
        elif item_use == "q":
            return True
        else:
            print("❌ Invalid input. Please enter a correct option from the list.")


def display_inventory(character):
    print(
        "\n🎒 Your Inventory\n"
        "--------------------------------------------------------\n"
        f" 1: 🩸 HP Potion ({character['Inventory']['HP Potion']})   - Fully restores your HP\n"
        f" 2: 🍽️ Kibble ({character['Inventory']['Kibble']})      - Increases your Hunger by +1\n"
        f" 3: 🗝️ Key ({character['Inventory']['Key']})         - Not directly usable\n"
        "--------------------------------------------------------"
    )


def display_stats(character):
    max_exp = character['Stat']['Max Exp']['Level 1'] if character['Stat']['Level'] == 1 else (
        character)['Stat']['Max Exp']['Level 2']
    print(
        "\n📊 Your Stats:\n"
        "--------------------------------------------------------\n"
        f"🔰 Level          : {character['Stat']['Level']}\n"
        f"🩸 HP             : {character['Stat']['Current HP']}/{character['Stat']['HP']}\n"
        f"⭐ Exp            : {character['Stat']['Exp']}/{max_exp}\n"
        f"❤️ Hearts         : {character['Stat']['Heart']}/{character['Stat']['Max Heart']}\n"
        f"🍗 Hunger         : {character['Stat']['Hunger']}/{character['Stat']['Max Hunger']}\n"
        f"🗡️ Basic Attack   : Damage {character['Skill']['Basic Attack']}\n"
        "--------------------------------------------------------\n"
    )


def display_skills(character):
    print("\n⚔️ Your Skills")
    print("--------------------------------------------------------")
    for skill, details in character['Skill']['Current Skills'].items():
        # Adjust the spacing to align the skill names and details better
        print(f"{skill:<12}: Damage: {details['Damage']}, {details['Description']}")
    print("--------------------------------------------------------")