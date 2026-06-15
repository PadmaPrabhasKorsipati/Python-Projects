
unit=input("Is this temperature in cesius or fahrenheit (c/f):")

temp=float(input("Enter the Temperature:"))


if unit=='C':
    temp =round(9*temp /5 +32,2)
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit=='F':
    temp=round((temp-32)*5/9,2)
    print(f"The temperature in Celsius is: {temp}°C ")

else:
    print(f"{unit} is an invalid unnit of the measurement.")




