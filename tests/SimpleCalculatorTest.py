import pytest


from src.Calculators.SimpleCalculator import SimpleCalculator


def test_add():
    """test addition function"""
    assert SimpleCalculator.calc_add(9, 1) == 10


def test_subtract():
    """test subtraction function"""
    assert SimpleCalculator.calc_subtract(9, 1) == 8


def test_multiply():
    """test multiplication function"""
    assert SimpleCalculator.calc_multiply(9, 3) == 27


def test_divide():
    """test division function"""
    assert SimpleCalculator.calc_divide(9, 3) == 3


def test_divide_exception():
    """test that exception is division by zero"""
    with pytest.raises(Exception):
        assert SimpleCalculator.calc_divide(9, 0)



