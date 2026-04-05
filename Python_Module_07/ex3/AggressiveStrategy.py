from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        total_damage = 0
        targets_attacked = self.prioritize_targets(battlefield)

        for i in range(len(hand)):
            min_index = i
            for j in range(i + 1, len(hand)):
                if hand[j].cost < hand[min_index].cost:
                    min_index = j
            hand[i], hand[min_index] = hand[min_index], hand[i]

        for card in hand[:2]:
            cards_played.append(card.name)
            mana_used += card.cost

            if isinstance(card, CreatureCard):
                total_damage += card.attack
            elif isinstance(card, SpellCard):
                total_damage += 6

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": total_damage
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if available_targets:
            return [available_targets[0]]
        else:
            return ["Enemy Player"]
