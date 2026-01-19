numbers = []

while True:
    num = input("Enter a number (type 'no' to stop): ")  # Prompting user to enter a number or stop
    if num.lower() == 'no':
        break
    try:
        num = int(num)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number!")

if numbers:
    total = 0
    product = 1
    even = 0
    odd = 0
    max_num = numbers[0]

    for n in numbers:
        total += n
        product *= n
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        if n > max_num:
            max_num = n

    print("Sum of numbers:", total)
    print("Product of numbers:", product)
    print("Even numbers count:", even)
    print("Odd numbers count:", odd)
    print("Highest number:", max_num)
else:
    print("No numbers were entered.")

