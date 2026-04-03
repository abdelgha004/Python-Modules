def validate_ingredients(ingredients: str) -> str:
    data = ingredients.split()
    for s in data:
        if s not in ["fire", "water", "earth", "air"]:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
