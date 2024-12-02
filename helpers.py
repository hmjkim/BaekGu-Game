def is_alive(character):
    return character['Stat']['Heart'] > 0


def lose_heart(character):
    character["Stat"]["Heart"] -= 1
    print(f"💔 You lost 1 Heart. You have {character['Stat']['Heart']} Heart(s) left.")
    character['Stat']['Current HP'] = character['Stat']['HP']


def get_item_choice(character):
    while True:
        item_use = (input("Which item would you like to use? (Enter the item number or type 'q' to quit): ")
                    .strip().lower())

        if item_use == '1' or item_use == 'hp potion':
            if character["Inventory"]["HP Potion"] > 0:
                character['Stat']['Current HP'] = character['Stat']['HP']
                character['Inventory']['HP Potion'] -= 1
                print("You used '🩸HP Potion'. Your HP is fully restored now. (HP %s/%s) - Remaining quantity: %s"
                      % (character['Stat']['Current HP'], character['Stat']['HP'], character['Inventory']['HP Potion']))
            else:
                print("❌ You don't have any HP Potion.")
        elif item_use == "2" or item_use == 'kibble':
            if character['Inventory']['Kibble'] > 0:
                character['Inventory']['Kibble'] -= 1
                character['Stat']['Hunger'] += 1
                print(f"You ate '🍽️Kibble'. Hunger increased by +1. - Remaining quantity: %s"
                      % character['Inventory']['Kibble'])
            else:
                print("❌ You don't have any Kibble.")
        elif item_use == "3" or item_use == 'key':
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
        f"🔰 Level     : {character['Stat']['Level']}\n"
        f"🩸 HP        : {character['Stat']['Current HP']}/{character['Stat']['HP']}\n"
        f"⭐ Exp       : {character['Stat']['Exp']}/{max_exp}\n"
        f"❤️ Hearts    : {character['Stat']['Heart']}/{character['Stat']['Max Heart']}\n"
        f"🍗 Hunger    : {character['Stat']['Hunger']}/{character['Stat']['Max Hunger']}\n"
        "--------------------------------------------------------\n"
    )


def display_skills(character):
    print("\n⚔️ Your Skills")
    print("--------------------------------------------------------")
    for skill, details in character['Skill']['Current Skills'].items():
        # Adjust the spacing to align the skill names and details better
        print(f"{skill:<12}: Damage: {details['Damage']}, {details['Description']}")
    print("--------------------------------------------------------")