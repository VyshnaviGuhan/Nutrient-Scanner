import json
from pathlib import Path
from typing import Optional


class IngredientDatabase:
    
    def __init__(self, json_path: str):
       
        self.json_path = json_path

        with open(json_path, 'r') as file:
            data = json.load(file)

        
        self._ingredients: dict = data["ingredients"]
        self._categories: dict = data["categories"]
    
        

    def lookup(self, ingredient_name: str) -> Optional[dict]:
        
        return self._ingredients.get(ingredient_name.lower())
    
    
        
    
    
        



        # 1. Convert ingredient_name to lowercase for case-insensitive lookup
        # 2. Use .get() to safely retrieve from self._ingredients
        # 3. Return the ingredient data dict, or None if not found
        #
        # Delete the line below and write your implementation:
       
        # ============================================================

    def get_all_ingredients(self) -> list[str]:
        """
        Get a list of all ingredient names in the database.

        Returns:
            A sorted list of all ingredient names.

        Example:
            >>> db.get_all_ingredients()[:3]
            ['almonds', 'apple', 'apple cider vinegar']
        """
        
        # Return a sorted list of all keys in self._ingredients
        #
        # Delete the line below and write your implementation:
        return sorted(self._ingredients.key())
        # ============================================================

    def get_category_info(self, category: str) -> Optional[dict]:
        """
        Get information about a category.

        Args:
            category: The category name ("healthy", "moderate", or "harmful")

        Returns:
            A dictionary with 'color', 'description', and 'score_range' keys,
            or None if the category doesn't exist.
        """
        
        # Use .get() to safely retrieve from self._categories
        #
        # Delete the line below and write your implementation:
        return self. _categories.get(category)
        # ============================================================

    def __len__(self) -> int:
        """Return the number of ingredients in the database."""
        return len(self._ingredients)

    def __contains__(self, ingredient_name: str) -> bool:
        """Check if an ingredient is in the database (case-insensitive)."""
        return ingredient_name.lower() in self._ingredients


def is_implemented() -> bool:
    """Check if this stage is implemented."""
    try:
        db_path = Path(__file__).parent.parent / "data" / "ingredients_db.json"
        db = IngredientDatabase(str(db_path))
        return not getattr(db, "_not_implemented", False) and len(db) > 0
    except Exception:
        return False


if __name__ == "__main__":
    db_path = Path(__file__).parent.parent / "data" / "ingredients_db.json"

    print(f"Loading database from: {db_path}")
    db = IngredientDatabase(str(db_path))

    print(f"\nDatabase contains {len(db)} ingredients")
    print(f"\nFirst 5 ingredients: {db.get_all_ingredients()[:5]}")

    print("\nLooking up 'sugar':")
    result = db.lookup("sugar")
    print(f"  {result}")

    print("\nLooking up 'Sugar' (uppercase):")
    result = db.lookup("Sugar")
    print(f"  {result}")

    print("\nLooking up 'unknown_ingredient':")
    result = db.lookup("unknown_ingredient")
    print(f"  {result}")

    print("\nCategory info for 'healthy':")
    print(f"  {db.get_category_info('healthy')}")

    print("\nUsing 'in' operator:")
    print(f"  'water' in db: {'water' in db}")
    print(f"  'unicorn tears' in db: {'unicorn tears' in db}")
