# test_integration.py
from mylib.lib import trapezoidal_rule, calculate_time_memory_trapezoidal
import math


def test_trapezoidal_rule_with_square():
    """Test trapezoidal_rule for f(x) = x^2 over [0, 1]."""
    result = trapezoidal_rule(0.0, 1.0, 100, lambda x: x**2)
    expected_result = 1.0 / 3.0  # Exact result of integral of x^2 over [0, 1]
    assert (
        abs(result - expected_result) < 0.001
    ), f"Test failed: Expected {expected_result}, got {result}"


def test_trapezoidal_rule_with_constant():
    """Test trapezoidal_rule for f(x) = 5.0 over [0, 2]."""
    result = trapezoidal_rule(0.0, 2.0, 100, lambda x: 5.0)
    expected_result = 10.0  # Exact result of integral of f(x) = 5 over [0, 2]
    assert (
        abs(result - expected_result) < 0.001
    ), f"Test failed: Expected {expected_result}, got {result}"


def test_trapezoidal_rule_with_sine():
    """Test trapezoidal_rule for f(x) = sin(x) over [0, π]."""
    result = trapezoidal_rule(0.0, math.pi, 100, math.sin)
    expected_result = 2.0  # Exact result of integral of sin(x) over [0, π]
    assert (
        abs(result - expected_result) < 0.001
    ), f"Test failed: Expected {expected_result}, got {result}"


def test_calculate_time_memory_trapezoidal():
    """Test calculate_time_memory_trapezoidal to ensure it returns expected results."""
    f = lambda x: x**2
    result, memory_usage, elapsed_time = calculate_time_memory_trapezoidal(
        0.0, 1.0, 100, f
    )

    # Simple checks to ensure outputs are non-null and within expected ranges
    assert result is not None, "Test failed: Result is None"
    assert memory_usage >= 0, "Test failed: Memory usage should be non-negative"
    assert elapsed_time >= 0, "Test failed: Elapsed time should be non-negative"
    print("calculate_time_memory_trapezoidal test passed successfully.")


if __name__ == "__main__":
    test_trapezoidal_rule_with_square()
    test_trapezoidal_rule_with_constant()
    test_trapezoidal_rule_with_sine()
    test_calculate_time_memory_trapezoidal()
    print("All tests passed!")
