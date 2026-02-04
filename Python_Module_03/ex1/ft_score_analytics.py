#!/usr/bin/env python3

import sys

size = len(sys.argv)
if size > 1:
    numbers = []
    print("=== Player Score Analytics ===")
    for i in range(1, size):
        try:
            numbers.append(int(sys.argv[i]))
        except ValueError:
            print(f"oops, I typed '{sys.argv[i]}' instead of '1000'")
    size = len(numbers)
    if(size > 0):
        print(f"Scores processed: {numbers}")
        print(f"Total players: {size}")
        print(f"Total score: {sum(numbers)}")
        print(f"Average score: {sum(numbers) / (size)}")
        print(f"High score: {max(numbers)}")
        print(f"Low score: {min(numbers)}")
        print(f"Score range: {max(numbers) - min(numbers)}")
else:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")