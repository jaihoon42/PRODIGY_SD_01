# TEMPERATURE CONVERSION PROGRAM


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature():
    print("Temperature Conversion Program")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()

    if unit == "C":
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
        print(f"{temp}°C = {f:.2f}°F")
        print(f"{temp}°C = {k:.2f}K")
    elif unit == "F":
        c = fahrenheit_to_celsius(temp)
        k = fahrenheit_to_kelvin(temp)
        print(f"{temp}°F = {c:.2f}°C")
        print(f"{temp}°F = {k:.2f}K")
    elif unit == "K":
        c = kelvin_to_celsius(temp)
        f = kelvin_to_fahrenheit(temp)
        print(f"{temp}K = {c:.2f}°C")
        print(f"{temp}K = {f:.2f}°F")
    else:
        print("Invalid unit! Please enter C, F, or K.")

# Run the program
convert_temperature()