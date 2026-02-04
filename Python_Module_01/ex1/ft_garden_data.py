#!/usr/bin/env python3

class Plant:
    """Represents a plant with basic attributes."""

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Height of the plant in cm.
            age (int): Age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    """Create plants and display their registry information."""
    garden_plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in garden_plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
