choice = str(input('''1.Type C to convert Celsius to Fahrenheit 
2.Type F to convert Fahrenheit to Celsius: '''))

temp = float(input("Enter the Temprature: "))

if choice == "C" or choice == "c":
    result = (temp * 9/5) + 32

elif choice == "F" or choice == "f":
        result = (temp - 32) * 5/9

else:
    print("invalid input")

print(f"The converted temprature is {round(result, 1)}{choice}")