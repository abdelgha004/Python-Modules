#!/usr/bin/env python3

class GardenError(Exception):
    """Base error for all garden problems"""
    pass


class PlantError(GardenError):
    """Error related to plants"""
    pass


class WaterError(GardenError):
    """Error related to watering"""
    pass


def test_plant_problem():
    """Simulate a plant problem"""
    raise PlantError("The tomato plant is wilting!")


def test_water_problem():
    """Simulate a watering problem"""
    raise WaterError("Not enough water in the tank!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        test_plant_problem()
    except PlantError as err:
        print(f"Caught PlantError: {err}")

    try:
        print("\nTesting WaterError...")
        test_water_problem()
    except WaterError as err:
        print(f"Caught WaterError: {err}")

    print("\nTesting catching all garden errors...")
    for func in [test_plant_problem, test_water_problem]:
        try:
            func()
        except GardenError as err:
            print(f"Caught a garden error: {err}")

    print("\nAll custom error types work correctly!")
