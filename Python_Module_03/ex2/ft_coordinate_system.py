#!/usr/bin/env python3

import sys
import math

print("=== Game Coordinate System ===\n")
position = (10, 20, 5)
start = (0, 0, 0)

x1, y1, z1 = start
x2, y2, z2 = position

distances = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

print(f"Position created: {position}")
print(f"Distance between {start} and {position}: {distances:.2f}\n")

for i in range(1, len(sys.argv)):
    try:
        position = tuple(int(n) for n in sys.argv[i].split(","))
        print(f"Parsing coordinates: \"{sys.argv[i]}\"")

        x2, y2, z2 = position
        print(f"Position position: {position}")

        distances = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        print(f"Distance between {start} and {position}: {distances:.1f}\n")

    except ValueError as err:
        print(f"Parsing invalid coordinates: \"{sys.argv[i]}\"")
        print(f"Error parsing coordinates: {err}")
        print("Error details - Type: "
              f"{type(err).__name__}, Args: (\"{err}\",)\n")

print("Unpacking demonstration:")
print(f"Player at x={x2}, y={y2}, z={z2}")
print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")
