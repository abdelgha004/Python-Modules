#!/usr/bin/env python3

class Plant:
    """Represents a plant that grows and ages over time."""

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a Plant instance.

        Args:
            name (str): Name of the plant.
            height (int): Initial height in cm.
            age (int): Initial age in days.
        """
        self.name = name
        self.height = height
        self.age = age
        self.weekly_growth = 0
        self.days = 1

    def grow(self):
        """Increase the plant's height by 1cm."""
        self.height += 1

    def age_up(self):
        """Increase the plant's age and advance the day counter."""
        self.age += 1
        self.days += 1

    def get_info(self):
        """Print the current day, height, and age of the plant."""
        print(f"=== Day {self.days} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    """Simulate one week of growth for multiple plants."""
    plants = [
        Plant("Rose", 25, 30),
        Plant("Cactus", 5, 90)
    ]
    for plant in plants:
        plant.get_info()
        for i in range(6):
            plant.grow()
            plant.age_up()
        plant.get_info()
        print(f"Growth this week: +{i + 1}cm")
        print("-------------------")
