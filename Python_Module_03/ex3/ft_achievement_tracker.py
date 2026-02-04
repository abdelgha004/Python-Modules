#!/usr/bin/env python3



alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob =  {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}


# data={
# 'alice' : {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'},
# 'bob' :  {'first_kill', 'level_10', 'boss_slayer', 'collector'},
# 'charlie' : {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
# }

print("=== Achievement Tracker System ===\n")
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

total = alice.union(bob, charlie)
print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {total}")
print(f"Total unique achievements: {len(total)}\n")

# Common to all players: {'level_10'}
# Rare achievements (1 player): {'collector', 'perfectionist'}


print(f"Alice vs Bob common: {alice.difference(bob)}")
# Alice vs Bob common: {'first_kill', 'level_10'}
# Alice unique: {'speed_demon', 'treasure_hunter'}
# Bob unique: {'boss_slayer', 'collector'}