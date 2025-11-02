from typing import List, Tuple


class BunData:
    """Тестовые данные для булочек"""
    
    # Параметризованные данные для тестов булочек
    BUN_PARAMETRIZE_DATA: List[Tuple[str, float]] = [
        ("Black Bun", 100),
        ("White Bun", 200),
        ("Red Bun", 300),
    ]
    
    # Данные для моков булочек
    MOCK_BUN_NAME = "Test Bun"
    MOCK_BUN_PRICE = 100.0  # как float
    
    # Данные из базы данных
    DB_BUNS_DATA = [
        {"name": "black bun", "price": 100.0},
        {"name": "white bun", "price": 200.0},
        {"name": "red bun", "price": 300.0},
    ]