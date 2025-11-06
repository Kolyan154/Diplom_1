import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BunData, IngredientData


@pytest.fixture
def mock_bun():
    """Фикстура для мока булочки"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = BunData.MOCK_BUN_NAME
    bun.get_price.return_value = BunData.MOCK_BUN_PRICE
    return bun


@pytest.fixture
def mock_sauce_ingredient():
    """Фикстура для мока соуса"""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = IngredientData.MOCK_SAUCE_NAME
    ingredient.get_price.return_value = IngredientData.MOCK_SAUCE_PRICE
    ingredient.get_type.return_value = IngredientData.MOCK_SAUCE_TYPE
    return ingredient


@pytest.fixture
def mock_filling_ingredient():
    """Фикстура для мока начинки"""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = IngredientData.MOCK_FILLING_NAME
    ingredient.get_price.return_value = IngredientData.MOCK_FILLING_PRICE
    ingredient.get_type.return_value = IngredientData.MOCK_FILLING_TYPE
    return ingredient


@pytest.fixture
def burger_with_ingredients(mock_bun, mock_sauce_ingredient, mock_filling_ingredient):
    """Фикстура для бургера с ингредиентами"""
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce_ingredient)
    burger.add_ingredient(mock_filling_ingredient)
    return burger