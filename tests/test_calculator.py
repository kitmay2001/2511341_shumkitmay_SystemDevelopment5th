"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

MAX_VALUE = Calculator.MAX_VALUE
MIN_VALUE = Calculator.MIN_VALUE

def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8
        sut = Calculator()

        # Act
        result = sut.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_at_max_boundary(self):
        """Test addition at maximum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(MAX_VALUE + 1, 0)

    def test_add_at_min_boundary(self):
        """Test addition at exact minimum boundary."""
        calc = Calculator()
        result = calc.add(MIN_VALUE, 0)
        assert result == MIN_VALUE

    def test_add_below_min_boundary(self):
        """Test addition below minimum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(MIN_VALUE - 1, 0)

    def test_add_at_max_boundary_valid(self):
        """Test addition at exact maximum boundary."""
        calc = Calculator()
        result = calc.add(MAX_VALUE, 0)
        assert result == MAX_VALUE

    def test_add_exact_max_plus_zero(self):
        """Distinguish > from >= mutation."""
        calc = Calculator()
        result = calc.add(MAX_VALUE, 0)
        assert result == MAX_VALUE
        assert result != MAX_VALUE - 1

    def test_add_exact_min_plus_zero(self):
        """Distinguish < from <= mutation."""
        calc = Calculator()
        result = calc.add(MIN_VALUE, 0)
        assert result == MIN_VALUE
        assert result != MIN_VALUE + 1


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 2
        b = 5
        expected = -3

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -2
        b = -5
        expected = 3

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_and_negative(self):
        """Test subtracting positive and negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 2
        b = -5
        expected = 7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_and_positive(self):
        """Test subtracting negative and positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -2
        b = 5
        expected = -7

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_numbers_with_zero(self):
        """Test subtracting positive numbers with zero."""
        # TODO: Implement
        calc = Calculator()
        a = 2
        b = 0
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_numbers_with_zero(self):
        """Test subtracting negative numbers with zero."""
        # TODO: Implement
        calc = Calculator()
        a = -5
        b = 0
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_at_min_boundary(self):
        """Test subtraction at exact minimum boundary."""
        calc = Calculator()
        result = calc.subtract(MIN_VALUE, 0)
        assert result == MIN_VALUE

    def test_subtract_below_min_boundary(self):
        """Test subtraction below minimum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(MIN_VALUE - 1, 0)

    def test_subtract_at_max_boundary_valid(self):
        """Test subtraction at exact maximum boundary."""
        calc = Calculator()
        result = calc.subtract(MAX_VALUE, 0)
        assert result == MAX_VALUE

    def test_subtract_above_max_boundary(self):
        """Test subtraction above maximum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(MAX_VALUE + 1, 0)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 2
        b = 4
        expected = 8

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -2
        b = -5
        expected = 10

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_and_negative_numbers(self):
        """Test multiplying positive and negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 2
        b = -7
        expected = -14

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_and_positive_numbers(self):
        """Test multiplying negative and positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -2
        b = 5
        expected = -10

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_positive_number_with_zero(self):
        """Test multiplying positive number with zero."""
        # TODO: Implement
        calc = Calculator()
        a = 7
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_number_with_zero(self):
        """Test multiplying negative number with zero."""
        # TODO: Implement
        calc = Calculator()
        a = -6
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_at_min_boundary(self):
        """Test multiplication at exact minimum boundary."""
        calc = Calculator()
        result = calc.multiply(MIN_VALUE, 1)
        assert result == MIN_VALUE

    def test_multiply_below_min_boundary(self):
        """Test multiplication below minimum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(MIN_VALUE - 1, 1)

    def test_multiply_at_max_boundary_valid(self):
        """Test multiplication at exact maximum boundary."""
        calc = Calculator()
        result = calc.multiply(MAX_VALUE, 1)
        assert result == MAX_VALUE

    def test_multiply_above_max_boundary(self):
        """Test multiplication above maximum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(MAX_VALUE + 1, 0)

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 10
        b = 5
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -10
        b = -2
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_and_negative_numbers(self):
        """Test dividing positive and negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 10
        b = -5
        expected = -2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_and_positive_numbers(self):
        """Test dividing positive and negative numbers."""
        # TODO: Implement
        calc = Calculator()
        a = -20
        b = 5
        expected = -4

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_zero(self):
        """Test dividing positive numbers."""
        # TODO: Implement
        calc = Calculator()
        a = 10
        b = 0

        # Act and Assert
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(a, b)

    def test_divide_at_min_boundary(self):
        """Test division at exact minimum boundary."""
        calc = Calculator()
        result = calc.divide(MIN_VALUE, 1)
        assert result == MIN_VALUE

    def test_divide_below_min_boundary(self):
        """Test division below minimum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(MIN_VALUE - 1, 1)

    def test_divide_at_max_boundary_valid(self):
        """Test division at exact maximum boundary."""
        calc = Calculator()
        result = calc.divide(MAX_VALUE, 1)
        assert result == MAX_VALUE

    def test_divide_above_max_boundary(self):
        """Test division above maximum boundary."""
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(MAX_VALUE + 1, 1)

    def test_divide_with_remainder(self):
        """Test division that produces float result."""
        calc = Calculator()
        assert calc.divide(10, 3) == pytest.approx(3.333333, rel=1e-5)



