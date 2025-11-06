import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import BunData, IngredientData, BurgerData, get_expected_receipt, get_expected_receipt_no_ingredients, get_expected_receipt_single_ingredient


class TestBurger:

    def test_burger_initialization(self):
        """Тест инициализации пустого бургера"""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, mock_bun):  
        """Тест установки булочки"""
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_bun, mock_sauce_ingredient):  
        """Тест добавления ингредиента"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce_ingredient)
        
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce_ingredient

    def test_remove_ingredient(self, burger_with_ingredients):  
        """Тест удаления ингредиента"""
        initial_count = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(0)
        
        assert len(burger_with_ingredients.ingredients) == initial_count - 1

    def test_remove_ingredient_invalid_index(self, burger_with_ingredients):  
        """Тест удаления ингредиента с неверным индексом"""
        with pytest.raises(IndexError):
            burger_with_ingredients.remove_ingredient(10)

    def test_move_ingredient(self, burger_with_ingredients, mock_sauce_ingredient, mock_filling_ingredient):  
        """Тест перемещения ингредиента"""
        # Изначально: [sauce, filling]
        assert burger_with_ingredients.ingredients[0] == mock_sauce_ingredient
        assert burger_with_ingredients.ingredients[1] == mock_filling_ingredient
        
        burger_with_ingredients.move_ingredient(0, 1)
        
        # После перемещения: [filling, sauce]
        assert burger_with_ingredients.ingredients[0] == mock_filling_ingredient
        assert burger_with_ingredients.ingredients[1] == mock_sauce_ingredient

    def test_move_ingredient_invalid_index(self, burger_with_ingredients): 
        """Тест перемещения ингредиента с неверным индексом"""
        with pytest.raises(IndexError):
            burger_with_ingredients.move_ingredient(10, 0)

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected_total", 
                             BurgerData.PRICE_PARAMETRIZE_DATA)
    def test_get_price_with_parameterization(self, mock_bun, bun_price, ingredient_prices, expected_total):
        """Параметризованный тест расчета цены с разными комбинациями"""
        burger = Burger()
        
        # Настраиваем мок булочки с нужной ценой
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        
        # Создаем и добавляем моки ингредиентов с разными ценами
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)
        
        assert burger.get_price() == expected_total

    def test_get_price_no_bun_raises_error(self):
        """Тест расчета цены без установленной булочки"""
        burger = Burger()
        
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_get_receipt(self, mock_bun, mock_sauce_ingredient, mock_filling_ingredient): 
        """Тест генерации чека"""
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce_ingredient)
        burger.add_ingredient(mock_filling_ingredient)
        
        receipt = burger.get_receipt()
        
        # Формируем ожидаемый чек
        expected_receipt = get_expected_receipt(
            bun_name=BunData.MOCK_BUN_NAME,
            ingredients=[
                {"type": "sauce", "name": IngredientData.MOCK_SAUCE_NAME},
                {"type": "filling", "name": IngredientData.MOCK_FILLING_NAME}
            ],
            total_price=330.0  # 2*100 + 50 + 80 как float
        )
        
        assert receipt == expected_receipt

    def test_get_receipt_no_ingredients(self, mock_bun):  
        """Тест генерации чека без ингредиентов"""
        burger = Burger()
        burger.set_buns(mock_bun)
        
        receipt = burger.get_receipt()
        
        # Формируем ожидаемый чек
        expected_receipt = get_expected_receipt_no_ingredients(
            bun_name=BunData.MOCK_BUN_NAME,
            total_price=200.0  # 2*100 как float
        )
        
        assert receipt == expected_receipt

    @pytest.mark.parametrize("ingredient_type,type_string", 
                             BurgerData.RECEIPT_INGREDIENT_TYPES_DATA)
    def test_get_receipt_ingredient_types_parameterized(self, mock_bun, ingredient_type, type_string):
        """Параметризованный тест типов ингредиентов в чеке"""
        # Создаем мок с возвращаемыми значениями
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "Test Ingredient"
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_price.return_value = 0 
        
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()
        
        # Формируем ожидаемый чек
        expected_receipt = get_expected_receipt_single_ingredient(
            bun_name=BunData.MOCK_BUN_NAME,
            ingredient_type=type_string,
            ingredient_name="Test Ingredient",
            total_price=200.0  # 2*100 как float
        )
        
        assert receipt == expected_receipt

    def test_get_receipt_no_bun_raises_error(self):
        """Тест генерации чека без установленной булочки"""
        burger = Burger()
        
        with pytest.raises(AttributeError):
            burger.get_receipt()