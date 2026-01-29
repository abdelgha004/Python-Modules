#!/usr/bin/env python3gs


def check_temperature(temp_str):
    """
    Validate and analyze a temperature input.

    Parameters:
        temp_str (str): Temperature value received as a string.

    Returns:
        str: A message describing whether the temperature is valid,
            too hot, too cold, or invalid input.
    """

    try:
        number = int(temp_str)
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"

    if 0 <= number <= 40:
        return f"Temperature {number}°C is perfect for plants!"
    elif number > 40:
        return f"Error: {number}°C is too hot for plants (max 40°C)"
    else:
        return f"Error: {number}°C is too cold for plants (min 0°C)"


def test_temperature_input():
    """
    Test the check_temperature function with different inputs
    to ensure the program handles errors without crashing.
    """
    print("=== Garden Temperature Checker ===\n")

    temperatures = ["25", "abc", "100", "-50"]

    for temp in temperatures:
        print(f"Testing temperature: {temp}")
        print(f"{check_temperature(temp)}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
