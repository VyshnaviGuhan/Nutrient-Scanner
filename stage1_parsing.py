def parse_ingredients(raw_text: str) -> list[str]:
    
    if not raw_text.strip ():
        return[]
        
    items = raw_text.split(',')
    result = []

    for item in items:
        if '(' in item:
            item =  item.split ('(')[0]
    
        item = item.strip().lower()
        
        if item:
            result.append(item)
        
    return result
            
        
   
    



def is_implemented() -> bool:
   
    result = parse_ingredients("Water, Sugar, Salt")
    return result != ["__NOT_IMPLEMENTED__"] and len(result) == 3
    


if __name__ == "__main__":
    test_cases = [
        ("Water, Sugar, Salt", ["water", "sugar", "salt"]),
        ("  Flour  ,  SUGAR,salt  ", ["flour", "sugar", "salt"]),
        ("Red 40 (for color), Sugar", ["red 40", "sugar"]),
        ("", []),
        ("Single", ["single"]),
    ]

    print("Testing parse_ingredients()...")
    for input_text, expected in test_cases:
        result = parse_ingredients(input_text)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {repr(input_text)}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()
