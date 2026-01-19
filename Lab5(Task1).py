def calculate_discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    return d

try:
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    c = float(input("Enter value for c: "))
    d = calculate_discriminant(a, b, c)

    print(f"Equation: {a}x² + {b}x + {c} = 0")
    print(f"Discriminant (D) = {d}")

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f"Two roots: x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"One root: x = {x}")
    else:
        print("No real roots.")

except ValueError:
    print("Invalid input! Please enter numeric values.")

