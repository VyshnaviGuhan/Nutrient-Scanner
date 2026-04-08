
import time
from typing import Optional


class NutrientScannerError(Exception):

    pass


class InvalidIngredientError(NutrientScannerError):
    
    def __init__(self, ingredient_name: str, reason: str = ""):
        self.ingredient_name = ingredient_name
        message = f"Invalid ingredient name: '{ingredient_name}'"
        if reason:
            message += f" ({reason})"
        super().__init__(message)
    
   


class DatabaseNotFoundError(NutrientScannerError):
    

    def __init__(self, path: str):
        self.path = path
        super().__init__(f"Ingredient database not found at: {path}")


class APIError(NutrientScannerError):
    

    def __init__(self, message: str, status_code: Optional[int] = None, original_error: Optional[Exception] = None):
        self.status_code = status_code
        self.original_error = original_error
        full_message = f"API Error: {message}"
        if status_code:
            full_message += f" (status code: {status_code})"
        super().__init__(full_message)
    
    


class ImageProcessingError(NutrientScannerError):
    

    def __init__(self, message: str, image_size: Optional[int] = None):
        self.image_size = image_size
        if image_size:
            message = f"{message} (image size: {image_size} bytes)"
        super().__init__(message)


def validate_ingredient_name(name: str) -> str:
  
    cleaned = name.strip()

    if not cleaned:
        raise InvalidIngredientError(name, "empty or whitespace only")

    if len(cleaned) > 100:
        raise InvalidIngredientError(name, "exceeds 100 characters")

    if cleaned.isdigit():
        raise InvalidIngredientError(name, "contains only numbers")

    if not any(c.isalpha() for c in cleaned):
        raise InvalidIngredientError(name, "must contain at least one letter")

    return cleaned.lower()
   
    return name  


def safe_parse_ingredients(raw_text: str) -> tuple[list[str], list[str]]:
    
    valid_ingredients = []
    error_messages = []

    items = raw_text.split(",")

    for item in items:
        try:
            validated = validate_ingredient_name(item)
            valid_ingredients.append(validated)
        except InvalidIngredientError as e:
            error_messages.append(str(e))

    return (valid_ingredients, error_messages)
    
    return ([], [])  


def safe_api_call(func, *args, max_retries: int = 3, **kwargs):
  
    last_exception = None

    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            last_exception = e
            if attempt < max_retries - 1:
                time.sleep(1)

    
    raise APIError(
        f"All {max_retries} attempts failed",
        original_error=last_exception
    )
    


def is_implemented() -> bool:
   
    try:
        valid, errors = safe_parse_ingredients("Sugar, , Water")
        return len(valid) > 0 or len(errors) > 0
    except Exception:
        return False


if __name__ == "__main__":
    print("Stage 8: Exception Handling")
    print("=" * 40)

    print("\nTesting validate_ingredient_name()...")
    test_cases = [
        ("  Sugar  ", True),
        ("", False),
        ("   ", False),
        ("12345", False),
        ("a" * 101, False),
        ("Red 40", True),
    ]

    for name, should_pass in test_cases:
        try:
            result = validate_ingredient_name(name)
            status = "✓" if should_pass else "✗ (should have raised)"
            print(f"  {status} '{name}' -> '{result}'")
        except InvalidIngredientError as e:
            status = "✓" if not should_pass else "✗ (unexpected error)"
            print(f"  {status} '{name}' -> Error: {e}")

    print("\nTesting safe_parse_ingredients()...")
    raw = "Sugar, , Water, 12345, Salt, " + "a" * 101
    valid, errors = safe_parse_ingredients(raw)
    print(f"  Input: '{raw[:50]}...'")
    print(f"  Valid ingredients: {valid}")
    print(f"  Errors: {errors}")

    print("\nTesting custom exceptions...")
    try:
        raise DatabaseNotFoundError("/path/to/db.json")
    except NutrientScannerError as e:
        print(f"  Caught: {type(e).__name__}: {e}")

    try:
        raise ImageProcessingError("Image too large", image_size=10_000_000)
    except NutrientScannerError as e:
        print(f"  Caught: {type(e).__name__}: {e}")
