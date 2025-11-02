import pytest
from praktikum.bun import Bun
from tests.data.bun_data import BunData


class TestBun:
    
    def test_bun_initialization(self):
        """Тест инициализации булочки"""
        bun = Bun(BunData.MOCK_BUN_NAME, BunData.MOCK_BUN_PRICE)
        assert bun.name == BunData.MOCK_BUN_NAME
        assert bun.price == BunData.MOCK_BUN_PRICE
    
    def test_get_name(self):
        """Тест получения названия булочки"""
        bun = Bun(BunData.MOCK_BUN_NAME, BunData.MOCK_BUN_PRICE)
        assert bun.get_name() == BunData.MOCK_BUN_NAME
    
    def test_get_price(self):
        """Тест получения цены булочки"""
        bun = Bun(BunData.MOCK_BUN_NAME, BunData.MOCK_BUN_PRICE)
        assert bun.get_price() == BunData.MOCK_BUN_PRICE
    
    @pytest.mark.parametrize("name,price", BunData.BUN_PARAMETRIZE_DATA)
    def test_bun_parameterized(self, name, price):
        """Параметризованный тест создания булочек с разными данными"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price