from dataclasses import dataclass



@dataclass
class Ingredient:
   

    name: str
    category: str = "unknown" 
    health_score: int = 5
    description: str = "No information available"
    found_in_database: bool = False


def create_unknown_ingredient(name: str) -> Ingredient:
  
    return Ingredient(name=name)

def is_implemented() -> bool:
   
    try:
        ing = Ingredient(name="test")
        return (
            ing.name != "__NOT_IMPLEMENTED__"
            and hasattr(ing, "category")
            and hasattr(ing, "health_score")
            and hasattr(ing, "description")
            and hasattr(ing, "found_in_database")
        )
    except Exception:
        return False


if __name__ == "__main__":
    print("Testing Ingredient dataclass...")

    ing1 = Ingredient(name="sugar")
    print(f"\nIngredient with only name:")
    print(f"  name: {ing1.name}")
    print(f"  category: {ing1.category}")
    print(f"  health_score: {ing1.health_score}")
    print(f"  description: {ing1.description}")
    print(f"  found_in_database: {ing1.found_in_database}")

    print("\nIngredient with all fields:")
    ing2 = Ingredient(
        name="water",
        category="healthy",
        health_score=10,
        description="Essential for hydration",
        found_in_database=True,
    )
    print(f"  {ing2}")

    print("\nUsing create_unknown_ingredient():")
    unknown = create_unknown_ingredient("mystery powder")
    print(f"  {unknown}")
