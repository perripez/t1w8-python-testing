import pytest
from src.calculator import add, subtract, multiply, divide

data = [(1,2,3), (5,6,11), (1,1,2)]

@pytest.mark.parametrize("a, b, expected", data)
def test_add(a,b,expected):
    assert add(a,b) == expected