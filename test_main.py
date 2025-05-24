import pytest
from main import add, subtract, multiply  # Import functions from main.py

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-5, -5) == -10
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    assert subtract(5.5, 2.5) == 3.0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
    assert multiply(7, 1) == 7
    assert multiply(2.5, 2) == 5.0

# To run the tests, use `pytest` in the terminal at the project root.
# Make sure pytest is installed: pip install pytest
