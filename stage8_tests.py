import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from stages.stage1_parsing import parse_ingredients
from stages.stage2_ingredient import Ingredient, create_unknown_ingredient
from stages.stage3_database import IngredientDatabase
from stages.stage5_scoring import calculate_overall_score, get_score_label, count_by_category


class TestStage1Parsing:
   

    def test_basic_parsing(self):
        result = parse_ingredients("Water, Sugar, Salt")
        assert result == ["water", "sugar", "salt"]
        

    def test_whitespace_handling(self):
       
        result = parse_ingredients("  Flour  ,  SUGAR,salt  ")
        assert result == ["flour", "sugar", "salt"]
        

    def test_empty_string(self):
        
        result = parse_ingredients("")
        assert result == []
        

    def test_parenthetical_removal(self):

       

        result = parse_ingredients("Red 40 (for color), Sugar")
        assert result == ["red 40", "sugar"]
        

    def test_single_ingredient(self):
        
        result = parse_ingredients("Water")
        assert result == ["water"]
        


class TestStage2Ingredient:
    

    def test_ingredient_creation_minimal(self):
        
        ing = Ingredient(name="sugar")
        assert ing.category == "unknown"
        assert ing.health_score == 5
        assert ing.found_in_database == False


    def test_ingredient_creation_full(self):
        
        ing = Ingredient(
            name="water",
            category="healthy",
            health_score=10,
            description="Essential for hydration",
            found_in_database=True
        )
        assert ing.name == "water"
        assert ing.category == "healthy"
        assert ing.health_score == 10
        assert ing.description == "Essential for hydration"
        assert ing.found_in_database == True


    def test_create_unknown_ingredient(self):
       
        ing = create_unknown_ingredient("mystery")
        assert ing.name == "mystery"
        assert ing.category == "unknown"
        assert ing.found_in_database == False


class TestStage3Database:
    @pytest.fixture
    def database(self):
        
        db_path = Path(__file__).parent.parent / "data" / "ingredients_db.json"
        return IngredientDatabase(str(db_path))

    def test_database_loads(self, database):

        assert len(database) > 0
        

    def test_lookup_existing_ingredient(self, database):
        result = database.lookup("sugar")
        assert result is not None
        assert "category" in result
        assert "health_score" in result
       

    def test_lookup_case_insensitive(self, database):
        assert database.lookup("SUGAR") == database.lookup("sugar")
        

    def test_lookup_nonexistent(self, database):
       
        assert database.lookup("unicorn tears") is None

        

    def test_contains_operator(self, database):
       
        assert "water" in database
        assert "unicorn tears" not in database
       
      


class TestStage5Scoring:
   

    @pytest.fixture
    def sample_ingredients(self):
       
        return [
            Ingredient(name="water", category="healthy", health_score=10,
                      description="Good", found_in_database=True),
            Ingredient(name="sugar", category="harmful", health_score=2,
                      description="Bad", found_in_database=True),
        ]

    def test_calculate_score_empty_list(self):
       
        assert calculate_overall_score([]) == 5.0
       

    def test_calculate_score_basic(self, sample_ingredients):
       
        assert calculate_overall_score(sample_ingredients) == 6.0

        

    def test_score_label_excellent(self):
        
        assert get_score_label(8.0) == "Excellent"
        assert get_score_label(9.0) == "Excellent"
        assert get_score_label(10.0) == "Excellent"
       

    def test_score_label_poor(self):
        
        assert get_score_label(0.0) == "Poor"
        assert get_score_label(2.0) == "Poor"
        assert get_score_label(3.9) == "Poor"
        

    def test_count_by_category(self, sample_ingredients):
      
        counts = count_by_category(sample_ingredients)
        assert counts == {"healthy": 1, "harmful": 1}
        


def is_implemented() -> bool:
   
    import inspect
    source = inspect.getsource(TestStage1Parsing.test_basic_parsing)
    return "assert" in source and "pass" not in source.split("assert")[0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
