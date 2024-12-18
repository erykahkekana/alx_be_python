#!/usr/bin/env python3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        sum = num1 + num2
        print(f"The result is {sum}.")
    case "-":
        difference = num1 - num2
        print(f"The result is {difference}.")
    case "*":
        product = num1 * num2
        print(f"The result is {product}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            quotient = num1 / num2
            print(f"The result is {quotient}.")
