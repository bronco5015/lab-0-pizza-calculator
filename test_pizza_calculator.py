from pizza_calculator import calculate_pizzas, serving_size, calculate_cost, main
from unittest.mock import patch
import pytest

def test_calculate_pizzas():
    """
    Test the calculate_pizzas function with 9, 12, and 25 guests.
    """
    assert calculate_pizzas(9) == (1, 0, 2)
    assert calculate_pizzas(12) == (1, 1, 2)
    assert calculate_pizzas(25) == (3, 1, 1)

def test_serving_size():
    """
    Test the serving_size function with various combinations of pizzas.
    """
    assert pytest.approx(serving_size(1, 2, 0), 0.01) == 716.28  # 1 Large + 2 Medium
    assert pytest.approx(serving_size(1, 0, 2), 0.01) == 540.36  # 1 Large + 2 Small
    assert pytest.approx(serving_size(3, 1, 0), 0.01) == 1143.54  # 3 Large + 1 Medium

def test_calculate_cost():
    """
    Test the calculate_cost function with various pizza counts and tip percentages.
    """
    assert pytest.approx(calculate_cost(1, 0, 2, 15), 0.01) == 33.63  # 1 Large, 2 Small, 15% tip
    assert pytest.approx(calculate_cost(1, 1, 0, 10), 0.01) == 28.14  # 1 Large, 1 Medium, 10% tip
    assert pytest.approx(calculate_cost(3, 1, 0, 20), 0.01) == 88.85  # 3 Large, 1 Medium, 20% tip

def test_main_function():
    with patch('builtins.input', side_effect=['9']):
        result = main.main()
        assert result == "Hello John! You are 25 years old."
