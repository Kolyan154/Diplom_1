import pytest
from praktikum.ingredient import Ingredient
from data import IngredientData


class TestIngredient:
    
    def test_ingredient_initialization(self):
        """Тест инициализации ингредиента"""
        ingredient = Ingredient(
            IngredientData.MOCK_SAUCE_TYPE,
            IngredientData.MOCK_SAUCE_NAME,
            IngredientData.MOCK_SAUCE_PRICE
        )
        assert ingredient.type == IngredientData.MOCK_SAUCE_TYPE
        assert ingredient.name == IngredientData.MOCK_SAUCE_NAME
        assert ingredient.price == IngredientData.MOCK_SAUCE_PRICE
    
    def test_get_price(self):
        """Тест получения цены ингредиента"""
        ingredient = Ingredient(
            IngredientData.MOCK_SAUCE_TYPE,
            IngredientData.MOCK_SAUCE_NAME,
            IngredientData.MOCK_SAUCE_PRICE
        )
        assert ingredient.get_price() == IngredientData.MOCK_SAUCE_PRICE
    
    def test_get_name(self):
        """Тест получения названия ингредиента"""
        ingredient = Ingredient(
            IngredientData.MOCK_SAUCE_TYPE,
            IngredientData.MOCK_SAUCE_NAME, 
            IngredientData.MOCK_SAUCE_PRICE
        )
        assert ingredient.get_name() == IngredientData.MOCK_SAUCE_NAME
    
    def test_get_type(self):
        """Тест получения типа ингредиента"""
        ingredient = Ingredient(
            IngredientData.MOCK_SAUCE_TYPE,
            IngredientData.MOCK_SAUCE_NAME,
            IngredientData.MOCK_SAUCE_PRICE
        )
        assert ingredient.get_type() == IngredientData.MOCK_SAUCE_TYPE
    
    @pytest.mark.parametrize("ingredient_type,name,price", IngredientData.INGREDIENT_PARAMETRIZE_DATA)
    def test_ingredient_parameterized(self, ingredient_type, name, price):
        """Параметризованный тест создания ингредиентов с разными данными"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price