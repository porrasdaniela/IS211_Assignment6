from anaconda_project.internal.conda_api import result

import conversions_refactored
from conversions_refactored import ConversionNotPossible

def test_general_conversion():
    result = conversions_refactored.convert('Kelvin', 'Fahrenheit', 255.37)
    print(f"Converted 255.37 K to Fahrenheit: {result}")
    expected_result = -0.004
    assert abs(result - expected_result) < 1e-4, "Kelvin to Fahrenheit conversion failed"

    print("Testing temperature conversions...")
    # Test valid temperature conversions
    assert conversions_refactored.convert('Celsius', 'Kelvin', 0) == 273.15, "Celsius to Kelvin conversion failed"
    assert conversions_refactored.convert('Celsius', 'Fahrenheit', 100) == 212.0, "Celsius to Fahrenheit conversion failed"
    assert conversions_refactored.convert('Fahrenheit', 'Celsius', 32) == 0.0, "Fahrenheit to Celsius conversion failed"
    assert conversions_refactored.convert('Kelvin', 'Celsius', 273.15) == 0.0, "Kelvin to Celsius conversion failed"
    expected_result = -0.004
    assert abs(result - expected_result) < 1e-4, "Kelvin to Fahrenheit conversion failed"

    print("Testing distance conversions...")
    # Test valid distance conversions
    assert conversions_refactored.convert('Miles', 'Yards', 1) == 1760, "Miles to Yards conversion failed"
    assert conversions_refactored.convert('Miles', 'Meters', 1) == 1609.34, "Miles to Meters conversion failed"
    assert conversions_refactored.convert('Yards', 'Miles', 1760) == 1, "Yards to Miles conversion failed"
    assert conversions_refactored.convert('Meters', 'Miles', 1609.34) == 1, "Meters to Miles conversion failed"

    print("Testing same unit conversions...")
    # Test converting same unit to itself
    assert conversions_refactored.convert('Celsius', 'Celsius', 25) == 25, "Same unit conversion for Celsius failed"
    assert conversions_refactored.convert('Meters', 'Meters', 100) == 100, "Same unit conversion for Meters failed"

    print("Testing invalid conversions...")
    # Test invalid conversions that should raise ConversionNotPossible
    try:
        conversions_refactored.convert('Celsius', 'Meters', 100)
    except ConversionNotPossible:
        print("Correctly raised ConversionNotPossible for Celsius to Meters conversion")
    else:
        print("Failed to raise ConversionNotPossible for Celsius to Meters conversion")

    try:
        conversions_refactored.convert('Miles', 'Kelvin', 5)
    except ConversionNotPossible:
        print("Correctly raised ConversionNotPossible for Miles to Kelvin conversion")
    else:
        print("Failed to raise ConversionNotPossible for Miles to Kelvin conversion")

    print("All tests passed!")

# runs the tests
if __name__ == "__main__":
    test_general_conversion()