from ex0.Card import Card
from typing import List
import random


class Deck:
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            card = self.cards.pop(0)
            return card
        return None

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = sum(
            1 for c in self.cards if c.__class__.__name__ == "CreatureCard"
        )
        spells = sum(
            1 for c in self.cards if c.__class__.__name__ == "SpellCard"
        )
        artifacts = sum(
            1 for c in self.cards if c.__class__.__name__ == "ArtifactCard"
        )
        avg_cost = (
            round(sum(c.cost for c in self.cards) / total, 1)
            if total > 0 else 0
        )

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
