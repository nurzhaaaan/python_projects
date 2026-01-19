def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            print("Error: Unknown operation!")
            return

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers!")

calculator()
