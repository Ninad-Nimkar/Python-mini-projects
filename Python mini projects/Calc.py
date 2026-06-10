n1 = int( input("enter your first number: "))
n2 = int(input ("enter your second number: "))

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):    
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def Power(n1, n2):
    return n1 ** n2

def div(n1, n2):
    if n2 == 0:
        return ("error: division by zero")
    return n1 / n2
    

print("choose your operation\n")
print("1.Add")
print("2.Sub")
print("3.Multiply")
print("4.Divide")
print("5.Power")

choice = int(input("enter yout choice: "))

if choice == 1:
    print(f"{n1} + {n2} = {add(n1, n2)}")

elif choice == 2:
    print(f"{n1} - {n2} = {sub(n1, n2)}")

elif choice == 3:
    print(f"{n1} * {n2} = {mul(n1, n2)}")

elif choice == 4:
    print(f"{n1} / {n2} = {div(n1, n2)}")

elif choice == 5:
    print(f"{n1} ** {n2} = {Power(n1, n2)}")

else:
    print ("invalid input")
    
# Simple Calculator Program in Python
