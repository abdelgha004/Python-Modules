#!/usr/bin/env python3

class GardenError(Exception):
    """Base error for all garden problems"""
    pass


class PlantError(GardenError):
    """Raised when there is a problem adding a plant"""
    pass


class WaterError(GardenError):
    """Raised when there is a problem watering plants"""
    pass


class PlantHealthError(GardenError):
    """Raised when plant health conditions are invalid"""
    pass


class GardenManager:
    """Manages garden operations: adding plants, watering, and health checks"""

    def add_plant(self, plant_list):
        """Add plants to the garden; reports errors for invalid names"""
        print("\nAdding plants to garden...")
        for plant in plant_list:
            try:
                if not plant:
                    raise PlantError("Plant name cannot be empty!")
                print(f"Added {plant} successfully")
            except PlantError as err:
                print(f"Error adding plant: {err}")

    def water_plants(self, plant_list):
        """Water each plant and ensure cleanup even if errors occur"""
        try:
            print("\nWatering plants...")
            print("Opening watering system")
            for plant in plant_list:
                if not plant:
                    raise WaterError("Cannot water None - invalid plant!")
                print(f"Watering {plant} - success")
        except WaterError as err:
            print(f"Error: {err}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plants_health(self, plant_name, water_level, sunlight_hours):
        """
        Check plant water and sunlight levels;
        raise errors for invalid values
        """
        try:
            if water_level > 10:
                raise PlantHealthError(f"Water level {water_level}"
                                       " is too high (max 10)")
            elif water_level < 1:
                raise PlantHealthError(f"Water level {water_level}"
                                       " is too low (min 1)")
            if sunlight_hours > 12:
                raise PlantHealthError(
                    f"Sunlight hours {sunlight_hours}"
                    " is too high (max 12)")
            elif sunlight_hours < 2:
                raise PlantHealthError(
                    f"Sunlight hours {sunlight_hours}"
                    " is too low (min 2)")

            print(f"{plant_name}: healthy (water: "
                  f"{water_level}, sun: {sunlight_hours})")
        except PlantHealthError as err:
            print(f"Error checking {plant_name}: {err}")


if __name__ == "__main__":
    print("=== Garden Management System ===")
    manager = GardenManager()
    manager.add_plant(("tomato", "lettuce", ""))
    manager.water_plants(("tomato", "lettuce"))

    print("\nChecking plant health...")
    manager.check_plants_health("tomato", 5, 8)
    manager.check_plants_health("lettuce", 15, 8)

    print("\nTesting error recovery...")
    try:
        water = -1
        if water < 1:
            raise WaterError("Not enough water in tank")
    except GardenError as err:
        print(f"Caught GardenError: {err}")

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")
