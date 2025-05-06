# Zykria Best
# 05/28/25
# P5HW
# Program simulates a simple Knight vs Dragon game where the player can create a Knight, display attributes, and battle a dragon.

import random

def create_character():
    """
    Value-returning function.
    No parameters.
    Asks user for character name, health, and attack points.
    Returns a dictionary representing the Knight.
    """
    print("\n⚔️ Create Your Knight! ⚔️")
    name = input("Enter your knight's name: ")
    health = int(input("Enter your knight's starting health (e.g., 100): "))
    attack_points = int(input("Enter your knight's attack points (e.g., 20): "))
    
    knight = {
        "Name": name,
        "Health": health,
        "Attack Points": attack_points
    }
    return knight

def display_character(character):
    """
    Non-value-returning function.
    Takes one parameter: character (dictionary).
    Prints character's attributes.
    """
    print("\n🛡️ Knight's Current Stats 🛡️")
    for attribute, value in character.items():
        print(f"{attribute}: {value}")

def attack_dragon(character):
    """
    Non-value-returning function.
    Simulates the knight attacking a dragon.
    Reduces the knight's health based on a random dragon attack.
    """
    if character["Health"] <= 0:
        print("\n❗ Your knight has no health left! They can't battle anymore.")
        return

    print("\n🐉 A dragon appears! Battle begins! 🐉")
    
    dragon_attack = random.randint(10, 30)
    character["Health"] -= dragon_attack
    
    if character["Health"] < 0:
        character["Health"] = 0

    print(f"The dragon attacks and deals {dragon_attack} damage!")
    print(f"🏥 Your knight now has {character['Health']} health left.")

def main():
    """
    Non-value-returning function.
    Controls the game loop.
    """
    knight = None  # No character created at start

    while True:
        print("\n🏰 Knight vs Dragon Menu 🏰")
        print("1. Create a New Knight")
        print("2. Display Knight")
        print("3. Battle a Dragon")
        print("4. Exit Game")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            knight = create_character()
        elif choice == "2":
            if knight:
                display_character(knight)
            else:
                print("\n⚠️ No knight created yet!")
        elif choice == "3":
            if knight:
                attack_dragon(knight)
            else:
                print("\n⚠️ No knight created yet!")
        elif choice == "4":
            print("\n🏰 Thanks for playing Knight vs Dragon! Farewell, brave warrior!")
            break
        else:
            print("\n⚠️ Invalid choice. Please pick 1-4.")

# Always call the main function at the end
if __name__ == "__main__":
    main()
