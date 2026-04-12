from typing import Callable





def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target}"

def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int)-> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified
    
def conditional_caster(condition: Callable, spell: Callable)-> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional

def spell_sequence(spells: list[Callable])-> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def strong_target(target: str, power: int) -> bool:
    return power > 10


# Testing spell combiner...
# Combined spell result: Fireball hits Dragon, Heals Dragon
# Testing power amplifier...
# Original: 10, Amplified: 30


# def main():
#     print("Testing spell combiner...")
#     combined = spell_combiner(fireball, heal)
#     print("Combined spell result:", combined(test_targets[0]))
#     print("\nTesting power amplifier...")
#     amp = power_amplifier(damage_spell, 3)
#     for n in test_values:
#         print(f"Original: {n}, Amplified: {amp(n)}")

#     print("\nTesting conditional caster...")
#     check = conditional_caster(strong_only, heal)
#     for n in test_targets:
#         print(f"can I heal this target {n}: {check(n)}")
#     print("\nTesting spell sequence...")
#     run = spell_sequence([fireball, heal, strong_only])
#     for v in test_targets:
#         print(f"casting all spells: {run(v)}")
def main():
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")


    print("\nTesting power amplifier...")
    amplified = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}, Amplified: {amplified()}")


# def main():
#     print("\nTesting spell combiner...")

#     c = spell_combiner(fireball, heal)()
#     print(f"Combined spell result: {c[0]}, {c[1]}")

#     print("\nTesting power amplifier...")
#     d = power_amplifier(spell, 3)
#     print(f"Original: {spell()}, Ampified: {d()}")

if __name__ == "__main__":
    main()

# $> python3 higher_magic.py
# Testing spell combiner...
# Combined spell result: Fireball hits Dragon, Heals Dragon

# Testing power amplifier...
# Original: 10, Amplified: 30


# test_values = [14, 6, 10]
# test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


# def fireball(target: str) -> str:
#     return f"Fireball hits {target}"


# def heal(target: str) -> str:
#     return f"Heals {target}"


# def damage_spell(power: int) -> int:
#     return power


# def strong_only(target: str) -> bool:
#     return target == "Knight"


# def spell_combiner(spell1: callable, spell2: callable) -> callable:
#     def combined(arg):
#         res1 = spell1(arg)
#         res2 = spell2(arg)
#         return (res1, res2)
#     return combined


# def power_amplifier(base_spell: callable, multiplier: int) -> callable:
#     def amplifier(arg):
#         return base_spell(arg) * multiplier
#     return amplifier


# def conditional_caster(condition: callable, spell: callable) -> callable:
#     def check_condition(arg):
#         if condition(arg):
#             return spell(arg)
#         else:
#             return "Spell fizzled"
#     return check_condition


# def spell_sequence(spells: list[callable]) -> callable:
#     def run_all(arg):
#         res = []
#         for s in spells:
#             res.append(s(arg))
#         return res
#     return run_all


# def main():
#     print("Testing spell combiner...")
#     combined = spell_combiner(fireball, heal)
#     print("Combined spell result:", combined(test_targets[0]))
#     print("\nTesting power amplifier...")
#     amp = power_amplifier(damage_spell, 3)
#     for n in test_values:
#         print(f"Original: {n}, Amplified: {amp(n)}")

#     print("\nTesting conditional caster...")
#     check = conditional_caster(strong_only, heal)
#     for n in test_targets:
#         print(f"can I heal this target {n}: {check(n)}")
#     print("\nTesting spell sequence...")
#     run = spell_sequence([fireball, heal, strong_only])
#     for v in test_targets:
#         print(f"casting all spells: {run(v)}")


# if __name__ == "__main__":
#     main()








# def spell_combiner(spell1: callable, spell2: callable) -> callable:
#     def combiner(*args, **kwargs):
#         return (spell1(*args, **kwargs), spell2(*args, **kwargs))
#     return combiner


# def power_amplifier(base_spell: callable, multiplier: int) -> callable:
#     def combiner(*args, **kwargs):
#         return base_spell(*args, **kwargs) * multiplier

#     return combiner


# def conditional_caster(condition: callable, spell: callable) -> callable:
#     def combiner(*args, **kwargs):
#         if conditional_caster(*args, **kwargs):
#             return spell(*args, **kwargs)
#         else:
#             return "Spell fizzled"

#     return combiner


# def spell_sequence(spells: list[callable]) -> callable:
#     def combiner(*args, **kwargs):
#         return [i(*args, **kwargs) for i in spells]

#     return combiner


# def fireball():
#     return "Fireball hits Dragon"


# def heal():
#     return "Heals Dragon"


# def spell():
#     return 10


# def main():
#     print("\nTesting spell combiner...")

#     c = spell_combiner(fireball, heal)()
#     print(f"Combined spell result: {c[0]}, {c[1]}")

#     print("\nTesting power amplifier...")
#     d = power_amplifier(spell, 3)
#     print(f"Original: {spell()}, Ampified: {d()}")


# if __name__ == "__main__":
#     main()