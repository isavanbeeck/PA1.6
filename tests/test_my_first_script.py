import sys
import os

from my_first_script import nerdy_computation

def test_nerdy_computation_basic():
    """Test that nerdy_computation returns correct sum of squares."""
    # For x=1: 1^2 = 1
    assert nerdy_computation(1) == 1, "Sum of squares through 1 should be 1."
    
    # For x=2: 1^2 + 2^2 = 1 + 4 = 5
    assert nerdy_computation(2) == 5, "Sum of squares through 2 should be 5."
    
    # For x=3: 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
    assert nerdy_computation(3) == 14, "Sum of squares through 3 should be 14."

def test_nerdy_computation_ten():
    """Test the specific case mentioned in the script (x=10)."""
    # Sum of squares from 1 to 10: 1^2 + 2^2 + ... + 10^2 = 385
    expected = 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2 + 7**2 + 8**2 + 9**2 + 10**2
    assert nerdy_computation(10) == expected, "Sum of squares through 10 should match the calculated total."
    assert nerdy_computation(10) == 385, "Sum of squares through 10 should be 385."

def test_nerdy_computation_zero():
    """Test edge case with x=0."""
    assert nerdy_computation(0) == 0, "Sum of squares through 0 should be 0."

def test_nerdy_computation_formula():
    """Test against the mathematical formula: n(n+1)(2n+1)/6"""
    for n in [1, 5, 10, 15]:
        expected = n * (n + 1) * (2 * n + 1) // 6
        assert nerdy_computation(n) == expected, f"Sum of squares through {n} should match the formula."