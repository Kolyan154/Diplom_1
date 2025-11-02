from typing import List, Tuple, Dict, Any
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class IngredientData:
    """Тестовые данные для ингредиентов"""
    
    # Параметризованные данные для тестов ингредиентов
    INGREDIENT_PARAMETRIZE_DATA: List[Tuple[str, str, float]] = [
        (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "Sour Cream", 200),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "Dinosaur", 200),
    ]
    
    # Данные для моков соуса
    MOCK_SAUCE_NAME = "Hot Sauce"
    MOCK_SAUCE_PRICE = 50.0  
    MOCK_SAUCE_TYPE = INGREDIENT_TYPE_SAUCE
    
    # Данные для моков начинки
    MOCK_FILLING_NAME = "Cutlet"
    MOCK_FILLING_PRICE = 80.0  
    MOCK_FILLING_TYPE = INGREDIENT_TYPE_FILLING
    
    # Данные из базы данных
    DB_INGREDIENTS_DATA = [
        {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100.0},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200.0},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "chili sauce", "price": 300.0},
        {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100.0},
        {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200.0},
        {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300.0},
    ]