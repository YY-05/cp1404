def main():
    choice = input("Convert from (A) Celsius to Fahrenheit or (B) Fahrenheit to Celsius? ")

    if choice == 'A':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit}°F")
    elif choice == 'B':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius}°C")
    else:
        print("Invalid choice.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()
