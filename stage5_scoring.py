"""
Stage 5: Health Scoring
=======================
Concepts: Functions, aggregation, mathematical operations

To test your work:
    uv run python stages/stage5_scoring.py

Your Task:
----------
Create functions to calculate overall health scores and generate
recommendations based on ingredient analysis.

Learning Objectives:
- Write functions with multiple parameters
- Aggregate data from a list (sum, average)
- Use conditional logic to generate recommendations
- Format output strings
"""

from stages.stage2_ingredient import Ingredient


def calculate_overall_score(ingredients: list[Ingredient]) -> float:
    """
    Calculate the overall health score for a list of ingredients.

    The overall score is the weighted average of all ingredient scores,
    where ingredients found in the database have weight 1.0 and unknown
    ingredients have weight 0.5 (we're less certain about them).

    Args:
        ingredients: List of analyzed Ingredient objects

    Returns:
        A float between 0 and 10 representing the overall health score.
        Returns 5.0 if the ingredient list is empty.

    Example:
        >>> ings = [
        ...     Ingredient(name="water", category="healthy", health_score=10,
        ...                description="", found_in_database=True),
        ...     Ingredient(name="sugar", category="harmful", health_score=2,
        ...                description="", found_in_database=True),
        ... ]
        >>> calculate_overall_score(ings)
        6.0  # (10 + 2) / 2 = 6.0
    """
    if not ingredients:
        return 5.0
    
    weighted_sum = 0.0
    total_weight = 0.0

    for ing in ingredients:
        weight = 1.0 if ing.found_in_database else 0.5
        weighted_sum += ing.health_score * weight
        total_weight += weight

    return weighted_sum / total_weight

    # ============================================================
    # 1. Handle edge case: return 5.0 if ingredients list is empty
    # 2. Calculate weighted sum: score * weight for each ingredient
    # 3. Calculate total weights
    # 4. Return weighted_sum / total_weights
    #
    # Hints:
    # - weight = 1.0 if ing.found_in_database else 0.5
    # - Be careful not to divide by zero
    #
    # Delete the line below and write your implementation:
    return -1.0  # Indicates not implemented
    # ============================================================


def get_score_label(score: float) -> str:
    """
    Convert a numeric score to a descriptive label.

    Args:
        score: A health score between 0 and 10

    Returns:
        A string label: "Excellent", "Good", "Fair", or "Poor"

    Score ranges:
        8-10: "Excellent"
        6-7.9: "Good"
        4-5.9: "Fair"
        0-3.9: "Poor"

    Example:
        >>> get_score_label(8.5)
        'Excellent'
        >>> get_score_label(5.0)
        'Fair'
    """
    if score >= 8:
        return "Excellent"
    elif score >= 6:
        return"Good"
    elif score >= 4:
        return "Fair"
    else:
        return "Poor"
    # ============================================================
    # Use if/elif/else to return the appropriate label based on score
    #
    # Delete the line below and write your implementation:
    
    # ============================================================


def count_by_category(ingredients: list[Ingredient]) -> dict[str, int]:
    """
    Count ingredients by category.

    Args:
        ingredients: List of analyzed Ingredient objects

    Returns:
        A dictionary with category names as keys and counts as values.

    Example:
        >>> ings = [
        ...     Ingredient(name="water", category="healthy", health_score=10, description="", found_in_database=True),
        ...     Ingredient(name="sugar", category="harmful", health_score=2, description="", found_in_database=True),
        ...     Ingredient(name="salt", category="moderate", health_score=5, description="", found_in_database=True),
        ...     Ingredient(name="oats", category="healthy", health_score=9, description="", found_in_database=True),
        ... ]
        >>> count_by_category(ings)
        {'healthy': 2, 'harmful': 1, 'moderate': 1}
    """
    counts= {}
    for ing in ingredients:
        counts[ing.category] = counts.get(ing.category, 0) +1
    return counts

    # ============================================================
    # 1. Create an empty dictionary for counts
    # 2. Loop through ingredients
    # 3. For each ingredient, increment the count for its category
    #
    # Hints:
    # - Use counts.get(category, 0) to get current count (default 0)
    # - Or use counts[category] = counts.get(category, 0) + 1
    #
    # Delete the line below and write your implementation:
    
    # ============================================================


def generate_recommendations(ingredients: list[Ingredient]) -> list[str]:
    """
    Generate health recommendations based on ingredient analysis.

    Args:
        ingredients: List of analyzed Ingredient objects

    Returns:
        A list of recommendation strings.

    Rules for generating recommendations:
    1. If there are 3+ harmful ingredients: "Consider choosing a healthier alternative"
    2. If there are any harmful ingredients: List them with "Watch out for: [names]"
    3. If there are unknown ingredients: "Unknown ingredients detected: [names]"
    4. If score >= 8: "Great choice! This product has healthy ingredients"
    5. Always return at least one recommendation

    Example:
        >>> ings = [
        ...     Ingredient(name="sugar", category="harmful", health_score=2, description="", found_in_database=True),
        ...     Ingredient(name="salt", category="moderate", health_score=5, description="", found_in_database=True),
        ... ]
        >>> recs = generate_recommendations(ings)
        >>> "Watch out for: sugar" in recs[0]
        True
    """
    recommendations = []
    
    harmful = [i.name for i in ingredients if i.category == "harmful"]
    unknown = [i.name for i in ingredients if i.category == "unknown"]
    score =  calculate_overall_score(ingredients)

    if len(harmful) >= 3:
        recommendations.append("Consider choosing a healthier a;ternative")

    if harmful:
        recommendations.append(f"Watch out for: {','. join (harmful)}")

    if unknown:
        recommendations.append(f"Unknown ingredients detected: {','. join(unknown)}")

    if score >= 8:
        recommendations.append("Great choice! This product has healthy ingredients")

    if not recommendations:
        recommendations.append("No specific concerns found")

    return recommendations
    # ============================================================
    # 1. Create an empty list for recommendations
    # 2. Find harmful ingredients: [i.name for i in ingredients if i.category == "harmful"]
    # 3. Find unknown ingredients: [i.name for i in ingredients if i.category == "unknown"]
    # 4. Calculate score using calculate_overall_score()
    # 5. Apply the rules above to add recommendations
    # 6. If no recommendations, add a default message
    #
    # Delete the line below and write your implementation:
    return ["Not implemented"]
    # ============================================================


def format_analysis_summary(ingredients: list[Ingredient]) -> str:
    """
    Create a formatted summary string of the ingredient analysis.

    Args:
        ingredients: List of analyzed Ingredient objects

    Returns:
        A formatted multi-line string summarizing the analysis.

    Example output:
        '''
        === Ingredient Analysis Summary ===
        Total ingredients: 4
        Overall health score: 6.5 (Good)

        Breakdown:
        - Healthy: 2
        - Moderate: 1
        - Harmful: 1
        '''
    """
    score = calculate_overall_score(ingredients)
    label = get_score_label(score)
    counts = count_by_category(ingredients)

    lines = []
    lines.append("=== Ingredient Analysis Summary ===")
    lines.append(f"Total ingredients: {len(ingredients)}")
    lines.append(f"Overall health score: {score:.1f} ({label})")
    lines.append("")
    lines.append("Breakdown:")

    for category, count in counts.items():
        lines.append(f"- {category.capitalize()}: {count}")
    
    return  "\n".join(lines)
    # ============================================================
    # Use string formatting to create a nice summary.
    # You can use f-strings and '\n' for newlines.
    #
    # Hints:
    # - Use calculate_overall_score() for the score
    # - Use get_score_label() for the label
    # - Use count_by_category() for the breakdown
    #
    # Delete the line below and write your implementation:
    return "Not implemented"
    # ============================================================


def is_implemented() -> bool:
    """Check if this stage is implemented."""
    score = calculate_overall_score([])
    return score != -1.0 and get_score_label(10.0) != "Not Implemented"


if __name__ == "__main__":
    test_ingredients = [
        Ingredient(name="water", category="healthy", health_score=10, description="Essential", found_in_database=True),
        Ingredient(name="sugar", category="harmful", health_score=2, description="Bad", found_in_database=True),
        Ingredient(name="salt", category="moderate", health_score=5, description="OK", found_in_database=True),
        Ingredient(name="mystery", category="unknown", health_score=5, description="Unknown", found_in_database=False),
    ]

    print("Testing calculate_overall_score()...")
    score = calculate_overall_score(test_ingredients)
    print(f"  Score: {score}")

    print("\nTesting get_score_label()...")
    for s in [9.0, 7.0, 5.0, 2.0]:
        print(f"  {s}: {get_score_label(s)}")

    print("\nTesting count_by_category()...")
    counts = count_by_category(test_ingredients)
    print(f"  Counts: {counts}")

    print("\nTesting generate_recommendations()...")
    recs = generate_recommendations(test_ingredients)
    for rec in recs:
        print(f"  - {rec}")

    print("\nTesting format_analysis_summary()...")
    summary = format_analysis_summary(test_ingredients)
    print(summary)
