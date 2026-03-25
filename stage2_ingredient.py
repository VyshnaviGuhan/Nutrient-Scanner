"""
Stage 2: Ingredient Data Class
==============================
Concepts: Classes, dataclasses, type hints

To test your work:
    uv run python stages/stage2_ingredient.py

Your Task:
----------
Create an Ingredient dataclass that represents a single analyzed ingredient.

Learning Objectives:
- Use the @dataclass decorator
- Define class attributes with type hints
- Understand when to use dataclasses vs regular classes
- Use default values in dataclass fields
"""

from dataclasses import dataclass



@dataclass
class Ingredient:
    """
    Represents a single ingredient with its health analysis.

    Requirements:
    1. Define the following fields with appropriate types:
       - name: str (the ingredient name, required)
       - category: str (one of "healthy", "moderate", "harmful", or "unknown")
       - health_score: int (0-10 scale, where 10 is healthiest)
       - description: str (explanation of why it's healthy/harmful)
       - found_in_database: bool (whether the ingredient was found in our database)

    2. Set sensible default values:
       - category should default to "unknown"
       - health_score should default to 5
       - description should default to "No information available"
       - found_in_database should default to False

    Example usage:
        >>> ing = Ingredient(name="sugar")
        >>> ing.name
        'sugar'
        >>> ing.category
        'unknown'

        >>> ing2 = Ingredient(
        ...     name="water",
        ...     category="healthy",
        ...     health_score=10,
        ...     description="Essential for hydration",
        ...     found_in_database=True
        ... )
        >>> ing2.health_score
        10
    """

    name: str
    category: str = "unknown" 
    health_score: int = 5
    description: str = "No information available"
    found_in_database: bool = False



    # Define the dataclass fields below.
    #
    # Hints:
    # 1. Use type hints for each field (e.g., name: str)
    # 2. For default values, simply assign them (e.g., category: str = "unknown")
    # 3. Required fields (no default) must come before fields with defaults
    #
    # Delete the placeholder below and define your fields:


    # Add the remaining fields here:
    # category: str = ...
    # health_score: int = ...
    # description: str = ...
    # found_in_database: bool = ...

    # ============================================================


def create_unknown_ingredient(name: str) -> Ingredient:
    
    
    """
    Factory function to create an Ingredient that wasn't found in the database.

    Args:
        name: The ingredient name

    Returns:
        An Ingredient instance with default "unknown" values

    Example:
        >>> ing = create_unknown_ingredient("mystery powder")
        >>> ing.name
        'mystery powder'
        >>> ing.found_in_database
        False
   
       """
    
           
    # Create and return an Ingredient instance with:
    # - The given name
    # - All other fields at their default values
    #
    # This should be a single line once your Ingredient class is defined!
    #
    # Delete the line below and write your implementation:
    return Ingredient(name=name)
    # ============================================================


def is_implemented() -> bool:
    """Check if this stage is implemented."""
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
