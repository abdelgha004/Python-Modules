alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
charlie = {'level_10', 'treasure_hunter',
           'boss_slayer', 'speed_demon', 'perfectionist'}

print("=== Achievement Tracker System ===\n")
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

all_ach = alice.union(bob, charlie)

print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {all_ach}")
print(f"Total unique achievements: {len(all_ach)}\n")

all_common = alice.intersection(bob, charlie)
print(f"Common to all players: {all_common}")

ab_common = alice.intersection(bob)
ac_common = alice.intersection(charlie)
bc_common = bob.intersection(charlie)
shared_ach = ab_common.union(ac_common, bc_common)

rare_ach = all_ach.difference(shared_ach)
print(f"Rare achievements (1 player): {rare_ach}\n")

print(f"Alice vs Bob common: {alice.intersection(bob)}")
print(f"Alice unique: {alice.difference(bob)}")
print(f"Bob unique: {bob.difference(alice)}")
