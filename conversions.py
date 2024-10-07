from sympy.physics.units import kelvin


def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = celsius * 9/5 +32
    return fahrenheit

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    return convertCelsiusToKelvin(convertFahrenheitToCelsius(fahrenheit))

def convertKelvinToCelsius(Kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    return Kelvin - 273.15

def convertKelvinToFahrenheit(Kelvin):
    """Takes in a float representing Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (Kelvin - 273.15) * (9 / 5) + 32
    return fahrenheit
