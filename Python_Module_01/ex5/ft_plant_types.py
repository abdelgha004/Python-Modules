#!/usr/bin/env python3

class Plant:
    """Base class for all plants with common attributes."""

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance.

        Args:
            name (str): The name of the plant.
            height (int): Height of the plant in cm.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Flower subclass with color and blooming capability."""

    def __init__(self, name: str, height: int, age: int, color: str):
        """
        Initialize a Flower instance.

        Args:
            name (str): Name of the flower.
            height (int): Height in cm.
            age (int): Age in days.
            color (str): Flower color.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print a message indicating that the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")

    def describe(self):
        """Print detailed information about the flower."""
        print(
            f"\n{self.name} (Flower): {self.height}cm, "
            f"{self.age} days, {self.color} color"
        )
        self.bloom()


class Tree(Plant):
    """Tree subclass with trunk diameter and shade production."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """
        Initialize a Tree instance.

        Args:
            name (str): Name of the tree.
            height (int): Height in cm.
            age (int): Age in days.
            trunk_diameter (int): Diameter of the trunk in cm.
        """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculate and print the approximate shade area provided by the tree.
        """
        shade_area = int((self.trunk_diameter / 2) ** 2 * 3.14 / 25)
        print(f"{self.name} provides {shade_area} square meters of shade")

    def describe(self):
        """Print detailed information about the tree."""
        print(
            f"\n{self.name} (Tree): {self.height}cm, "
            f"{self.age} days, {self.trunk_diameter}cm diameter"
        )
        self.produce_shade()


class Vegetable(Plant):
    """Vegetable subclass with harvest season and nutritional value."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str):
        """
        Initialize a Vegetable instance.

        Args:
            name (str): Name of the vegetable.
            height (int): Height in cm.
            age (int): Age in days.
            harvest_season (str): Season when the vegetable is harvested.
            nutritional_value (str): Key nutritional content.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe(self):
        """Print detailed information about the vegetable."""
        print(
            f"\n{self.name} (Vegetable): {self.height}cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    """Run a demo of different garden plant types."""
    plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 300, 1460, 40),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Carrot", 60, 70, "winter", "vitamin A")
    ]

    print("=== Garden Plant Types ===")
    for plant in plants:
        plant.describe()
