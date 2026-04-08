import pandas as pd
from stages.stage2_ingredient import Ingredient


def ingredients_to_dataframe(ingredients: list[Ingredient]) -> pd.DataFrame:

    data = [
        {
            "name": ing.name,
            "category": ing.category,
            "health_score": ing.health_score,
            "description": ing.description,
            "found_in_database": ing.found_in_database,
        }
        for ing in ingredients
    ]
    return pd.DataFrame(data)


    
    
    return pd.DataFrame({"_not_implemented": [True]})
   


def filter_dataframe_by_category(
    df: pd.DataFrame, category: str
) -> pd.DataFrame:
    
    return df[df["category"] == category]
    
    
    return df
    


def sort_dataframe_by_score(
    df: pd.DataFrame, ascending: bool = False
) -> pd.DataFrame:
    
    return df.sort_values("health_score", ascending=ascending)

   
  


def get_summary_statistics(df: pd.DataFrame) -> dict:

    return {
        "total_count": len(df),
        "avg_score": df["health_score"].mean(),
        "min_score": df["health_score"].min(),
        "max_score": df["health_score"].max(),
        "category_counts": df["category"].value_counts().to_dict(),
    }

    
    
    return {
        "total_count": 0,
        "avg_score": 0.0,
        "min_score": 0,
        "max_score": 0,
        "category_counts": {},
    }
   


def is_implemented() -> bool:
    
    test_ings = [
        Ingredient(name="test", category="healthy", health_score=8, description="", found_in_database=True)
    ]
    df = ingredients_to_dataframe(test_ings)
    return "_not_implemented" not in df.columns


if __name__ == "__main__":
    test_ingredients = [
        Ingredient(name="water", category="healthy", health_score=10, description="Essential", found_in_database=True),
        Ingredient(name="sugar", category="harmful", health_score=2, description="Bad", found_in_database=True),
        Ingredient(name="salt", category="moderate", health_score=5, description="OK", found_in_database=True),
        Ingredient(name="mystery", category="unknown", health_score=5, description="Unknown", found_in_database=False),
    ]

    print("Testing ingredients_to_dataframe()...")
    df = ingredients_to_dataframe(test_ingredients)
    print(df)
    print()

    print("Testing filter_dataframe_by_category()...")
    healthy_df = filter_dataframe_by_category(df, "healthy")
    print(f"Healthy ingredients:\n{healthy_df}")
    print()

    print("Testing sort_dataframe_by_score()...")
    sorted_df = sort_dataframe_by_score(df, ascending=False)
    print(f"Sorted by score (highest first):\n{sorted_df}")
    print()

    print("Testing get_summary_statistics()...")
    stats = get_summary_statistics(df)
    print(f"Statistics: {stats}")
