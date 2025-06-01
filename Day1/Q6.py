""" 6- Temperature Converter : Ask the user to enter temperature in Celsius

Convert it to Fahrenheit using the formula:
Fahrenheit = (Celsius × 9/5) + 32

Print the result in a user-friendly format, like:
"37°C is equal to 98.6°F" """

temp_celsius = int(input("enter temperature in celcius"))

Fahrenheit = (temp_celsius * 9/5) + 32

print(temp_celsius,"C is equal to ",Fahrenheit,"F")
