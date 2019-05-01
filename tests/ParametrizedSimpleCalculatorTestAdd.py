import pytest
from src.Calculators.SimpleCalculator import SimpleCalculator


@pytest.mark.parametrize('first, second, expected', [
    (5, 3, 8),
    (4, 2, 6),
    (9999, 1, 10000)
    ]
)
def test_calc_add(first, second, expected):
    assert SimpleCalculator().calc_add(first, second) == expected


@pytest.mark.parametrize('first, second, expected', [
    (5, 3, 2),
    (4, 6, -2),
    (9999, 1, 9998)
    ]
)
def test_calc_subtract(first, second, expected):
    assert SimpleCalculator().calc_subtract(first, second) == expected


@pytest.mark.parametrize('first, second, expected', [
    (5, 3, 15),
    (4, 6, 24),
    (9999, 1, 9999)
    ]
)
def test_calc_multiply(first, second, expected):
    assert SimpleCalculator().calc_multiply(first, second) == expected


@pytest.mark.parametrize('first, second, expected', [
    (15, 3, 6),
    (24, 6, 4),
    (9999, 1, 9999)
    ]
)
def test_calc_multiply(first, second, expected):
    assert SimpleCalculator().calc_divide(first, second) == expected
