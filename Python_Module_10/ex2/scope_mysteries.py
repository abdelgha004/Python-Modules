
initial_powers = [20, 47, 79]
power_additions = [16, 5, 12, 9, 7]
enchantment_types = ['Earthen', 'Flaming', 'Flowing']
items_to_enchant = ['Amulet', 'Sword', 'Wand', 'Staff']


def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def add_power(total):
        nonlocal power
        power += total
        return power
    return add_power


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item):
        return f"{enchantment_type} {item}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main():
    print("Testing mage counter...")
    c = mage_counter()
    for i in range(1, 3 + 1):
        print(f"Call {i}:", c())

    print("\nTesting spell accumulator...")
    p = spell_accumulator(initial_powers[0])
    print(f"Initial power {initial_powers[0]}: accumulated power {p(10)}")

    print("\nTesting enchantant factory...")
    e = enchantment_factory(enchantment_types[1])
    for i in items_to_enchant:
        print(e(i))

    print("\nTesting memory vault...")
    function_dict = memory_vault()
    function_dict["store"]("color", "blue")
    print(function_dict["recall"]("color"))


if __name__ == "__main__":
    main()



# def mage_counter() -> callable:
#     x: int = 0

#     def count_mages() -> int:
#         nonlocal x
#         x += 1
#         return x
#     return count_mages


# def spell_accumulator(initial_power: int) -> callable:
#     x: int = initial_power

#     def add_number(power_to_add):
#         nonlocal x
#         x += power_to_add
#         return x
#     return add_number


# def enchantment_factory(enchantment_type: str) -> callable:
#     def fun(type_name):
#         return f"{enchantment_type} {type_name}"

#     return fun


# def memory_vault() -> dict[str, callable]:
#     def store(key, value):
#         dict[key] = value

#     def recall(key):
#         try:
#             return dict[key]
#         except KeyError:
#             return "Memory not found"

#     return {
#         'store': store,
#         'recall': recall
#         }


# def main():
#     print("\nTesting mage counter...")
#     x = mage_counter()
#     print(f"Call 1: {x()}")
#     print(f"Call 2: {x()}")
#     print(f"Call 3: {x()}")

#     print("\nTesting enchantment factory...")
#     print(enchantment_factory("Flaming")("Sword"))
#     print(enchantment_factory("Frozen")("Shield"))


# if __name__ == "__main__":
#     main()