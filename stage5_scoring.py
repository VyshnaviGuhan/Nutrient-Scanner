from stages.stage2_ingredient import Ingredient


def calculate_overall_score(ingredients: list[Ingredient]) -> float:
    
    if not ingredients:
        return 5.0
    
    weighted_sum = 0.0
    total_weight = 0.0

    for ing in ingredients:
        weight = 1.0 if ing.found_in_database else 0.5
        weighted_sum += ing.health_score * weight
        total_weight += weight

    return weighted_sum / total_weight

    
    return -1.0  # Indicates not implemented
   


def get_score_label(score: float) -> str:
    
    if score >= 8:
        return "Excellent"
    elif score >= 6:
        return"Good"
    elif score >= 4:
        return "Fair"
    else:
        return "Poor"
    


def count_by_category(ingredients: list[Ingredient]) -> dict[str, int]:
   
    counts= {}
    for ing in ingredients:
        counts[ing.category] = counts.get(ing.category, 0) +1
    return counts

   


def generate_recommendations(ingredients: list[Ingredient]) -> list[str]:
    
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
    
    return ["Not implemented"]

def format_analysis_summary(ingredients: list[Ingredient]) -> str:
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
   
    return "Not implemented"
  


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
