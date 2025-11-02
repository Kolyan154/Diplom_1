import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.data.bun_data import BunData
from tests.data.ingredient_data import IngredientData


class TestDatabase:
    
    def test_database_initialization(self):
        """Тест инициализации базы данных"""
        db = Database()
        assert len(db.buns) == len(BunData.DB_BUNS_DATA)
        assert len(db.ingredients) == len(IngredientData.DB_INGREDIENTS_DATA)
    
    def test_available_buns(self):
        """Тест получения доступных булочек"""
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == len(BunData.DB_BUNS_DATA)
        assert all(isinstance(bun, Bun) for bun in buns)
        
        # Проверяем данные булочек
        for i, expected_bun_data in enumerate(BunData.DB_BUNS_DATA):
            assert buns[i].get_name() == expected_bun_data["name"]
            assert buns[i].get_price() == expected_bun_data["price"]
    
    def test_available_ingredients(self):
        """Тест получения доступных ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == len(IngredientData.DB_INGREDIENTS_DATA)
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        # Проверяем данные ингредиентов
        for i, expected_ingredient_data in enumerate(IngredientData.DB_INGREDIENTS_DATA):
            assert ingredients[i].get_type() == expected_ingredient_data["type"]
            assert ingredients[i].get_name() == expected_ingredient_data["name"]
            assert ingredients[i].get_price() == expected_ingredient_data["price"]
    
    def test_available_buns_returns_same_list(self):
        """Тест, что available_buns возвращает тот же список (не копию)"""
        db = Database()
        buns1 = db.available_buns()
        buns2 = db.available_buns()
        
        assert buns1 is buns2
    
    def test_available_ingredients_returns_same_list(self):
        """Тест, что available_ingredients возвращает тот же список (не копию)"""
        db = Database()
        ingredients1 = db.available_ingredients()
        ingredients2 = db.available_ingredients()
        
        assert ingredients1 is ingredients2