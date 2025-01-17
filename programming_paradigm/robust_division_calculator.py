#!/usr/bin/env python3
def safe_divide(numerator, denominator):
    """Perform division with error handling for zero division and non-numeric inputs."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."

        # Perform the division
        return f"The result of the division is {num / denom}"
    
    except ValueError:
        return "Error: Please enter numeric values only."

