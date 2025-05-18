while True:
    num1 = float(input("Type a number: "))
    num2 = float(input("Type a second number: "))
    operation = input("For make an operation or (+ - * /) or 'exit' to exit: ")
    if operation == "exit":
        print("Good bye")
        break
    if operation == "+":
        print(f"The Answer is: {num1 + num2}")
    elif operation == "-":
        print(f"The answer is: {num1 - num2}")
    elif operation == "*":
      print(f"The answer is: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"The answer is: {num1 / num2}")
        else:
            print("Can´t divide 0")
    else:
        print("invalid operation")


