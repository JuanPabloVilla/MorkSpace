
num1 = float(input("Type one number: "))
num2 = float(input("Type antoher number: "))
operacion = input("What type of operation do you want to do? (+,-,*,/)")

if operacion == "+":
    print(f"resultado: {num1 + num2}")
elif operacion == "-":
    print(f"resultado: {num1 - num2}")
elif operacion == "*":
    print(f"resultado: {num1 * num2}")
elif operacion == "/":
    if num2 != 0:
        print(f"resultado: {num1 / num2}")
    else:
        print("Can't divide by zero")
else:
    print("invalide operation")

num3 = float(input("Write a number to determinate if is negative or positive: "))

if num3 >= 1:
    print("The number is positive")
elif num3 <= -1:
    print("The number is negative")
else:
    print("The number is zero")