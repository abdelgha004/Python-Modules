from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")

    print("\nCreatureCard Info:")
    c_card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(c_card.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {c_card.is_playable(6)}")
    game_state = {"available_mana": 6}
    print(f"Play result: {c_card.play(game_state)}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", c_card.attack_target("Goblin Warrior"))

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {c_card.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
