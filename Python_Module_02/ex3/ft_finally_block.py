#!/usr/bin/env python3

def water_plants(plant_list):
    """
        Water each plant in the list and always close
        the watering system.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as err:
        print(f"Error: {err}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test normal and error cases to show that cleanup always runs."""
    print("\nTesting normal watering...")
    plant_list = ("tomato", "lettuce", "carrots")
    water_plants(plant_list)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    plant_list = ("tomato", None, "carrots")
    water_plants(plant_list)


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
