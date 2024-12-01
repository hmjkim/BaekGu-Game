def is_alive(character):
    return character['Stat']['Heart'] > 0


def display_inventory(character):
    print(
        "\n🎒 Your Inventory\n"
        "--------------------------------------------------------\n"
        f" 1: 🩸 HP Potion ({character['Inventory']['HP Potion']})   - Fully restores your HP\n"
        f" 2: 🍽️ Kibble ({character['Inventory']['Kibble']})      - Increases your Hunger by +1\n"
        f" 3: 🗝️ Key ({character['Inventory']['Key']})         - not usable directly\n"
        "--------------------------------------------------------\n"
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
        "--------------------------------------------------------"
    )


def display_skills(character):
    print("\n⚔️ Your Skills")
    print("--------------------------------------------------------")
    for skill, details in character['Skill']['Current Skills'].items():
        # Adjust the spacing to align the skill names and details better
        print(f"{skill:<12}: Damage: {details['Damage']}, {details['Description']}")
    print("--------------------------------------------------------")