import math

print("=== Game Coordinate System ===\n")
position = (10, 20, 5)
start = (0, 0, 0)

x1, y1, z1 = start
x2, y2, z2 = position

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

print(f"Position created: {position}")
print(f"Distance between {start} and {position}: {distance:.2f}\n")

coordinate_strings = ["3,4,0", "abc,def,ghi"]

for coord_str in coordinate_strings:
    try:
        numbers = []
        for n in coord_str.split(","):
            numbers.append(int(n))
        position = tuple(numbers)
        print(f"Parsing coordinates: \"{coord_str}\"")

        x2, y2, z2 = position
        print(f"Parsed position: {position}")

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"Distance between {start} and {position}: {distance:.1f}\n")

    except ValueError as err:
        print(f"Parsing invalid coordinates: \"{coord_str}\"")
        print(f"Error parsing coordinates: {err}")
        print("Error details - Type: "
              f"{type(err).__name__}, Args: (\"{err}\",)\n")

print("Unpacking demonstration:")
print(f"Player at x={x2}, y={y2}, z={z2}")
print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
