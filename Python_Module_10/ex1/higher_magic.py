from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def damage_spell(target: str, power: int) -> int:
    return power


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def high_power_only(target: str, power: int) -> bool:
    return power >= 12


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 20)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell('Dragon', 10)},"
          f" Amplified: {amplified('Dragon', 10)}")

    print("\nTesting conditional caster...")
    caster = conditional_caster(high_power_only, lightning)
    print(caster("Knight", 10))
    print(caster("Dragon", 20))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, lightning])
    results = sequence("Knight", 10)
    for i, res in enumerate(results):
        print(f"Spell {i+1} result: {res}")


if __name__ == "__main__":
    main()
