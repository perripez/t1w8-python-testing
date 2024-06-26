import pytest
from src.calculator import add, subtract, multiply, divide

@pytest.fixtures()
def sample_data():
    return {
        "a": 5,
        "b": 3,
        "expected_sum": 8,
        "expected_difference": 2,
        "expected_product": 15,
        "expected_division": 5 / 3
    }
def test_add(sample_data):
    assert  add(sample_data["a"], sample_data["b"]) == sample_data["expected_sum"]