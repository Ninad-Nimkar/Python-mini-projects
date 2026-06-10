items = []
prices = []
total = 0

while True:
    item = input("Enter the item you want to add to your cart / press q to quit: ")
    if item == "q" or item == "Q":
        break
    else:
        items.append(item)
        price = int(input("Enter the price of the item: "))
        prices.append(price)

print("------YOUR CART------")
for item in items:
    print(item)

for price in prices:
    total += price

print(f"Total: Rs.{total}")









