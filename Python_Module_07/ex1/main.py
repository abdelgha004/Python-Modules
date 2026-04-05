from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Deck Builder ===")
    print("\nBuilding deck with different card types...")

    deck = Deck()

    spell_card = SpellCard("Lightning Bolt", 3, "Rare", "damage")
    artifact_card = ArtifactCard(
        "Mana Crystal", 2,
        "Common", 8, "+1 mana per turn")
    creature_card = CreatureCard("Fire Dragon", 5, "Legendary", 9, 6)

    deck.add_card(spell_card)
    deck.add_card(artifact_card)
    deck.add_card(creature_card)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    for _ in range(3):
        card = deck.draw_card()
        card_info = card.get_card_info()
        print(f"\nDrew: {card_info['name']} ({card_info['type']})")
        game_state = {"available_mana": 6}
        print(f"Play result: {card.play(game_state)}")

    print(
        "\nPolymorphism in action: Same interface,"
        " different card behaviors!"
        )


if __name__ == "__main__":
    main()
