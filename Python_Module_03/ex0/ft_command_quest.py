#!/usr/bin/env python3

import sys

print("=== Command Quest ===")
count = len(sys.argv)
if count == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {count}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {count - 1}")

    for i in range(1, count):
        print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {count}")
