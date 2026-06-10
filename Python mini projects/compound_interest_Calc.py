principle = 0
rate = 0
time = 0

while principle <= 0 or rate <= 0 or time <= 0:
    principle = float(input("Enter the principle amount: "))
    rate = float(input("Enter the rate of interest:"))
    time = int(input("Enter the time in years: "))

    if principle <= 0 or rate <= 0 or time <= 0:
        print("Please enter positive values only")

result = principle * (1 + rate/100) ** time
print(round(result, 2))