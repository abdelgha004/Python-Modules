#!/usr/bin/env python3

players_inventory = {
    "alice": {"sword": 1, "potion": 5, "shield": 1},
    "bob": {"magic_ring": 1, "potion": 0}
    }

item_catalog = {
    "sword": {"type": "weapon", "value": 500, "rarity": "rare"},
    "potion": {"type": "consumable", "value": 50, "rarity": "common"},
    "shield": {"type": "armor", "value": 200, "rarity": "uncommon"},
    "magic_ring": {"type": "accessory", "value": 200, "rarity": "rare"},
}

print("=== Player Inventory System ===\n")
print("=== Alice's Inventory ===")
inventory_value = 0
item_count = 0
weapon = 0
consumable = 0
armor = 0

for item, qty in players_inventory["alice"].items():
    info = item_catalog.get(item)
    total = qty * info["value"]
    inventory_value += total
    item_count += qty
    if info["type"] == "weapon":
        weapon += qty
    elif info["type"] == "consumable":
        consumable += qty
    elif info["type"] == "armor":
        armor += qty
    print(f"{item} ({info['type']}, {info['rarity']}): "
          f"{qty}x @ {info['value']} gold each = {total} gold")


print(f"\nInventory value: {inventory_value} gold")
print(f"Item count: {item_count} items")
print(f"Categories: weapon({weapon}),"
      f" consumable({consumable}), armor({armor})")

print("\n=== Transaction: Alice gives Bob 2 potions ===")
if players_inventory["alice"]["potion"] >= 2:
    players_inventory["alice"]["potion"] -= 2
    bob_potion = players_inventory["bob"].get("potion", 0)
    players_inventory["bob"].update({"potion": bob_potion + 2})
    print("Transaction successful!")
else:
    print("Transaction failed!")

print("\n=== Updated Inventories ===")
print(f"Alice potions: {players_inventory['alice']['potion']}")
print(f"Bob potions: {players_inventory['bob']['potion']}")

print("\n=== Inventory Analytics ===")

most_value_player = ""
most_items_player = ""
max_value = 0
max_items = 0
rare_items = []
for player, inv in players_inventory.items():
    total_value = 0
    total_items = 0

    for item, qty in inv.items():
        info = item_catalog.get(item)
        if info:
            total_value += qty * info["value"]
            total_items += qty

            if info["rarity"] == "rare" or info["rarity"] == "legendary":
                rare_items.append(item)
    if total_value > max_value:
        max_value = total_value
        most_value_player = player

    if total_items > max_items:
        max_items = total_items
        most_items_player = player
print(f"Most valuable player: "
      f"{most_value_player.capitalize()} ({max_value} gold)")
print(f"Most items: {most_items_player.capitalize()} ({max_items} items)")
print(f"Rarest items: {', '.join(rare_items)}")
