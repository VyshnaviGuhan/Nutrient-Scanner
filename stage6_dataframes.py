"""
Stage 6: DataFrames
===================
Concepts: Pandas DataFrames, data transformation, filtering, sorting

To test your work:
    uv run python stages/stage6_dataframes.py

Your Task:
----------
Create functions to convert ingredient analysis results to DataFrames
for better visualization and manipulation.

Learning Objectives:
- Create DataFrames from lists of objects
- Select and filter DataFrame rows
- Sort DataFrames
- Calculate summary statistics
"""

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


    """
    Convert a list of Ingredient objects to a pandas DataFrame.

    Args:
        ingredients: List of Ingredient objects

    Returns:
        A DataFrame with columns: name, category, health_score, description, found_in_database

    Example:
        >>> ings = [
        ...     Ingredient(name="water", category="healthy", health_score=10,
        ...                description="Essential", found_in_database=True),
        ...     Ingredient(name="sugar", category="harmful", health_score=2,
        ...                description="Bad", found_in_database=True),
        ... ]
        >>> df = ingredients_to_dataframe(ings)
        >>> df.columns.tolist()
        ['name', 'category', 'health_score', 'description', 'found_in_database']
        >>> len(df)
        2
    """
    # ============================================================
    # TODO: YOUR CODE HERE
    # ============================================================
    # 1. Create a list of dictionaries from the Ingredient objects
    # 2. Each dict should have keys: name, category, health_score, description, found_in_database
    # 3. Pass the list of dicts to pd.DataFrame()
    #
    # Hints:
    # - You can use a list comprehension:
    #   data = [{"name": ing.name, "category": ing.category, ...} for ing in ingredients]
    # - Or use dataclasses.asdict() if you want to be fancy
    #
    # Delete the line below and write your implementation:
    return pd.DataFrame({"_not_implemented": [True]})
    # ============================================================


def filter_dataframe_by_category(
    df: pd.DataFrame, category: str
) -> pd.DataFrame:
    
    return df[df["category"] == category]
    """
    Filter a DataFrame to show only ingredients of a specific category.

    Args:
        df: A DataFrame with ingredient data (must have 'category' column)
        category: The category to filter by

    Returns:
        A new DataFrame containing only rows matching the category.

    Example:
        >>> df = pd.DataFrame({
        ...     'name': ['water', 'sugar'],
        ...     'category': ['healthy', 'harmful'],
        ...     'health_score': [10, 2]
        ... })
        >>> filtered = filter_dataframe_by_category(df, 'healthy')
        >>> len(filtered)
        1
        >>> filtered.iloc[0]['name']
        'water'
    """
    # ============================================================
    # TODO: YOUR CODE HERE
    # ============================================================
    # Use boolean indexing: df[df['column'] == value]
    #
    # Delete the line below and write your implementation:
    return df
    # ============================================================


def sort_dataframe_by_score(
    df: pd.DataFrame, ascending: bool = False
) -> pd.DataFrame:
    
    return df.sort_values("health_score", ascending=ascending)

    """
    Sort a DataFrame by health_score.

    Args:
        df: A DataFrame with ingredient data (must have 'health_score' column)
        ascending: If True, sort lowest to highest. Default is False (highest first).

    Returns:
        A new DataFrame sorted by health_score.

    Example:
        >>> df = pd.DataFrame({
        ...     'name': ['sugar', 'water'],
        ...     'health_score': [2, 10]
        ... })
        >>> sorted_df = sort_dataframe_by_score(df, ascending=False)
        >>> sorted_df.iloc[0]['name']
        'water'
    """
    # ============================================================
    # TODO: YOUR CODE HERE
    # ============================================================
    # Use df.sort_values('column', ascending=...)
    #
    # Delete the line below and write your implementation:
   
    # ============================================================


def get_summary_statistics(df: pd.DataFrame) -> dict:

    return {
        "total_count": len(df),
        "avg_score": df["health_score"].mean(),
        "min_score": df["health_score"].min(),
        "max_score": df["health_score"].max(),
        "category_counts": df["category"].value_counts().to_dict(),
    }

    """
    Calculate summary statistics from the ingredient DataFrame.

    Args:
        df: A DataFrame with ingredient data

    Returns:
        A dictionary with summary statistics:
        - total_count: Total number of ingredients
        - avg_score: Average health score
        - min_score: Minimum health score
        - max_score: Maximum health score
        - category_counts: Dict of category -> count

    Example:
        >>> df = pd.DataFrame({
        ...     'name': ['water', 'sugar', 'salt'],
        ...     'category': ['healthy', 'harmful', 'moderate'],
        ...     'health_score': [10, 2, 5]
        ... })
        >>> stats = get_summary_statistics(df)
        >>> stats['total_count']
        3
        >>> stats['avg_score']
        5.666...
    """
    # ============================================================
    # TODO: YOUR CODE HERE
    # ============================================================
    # Use pandas methods:
    # - len(df) for total count
    # - df['health_score'].mean() for average
    # - df['health_score'].min() for minimum
    # - df['health_score'].max() for maximum
    # - df['category'].value_counts().to_dict() for category counts
    #
    # Delete the lines below and write your implementation:
    return {
        "total_count": 0,
        "avg_score": 0.0,
        "min_score": 0,
        "max_score": 0,
        "category_counts": {},
    }
    # ============================================================


def is_implemented() -> bool:
    """Check if this stage is implemented."""
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
