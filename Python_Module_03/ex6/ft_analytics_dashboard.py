players = {
    "alice": 2300, "bob": 1800,
    "charlie": 2150, "diana": 2050
}

active_status = {
    "alice": True, "bob": True,
    "charlie": True, "diana": False
}

categories = {"high": 3, "medium": 2, "low": 1}

achievements = {
    "alice": ["first_kill", "level_10", "level_10",
              "first_kill", "boss_slayer"],
    "bob": ["first_kill", "level_10", "boss_slayer"],
    "charlie": ["boss_slayer", "level_10", "boss_slayer", "level_10",
                "first_kill", "level_10", "boss_slayer"]
}

regions = ["north", "east", "central", "north", "east"]

print("=== Game Analytics Dashboard ===")
print("\n=== List Comprehension Examples ===")
high_scorers = [name for name, score in players.items() if score > 2000]
score_doubled = [score * 2 for score in players.values()]
active_players = [name for name, active in active_status.items() if active]

print(f"High scorers (>2000): {high_scorers}")
print(f"Scores doubled: {score_doubled}")
print(f"Active players: {active_players}")

print("\n=== Dict Comprehension Examples ===")
player_scores = {name: score for name, score in players.items()
                 if name != "diana"}
score_categories = {name: value for name, value in categories.items()}
achievement_counts = {name: len(ach) for name, ach in achievements.items()}

print(f"Player scores: {player_scores}")
print(f"Score categories: {score_categories}")
print(f"Achievement counts: {achievement_counts}")

print("\n=== Set Comprehension Examples ===")
unique_players = {name for name in players.keys()}
unique_achievements = {a for ach_list in achievements.values()
                       for a in ach_list}
active_regions = {region for region in regions}

print(f"Unique players: {unique_players}")
print(f"Unique achievements: {unique_achievements}")
print(f"Active regions: {active_regions}")

print("\n=== Combined Analysis ===")
total_players = len(unique_players)
total_unique_achievements = len(unique_achievements)
average_score = sum(players.values()) / total_players
top_performer = max(players, key=players.get)

print(f"Total players: {total_players}")
print(f"Total unique achievements: {total_unique_achievements}")
print(f"Average score: {average_score}")
print(f"Top performer: {top_performer} ({players[top_performer]} points, "
      f"{len(achievements[top_performer])} achievements)")
