# ---------- Task 3 – Numbers (WITHOUT sys module) ----------

#  We enter the maximum integer manually
max_int = 9223372036854775807
print("Maximum integer value (64-bit):", max_int)

# We ask the user for an integer between 100 and 999
num = int(input("Enter a number between 100 and 999: "))
if 100 <= num <= 999:
    a = num // 100
    b = (num // 10) % 10
    c = num % 10
    digit_sum = a + b + c
    digit_mul = 1
    for d in (a, b, c):
        if d != 0:
            digit_mul *= d
    print("Sum:", digit_sum)
    print("Multiplication (excluding 0):", digit_mul)
else:
    print("Number is not in the range.")

# Convert between Celsius and Fahrenheit
print("Choose conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter 1 or 2: ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    f = c * 9/5 + 32
    print("Temperature in Fahrenheit:", f)
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) / 1.8
    print("Temperature in Celsius:", c)
else:
    print("Invalid choice.")


