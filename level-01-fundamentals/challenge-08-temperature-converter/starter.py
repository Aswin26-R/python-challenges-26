def celsius_to_fahrenheit(celsius):
    return((celsius * 9/5) + 32)
    pass
print(celsius_to_fahrenheit(-40))


def fahrenheit_to_celsius(fahrenheit):
    return((fahrenheit - 32)* 5/9)
    pass
print(fahrenheit_to_celsius(98.6))


def celsius_to_kelvin(celsius):
    return(celsius + 273.15)
    pass
print(celsius_to_kelvin(100))


def kelvin_to_celsius(kelvin):
    return(kelvin - 273.15)
    pass
print(kelvin_to_celsius(0))