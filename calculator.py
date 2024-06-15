num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

operation = input("Enter type of operation (+,-,*,/,%): ")

if operation == '+':
    sum = num1 + num2
    print(f"Your answer is {sum}")

elif operation == '-':
    sum = num1 - num2
    print(f"Your answer is {sum}")

elif operation == '*':
    sum = num1 * num2
    print(f"Your answer is {sum}")

elif operation == '/':
    sum = num1 / num2
    print(f"Your answer is {sum}")

elif operation == '%':
    sum = num1 % num2
    print(f"Your answer is {sum}")

else:
    print("Wrong data format")
