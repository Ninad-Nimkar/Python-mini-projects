import time

duration = int(input("Enter the Duration in seconds:"))

print("countdown has started...")

for x in range(duration, 0, -1):
    seconds = int(x % 60)
    minutes  = int(x / 60) % 60
    hours = int(x / 3600)
    days = int(x / 86400)
    time.sleep(1)
    print(f"{days}:{hours:02}:{minutes:02}:{seconds:02}")

print("times up")