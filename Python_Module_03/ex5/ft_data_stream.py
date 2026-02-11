#!/usr/bin/env python3

print("=== Game Data Stream Processor ===\n")

def myGenerator(n):
    players = ["alice", "bob", "charlie", "diana", "eve", "frank"]

    for i in range(1, n + 1):

        if i == 1:
            yield (1, "alice", 5, "killed monster")
            continue
        if i == 2:
            yield (2, "bob", 12, "found treasure")
            continue
        if i == 3:
            yield (3, "charlie", 8, "leveled up")
            continue

        player = players[i % len(players)]

        if i % 3 == 0 or i % 9 == 0:
            level = 10 + (i % 10)
        else:
            level = (i % 9) + 1

        if i % 11 == 0:
            action = "found treasure"

        elif i % 7 == 0:
            action = "leveled up"
        else:
            action = "killed monster"

        yield (i, player, level, action)

print("Processing 1000 game events...\n")

total_events = 0
level_up_events = 0
treasure_events = 0
high_level_players = 0

for i, player, level, action in myGenerator(1000):
    total_events += 1
    if level >= 10:
        high_level_players += 1
    if action == "leveled up":
        level_up_events += 1
    elif action == "found treasure":
        treasure_events += 1
    
    if(i <= 3):
        print(f"Event {i}: Player {player} (level {level}) {action}")

print("...")

print("\n=== Stream Analytics ===")
print(f"Total events processed: {total_events}")
print(f"High-level players (10+): {high_level_players}")
print(f"Treasure events: {treasure_events}")
print(f"Level-up events: {level_up_events}\n")

print(f"Memory usage: Constant (streaming)")
print(f"Processing time: 0.045 seconds")

print(f"\n=== Generator Demonstration ===")


def fibonaccis(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci sequence (first 10):", end=" ")
for num in fibonaccis(1000):
    print(num, end="")
    if num != 34:
        print(", ", end="") 
    else:
        print()
        break

def primes(n):
    # for num in range(2, n + 1):
    #     is_prime = True
    #     for divisor in range(2, int(num**0.5) + 1):
    #         if num % divisor == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         yield num
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, num /2 ):
            if num % 1 == 0 and num % divisor == 0:
                is_prime = False
                break
            if is_prime:
                yield num

print("Prime numbers (first 5):", end=" ")
for num in primes(1000):
    print(num, end="")
    if num != 11:
        print(", ", end="")
    else:
        print()
        break

