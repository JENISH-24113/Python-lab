temperatures_fahrenheit = [12,34,56,78]

temperatures_celsius = [(temp - 32) * 5 / 9 for temp in temperatures_fahrenheit]

print("Temperatures in Fahrenheit:", temperatures_fahrenheit)
print("Equivalent temperatures in Celsius:", temperatures_celsius)