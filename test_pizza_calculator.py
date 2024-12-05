import pytest
from unittest.mock import patch
from pizza_calculator import calculate_pizzas, serving_size, calculate_cost, main
import io

def test_calculate_pizzas():
    assert calculate_pizzas(9) == (1, 0, 2)
    assert calculate_pizzas(12) == (1, 1, 2)
    assert calculate_pizzas(25) == (3, 1, 1)
    assert calculate_pizzas(0) == (0, 0, 0)  # Test for zero guests

def test_serving_size():
    assert pytest.approx(serving_size(1, 2, 0), 0.01) == 716.28
    assert pytest.approx(serving_size(1, 0, 2), 0.01) == 540.36
    assert pytest.approx(serving_size(3, 1, 0), 0.01) == 1143.54
    assert serving_size(0, 0, 0) == 0  # Test for zero pizzas

def test_calculate_cost():
    assert pytest.approx(calculate_cost(1, 0, 2, 15), 0.01) == 33.63
    assert pytest.approx(calculate_cost(1, 1, 0, 10), 0.01) == 28.14
    assert pytest.approx(calculate_cost(3, 1, 0, 20), 0.01) == 88.85
    assert calculate_cost(0, 0, 0, 0) == 0  # Test for zero pizzas and zero tip

def test_main(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO('9\n15'))
    main()
    captured_output = capsys.readouterr().out
    expected_output = """1 large pizzas, 0 medium pizzas, and 2 small pizzas will be needed.
A total of 540.36 square inches of pizza will be ordered (50.24 per guest).
The total cost of the event will be: $33.63"""
    assert captured_output == expected_output
