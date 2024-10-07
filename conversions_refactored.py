from conversions import convertFahrenheitToCelsius, convertKelvinToCelsius, convertCelsiusToFahrenheit


class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    """General conversion function for temperature and distance"""

    # Temperature conversions
    if fromUnit == 'Celsius' and toUnit == 'Kelvin':
        return value + 273.15
    elif fromUnit == 'Celsius' and toUnit == 'Fahrenheit':
        return (value * 9 / 5) + 32
    elif fromUnit == 'Fahrenheit' and toUnit == 'Celsius':
        return (value - 32) * 5 / 9
    elif fromUnit == 'Fahrenheit' and toUnit == 'Kelvin':
        return convert('Celsius', 'Kelvin', convertFahrenheitToCelsius(value))
    elif fromUnit == 'Kelvin' and toUnit == 'Celsius':
        return value - 273.15
    elif fromUnit == 'Kelvin' and toUnit == 'Fahrenheit':
        celsius = convertKelvinToCelsius(value)
        return convertCelsiusToFahrenheit(celsius)

    # Distance conversions
    elif fromUnit == 'Miles' and toUnit == 'Yards':
        return value * 1760
    elif fromUnit == 'Miles' and toUnit == 'Meters':
        return value * 1609.34
    elif fromUnit == 'Yards' and toUnit == 'Miles':
        return value / 1760
    elif fromUnit == 'Meters' and toUnit == 'Miles':
        return value / 1609.34

    # Same unit conversion
    elif fromUnit == toUnit:
        return value

    # Raise exception if conversion is not possible
    else:
        raise ConversionNotPossible(f"Conversion not possible between {fromUnit} and {toUnit}")
