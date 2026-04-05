from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()
    dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        power=10,
        health=8,
        rating=1200,
    )
    wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        power=7,
        health=6,
        rating=1150,
    )
    print("\nRegistering Tournament Cards...")
    print(platform.register_card(dragon))
    print(platform.register_card(wizard))

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon.card_id, wizard.card_id)
    print("Match result:", match_result)

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(f"{entry}")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
