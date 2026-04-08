from pathlib import Path
from stages.stage2_ingredient import Ingredient, create_unknown_ingredient
from stages.stage3_database import IngredientDatabase


def analyze_single_ingredient(name: str, database: IngredientDatabase) -> Ingredient:
    data = database.lookup(name)
    if data:
        return Ingredient(
            name=name,
            category=data["category"],
            health_score=data["health_score"],
            description=data["description"],
            found_in_database=True
        )
    return create_unknown_ingredient(name)




def analyze_ingredients(
    ingredient_names: list[str], database: IngredientDatabase
) -> list[Ingredient]:
 
    
    
    return [analyze_single_ingredient(name, database) for name in ingredient_names]
    


def filter_by_category(
    ingredients: list[Ingredient], category: str
) -> list[Ingredient]:
   
   
    
    return [ing for ing in ingredients if ing.category == category]
  


def sort_by_health_score(
    ingredients: list[Ingredient], ascending: bool = True
) -> list[Ingredient]:
    
    
    return sorted (ingredients, key=lambda ing: ing.health_score, reverse=not ascending)
    


def is_implemented() -> bool:
    
    try:
        db_path = Path(__file__).parent.parent / "data" / "ingredients_db.json"
        db = IngredientDatabase(str(db_path))
        result = analyze_single_ingredient("water", db)
        return result.name != "__NOT_IMPLEMENTED__"
    except Exception:
        return False


if __name__ == "__main__":
    db_path = Path(__file__).parent.parent / "data" / "ingredients_db.json"
    db = IngredientDatabase(str(db_path))

    print("Testing analyze_single_ingredient()...")
    water = analyze_single_ingredient("water", db)
    print(f"  water: {water}")

    sugar = analyze_single_ingredient("sugar", db)
    print(f"  sugar: {sugar}")

    mystery = analyze_single_ingredient("mystery powder", db)
    print(f"  mystery: {mystery}")

    print("\nTesting analyze_ingredients()...")
    names = ["water", "sugar", "salt", "mystery powder"]
    results = analyze_ingredients(names, db)
    for ing in results:
        print(f"  {ing.name}: {ing.category} (score: {getattr(ing, 'health_score', 'N/A')})")

    print("\nTesting filter_by_category()...")
    harmful = filter_by_category(results, "harmful")
    print(f"  Harmful ingredients: {[i.name for i in harmful]}")

    print("\nTesting sort_by_health_score()...")
    sorted_results = sort_by_health_score(results, ascending=False)
    print(f"  Sorted (best first): {[(i.name, getattr(i, 'health_score', 'N/A')) for i in sorted_results]}")
