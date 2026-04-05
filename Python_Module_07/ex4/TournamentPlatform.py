from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return (
            f"\n{card.name} (ID: {card.card_id}):\n"
            f"- Interfaces: [Card, Combatable, Rankable]\n"
            f"- Rating: {card.rating}\n"
            f"- Record: {card.wins}-{card.lose}"
        )

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        self.matches_played += 1

        while True:
            card2.health -= card1.power
            if card2.health <= 0:
                winner, loser = card1, card2
                break

            card1.health -= card2.power
            if card1.health <= 0:
                winner, loser = card2, card1
                break
        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        cards_list = list(self.cards.values())

        n = len(cards_list)
        for i in range(n):
            max_index = i
            for j in range(i + 1, n):
                if cards_list[j].rating > cards_list[max_index].rating:
                    max_index = j
            (
                cards_list[i], cards_list[max_index]
            ) = (
                cards_list[max_index], cards_list[i]
            )
        leaderboard = []
        for i, card in enumerate(cards_list, start=1):
            leaderboard.append(
                f"{i}. {card.name} - Rating: {card.rating} "
                f"({card.wins}-{card.lose})"
            )

        return leaderboard

    def generate_tournament_report(self) -> dict:
        Total_cards = len(self.cards)
        total_rating = sum(card.rating for card in self.cards.values())
        avg_rating = total_rating // Total_cards if Total_cards > 0 else 0

        return {
            "total_cards": Total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
