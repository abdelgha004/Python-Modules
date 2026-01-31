#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Check if plant name, water level, and sunlight hours are valid.
    Prints an error message if any value is invalid.
    """
    try:
        if len(plant_name) == 0:
            raise ValueError("Plant name cannot be empty!")

        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif water_level < 1:
            raise ValueError(f"Water level {water_level} is too low (min 1)")

        if sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {sunlight_hours}"
                " is too high (max 12)")
        elif sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours}"
                " is too low (min 2)")

        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as err:
        print(f"Error: {err}")


def test_plant_checks():
    """
    Test check_plant_health with valid and invalid input values.
    """
    print("\nTesting good values...")
    check_plant_health("tomato", 5, 7)

    print("\nTesting empty plant name...")
    check_plant_health("", 5, 7)

    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 7)

    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
    print("\nAll error raising tests completed!")
