from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.creature_list = ['dragon', 'goblin']
        self.spells_list = ['fireball']
        self.artifacts_list = ['mana_ring']
        self.cards = []

    def create_creature(self, name) -> Card:
        if name == "Fire Dragon":
            creature = CreatureCard(name, 5, "Legendery", 4, 10)
        elif name == "Goblin Warrior":
            creature = CreatureCard(name, 2, "Legendery", 2, 5)
        else:
            creature = CreatureCard(name, 1, "Legendery", 1, 10)

        self.cards.append(creature)
        return creature

    def create_spell(self, name) -> Card:
        spell = SpellCard(name, 3, "Legendery", "damage")
        self.cards.append(spell)
        return spell

    def create_artifact(self, name) -> Card:
        artifact = ArtifactCard(name, 2, "Legendery", 4, "mana boost")
        self.cards.append(artifact)
        return artifact

    def create_themed_deck(self, size: int) -> list:
        deck = [
            self.create_creature("Fire Dragon"),
            self.create_creature("Goblin Warrior"),
            self.create_spell("Lightning Bolt")
        ]
        return deck[:size]

    def get_supported_types(self):
        return {
            "creatures": self.creature_list,
            "spells": self.spells_list,
            "artifacts": self.artifacts_list
        }
