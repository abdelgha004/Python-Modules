#!/usr/bin/env python3

class Plant:
    """Base class for all plants."""
    def __init__(self, name, height):
        """
        Initialize a Plant.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in cm.
        """
        self.name = name
        self.height = height

    def grow(self):
        """Increase plant height by 1cm."""
        self.height += 1


class FloweringPlant(Plant):
    """Plant that can produce flowers."""
    def __init__(self, name, height, color=None, blooming=False):
        """
        Initialize a FloweringPlant.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in cm.
            color (str, optional): The flower color.
            blooming (bool, optional): Whether the plant is blooming.
        """
        super().__init__(name, height)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    """Special flowering plant that can win prizes."""
    def __init__(self, name, height, color=None,
                 blooming=False, prize_points=0):
        """
        Initialize a PrizeFlower.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in cm.
            color (str, optional): The flower color.
            blooming (bool, optional): Whether the plant is blooming.
            prize_points (int, optional): Prize points for the plant.
        """
        super().__init__(name, height, color, blooming)
        self.prize_points = prize_points


class GardenManager:
    """Manages multiple gardens and provides analytics."""
    total_gardens = 0

    def __init__(self):
        """Initialize a GardenManager and increment total gardens."""
        self.gardens = []
        GardenManager.total_gardens += 1

    class Garden:
        """Individual garden that contains plants."""
        def __init__(self, owner):
            """
            Initialize a Garden.

            Args:
                owner (str): The name of the garden owner.
            """
            self.owner = owner
            self.plants = []
            self.total_growth = 0

        def add_plant(self, plant, printed=True):
            """
            Add a plant to this garden.

            Args:
                plant (Plant): The plant instance to add.
                printed (bool, optional): Whether to print confirmation.
            """
            self.plants.append(plant)
            if printed:
                print(f"Added {plant.name} to {self.owner}'s garden")

        def grow_all_plants(self):
            """Grow all plants in the garden by 1cm."""
            print(f"\n{self.owner} is helping all plants grow...")
            for plant in self.plants:
                plant.grow()
                self.total_growth += 1
                print(f"{plant.name} grew 1cm")

        def report(self, all_gardens):
            """
            Print a report of the garden, including plant details and scores.

            Args:
                all_gardens (list): List of all gardens for score comparison.
            """
            print(f"\n=== {self.owner}'s Garden Report ===")
            print("Plants in garden:")

            for plant in self.plants:
                line = f"- {plant.name}: {plant.height}cm"
                if isinstance(plant, FloweringPlant):
                    if plant.color:
                        line += f", {plant.color} flowers"
                    if plant.blooming:
                        line += " (blooming)"
                if isinstance(plant, PrizeFlower):
                    line += f", Prize points: {plant.prize_points}"
                print(line)

            stats = GardenManager.GardenStats(self)
            stats.count_plant_types()
            stats.check_height_validity()
            print(
                f"\nPlants added: {stats.total_plants},"
                f" Total growth: {self.total_growth}cm"
            )
            print(
                f"Plant types: {stats.regular} regular,"
                f" {stats.flowering} flowering,"
                f" {stats.prize} prize flowers"
            )
            print(f"\nHeight validation test: {stats.height_validation}")

            print("Garden scores - ", end="")
            scores = []
            for garden in all_gardens:
                stats = GardenManager.GardenStats(garden)
                score = stats.garden_scores()
                scores.append(f"{garden.owner}: {score}")

            print(", ".join(scores))

    class GardenStats:
        """Helper class for calculating garden statistics."""
        def __init__(self, garden):
            """
            Initialize GardenStats.

            Args:
                garden (GardenManager.Garden): The garden to analyze.
            """
            self.garden = garden

        def count_plant_types(self):
            """Count regular, flowering, and prize plants in the garden."""
            self.regular = 0
            self.flowering = 0
            self.prize = 0
            self.total_plants = 0
            for plant in self.garden.plants:
                if isinstance(plant, PrizeFlower):
                    self.prize += 1
                elif isinstance(plant, FloweringPlant):
                    self.flowering += 1
                elif isinstance(plant, Plant):
                    self.regular += 1
                self.total_plants += 1

        def check_height_validity(self):
            """Verify all plants have positive height."""
            self.height_validation = True
            for plant in self.garden.plants:
                if plant.height <= 0:
                    self.height_validation = False
                    break

        def garden_scores(self):
            """
            Calculate the total score for the garden.

            Returns:
                int: Total score including height, blooming bonus,
                and prize points.
            """
            score = 0
            for plant in self.garden.plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    if plant.blooming:
                        score += 15
                    score += plant.prize_points
                elif isinstance(plant, FloweringPlant):
                    if plant.blooming:
                        score += 15
            return score

    def welcome_message():
        """
        Print the welcome message for the Garden Management System.
        """
        print("=== Garden Management System Demo ===")

    welcome_message = staticmethod(welcome_message)

    def create_garden_network(cls):
        """
        Class method that creates a demo network of gardens,
        grows plants, and prints reports.
        """
        manager1 = cls()
        manager2 = cls()

        alice = cls.Garden("Alice")
        alice.add_plant(Plant("Oak Tree", 100))
        alice.add_plant(FloweringPlant("Rose", 25, "red", True))
        alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", True, 10))
        manager1.gardens.append(alice)

        alice.grow_all_plants()

        bob = cls.Garden("Bob")
        bob.add_plant(Plant("Willow", 40), False)
        bob.add_plant(FloweringPlant("Daisy", 52, "white", False), False)
        manager2.gardens.append(bob)

        all_gardens = manager1.gardens + manager2.gardens

        alice.report(all_gardens)

        print(f"Total gardens managed: {cls.total_gardens}")

    create_garden_network = classmethod(create_garden_network)


if __name__ == "__main__":
    """Run the Garden Management System demo."""
    GardenManager.welcome_message()
    GardenManager.create_garden_network()
