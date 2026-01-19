n = input("Enter the number of Fibonacci numbers: ")  # Asking how many Fibonacci numbers to generate
try:
    n = int(n)
    a, b = 0, 1
    result = []

    for _ in range(n):
        result.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", result)
except ValueError:
    print("Please enter a valid integer!")

