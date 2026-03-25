"""
Stage 4: Ingredient Analyzer
============================
Concepts: Loops, list comprehensions, combining previous stages

To test your work:
    uv run python stages/stage4_analyzer.py

Your Task:
----------
Create functions that analyze a list of ingredients using the database and
return analyzed Ingredient objects.

Learning Objectives:
- Use for loops and list comprehensions
- Combine classes and functions from previous stages
- Transform data from one format to another
"""

from pathlib import Path
from stages.stage2_ingredient import Ingredient, create_unknown_ingredient
from stages.stage3_database import IngredientDatabase


def analyze_single_ingredient(name: str, database: IngredientDatabase) -> Ingredient:
    """
    Analyze a single ingredient using the database.

    Args:
        name: The ingredient name to analyze
        database: An IngredientDatabase instance

    Returns:
        An Ingredient object with data from the database,
        or an "unknown" ingredient if not found.

    Example:
        >>> db = IngredientDatabase("data/ingredients_db.json")
        >>> result = analyze_single_ingredient("sugar", db)
        >>> result.category
        'harmful'
        >>> result.found_in_database
        True

        >>> result = analyze_single_ingredient("mystery powder", db)
        >>> result.category
        'unknown'
        >>> result.found_in_database
        False
    """
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


    # 1. Look up the ingredient in the database using database.lookup()
    # 2. If found, create an Ingredient with the database data
    # 3. If not found, use create_unknown_ingredient()
    #
    # Hints:
    # - database.lookup() returns a dict or None
    # - The dict has keys: 'category', 'health_score', 'description'
    # - Set found_in_database=True when found, False otherwise
    #
    # Delete the line below and write your implementation:
   
    # ============================================================


def analyze_ingredients(
    ingredient_names: list[str], database: IngredientDatabase
) -> list[Ingredient]:
    """
    Analyze a list of ingredients and return Ingredient objects.

    Args:
        ingredient_names: List of ingredient names to analyze
        database: An IngredientDatabase instance

    Returns:
        A list of Ingredient objects, one for each input name.

    Example:
        >>> db = IngredientDatabase("data/ingredients_db.json")
        >>> results = analyze_ingredients(["water", "sugar", "mystery"], db)
        >>> len(results)
        3
        >>> results[0].category
        'healthy'
        >>> results[1].category
        'harmful'
        >>> results[2].category
        'unknown'
    """
    
    # ============================================================
    # Use a list comprehension or for loop to analyze each ingredient.
    #
    # Option 1 - List comprehension (1 line):
    #   return [analyze_single_ingredient(name, database) for name in ingredient_names]
    #
    # Option 2 - For loop:
    #   results = []
    #   for name in ingredient_names:
    #       results.append(analyze_single_ingredient(name, database))
    #   return results
    #
    # Delete the line below and write your implementation:
    return [analyze_single_ingredient(name, database) for name in ingredient_names]
    # ============================================================


def filter_by_category(
    ingredients: list[Ingredient], category: str
) -> list[Ingredient]:
    """
    Filter ingredients by category.

    Args:
        ingredients: List of Ingredient objects
        category: The category to filter by ("healthy", "moderate", "harmful", "unknown")

    Returns:
        A list containing only ingredients matching the specified category.

    Example:
        >>> ingredients = [
        ...     Ingredient(name="water", category="healthy", health_score=10, description="", found_in_database=True),
        ...     Ingredient(name="sugar", category="harmful", health_score=2, description="", found_in_database=True),
        ... ]
        >>> healthy = filter_by_category(ingredients, "healthy")
        >>> len(healthy)
        1
        >>> healthy[0].name
        'water'
    """
   
    # ============================================================
    # Use a list comprehension to filter ingredients where ing.category == category
    #
    # Delete the line below and write your implementation:
    return [ing for ing in ingredients if ing.category == category]
    # ============================================================


def sort_by_health_score(
    ingredients: list[Ingredient], ascending: bool = True
) -> list[Ingredient]:
    """
    Sort ingredients by health score.

    Args:
        ingredients: List of Ingredient objects
        ascending: If True, sort from lowest to highest score.
                   If False, sort from highest to lowest.

    Returns:
        A new sorted list of ingredients (does not modify original).

    Example:
        >>> ingredients = [
        ...     Ingredient(name="sugar", category="harmful", health_score=2, description="", found_in_database=True),
        ...     Ingredient(name="water", category="healthy", health_score=10, description="", found_in_database=True),
        ... ]
        >>> sorted_asc = sort_by_health_score(ingredients, ascending=True)
        >>> sorted_asc[0].name
        'sugar'
        >>> sorted_desc = sort_by_health_score(ingredients, ascending=False)
        >>> sorted_desc[0].name
        'water'
    """
    # ============================================================
    # TODO: YOUR CODE HERE
    # ============================================================
    # Use the sorted() function with a key parameter
    #
    # Hints:
    # - sorted(list, key=lambda x: x.attribute) sorts by an attribute
    # - sorted(list, key=..., reverse=True) sorts in descending order
    # - 'ascending=True' means reverse=False
    #
    # Delete the line below and write your implementation:
    return sorted (ingredients, key=lambda ing: ing.health_score, reverse=not ascending)
    # ============================================================


def is_implemented() -> bool:
    """Check if this stage is implemented."""
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
