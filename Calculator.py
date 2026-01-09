# Simple Calculator

print("Simple Calculator")
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = input("Enter choice (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == "1":
    result = num1 + num2
    print(num1 ,"+", num2, "=", result)

elif operation == "2":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

elif operation == "3":
    result = num1 * num2
    print(num1,"*", num2,"=", result)

elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        print(num1,"/", num2, "=", result)
    else:
        print("Error: Division by zero")

else:
    print("Invalid choice")
