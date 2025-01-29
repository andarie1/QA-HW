import pytest


class SimpleMath:
    """Класс с простыми математическими операциями."""
    def square(self, x):
        """Возвращает квадрат числа."""
        return x * x


    def cube(self, x):
        """Возвращает куб числа."""
        return x * x * x


@pytest.fixture
def simple_math():
    """Фикстура для создания объекта SimpleMath."""
    return SimpleMath()

#SQUARE
def test_square_positive_number(simple_math):
    actual_result = simple_math.square(3)
    expected_result = 9
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

def test_square_negative_number(simple_math):
    actual_result = simple_math.square(-4)
    expected_result = 16
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

def test_square_zero(simple_math):
    actual_result = simple_math.square(0)
    expected_result = 0
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

#CUBE
def test_cube_positive_number(simple_math):
    actual_result = simple_math.cube(2)
    expected_result = 8
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

def test_cube_negative_number(simple_math):
    actual_result = simple_math.cube(-3)
    expected_result = -27
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"

def test_cube_zero(simple_math):
    actual_result = simple_math.cube(0)
    expected_result = 0
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"
