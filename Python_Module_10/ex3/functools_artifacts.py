
from functools import reduce, partial, lru_cache, singledispatch
import operator


spell_powers = [48, 44, 45, 49, 45, 34]
fibonacci_tests = [16, 15, 10]


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "sub": operator.sub,
        "min": lambda x, y: x if x < y else y,
        "max": lambda x, y: x if x > y else y,
    }
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightining")
    }


def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    print(f"counting...{n}")
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


memoized_fibonacci = lru_cache(maxsize=None)(memoized_fibonacci)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(arg):
        print(f"Unknown spell type: {arg}")

    @spell.register(int)
    def _(arg):
        print("damage spell")

    @spell.register(str)
    def _(arg):
        print("enchantment")

    @spell.register(list)
    def _(arg):
        print("multi-cast")

    return spell


def main():
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"sub: {spell_reducer(spell_powers, 'sub')}")
    print(f"min: {spell_reducer(spell_powers, 'min')}")
    print(f"max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power, element, target):
        return f"{element} enchantment ({power}) on {target}"

    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire_enchant"]("sword"))
    print(enchants["ice_enchant"]("wand"))
    print(enchants["lightning_enchant"]("staff"))
    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(10))
    print("\nTesting spell dispatcher...")
    s = spell_dispatcher()
    s(45)
    s("spell")
    s([1, 2, 3])
    s(12.23)


if __name__ == "__main__":
    main()




# from functools import reduce, partial, lru_cache, singledispatch
# from operator import add, mul

# def spell_reducer(spells: list[int], operation: str) -> int:
#     if operation == "add":
#         return reduce(lambda x, y: add(x, y), spells)
#     elif operation == "multiply":
#         return reduce(lambda x, y: mul(x, y), spells)
#     elif operation == "max":
#         return reduce(lambda x, y: max(x, y), spells)
#     elif operation == "min":
#         return reduce(lambda x, y: min(x, y), spells)
#     else:
#         print("Error: operation key should be add or multiply or max or min")

# def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    
#     return {
#         "fire_enchant": partial(base_enchantment, power=50, element="fire"),
#         "ice_enchant": partial(base_enchantment, power=50, element="ice"),
#         "lightning_enchant": partial(base_enchantment, power=50, element="lightning")
#         }

# @lru_cache
# def memoized_fibonacci(n: int) -> int:
#     if n == 1 or n == 0:
#         return n
#     return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


# def spell_dispatcher() -> callable:
#     @singledispatch
#     def fun(value):
#         print("Value:")
    
#     @fun.register(int)
#     def _(value: int):
    
#         return "damage spell"
    
#     @fun.register(str)
#     def _(value: str):
#         return "enchantment"
    
#     @fun.register(list)
#     def _(value: list):
#         return "multi-cast"
    

# def main():
#     print("\nTesting spell reducer...")
#     print("Sum:",spell_reducer([12,3,41,543,30], "add"))
#     print("Product:",spell_reducer([12,3,41,543,30], "multiply"))
#     print("Max:",spell_reducer([12,3,41,543,30], "max"))
#     print("Min:",spell_reducer([12,3,41,543,30], "min"))

#     print("\nTesting memoized fibonacci...")
#     n = 10
#     print(f"Fib({n})", memoized_fibonacci(n))
#     n = 15
#     print(f"Fib({n})", memoized_fibonacci(n))



# if __name__ == "__main__":
#     main()