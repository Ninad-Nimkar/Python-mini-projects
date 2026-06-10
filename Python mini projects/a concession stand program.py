menu = {"biryani": 500,
        "chapati": 50,
        "jeera rice": 150,
        "chicken handi": 400,
        "chicken kadai": 400}

cart = []
total = 0

print("-------MENU--------")
for key, value in menu.items():
    print(f"{key:15}: Rs.{value}")
print("-------------------")

while True:
    food = input("enter the items (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------Your Order----------")
for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f"Your total is Rs.{total}: ")
