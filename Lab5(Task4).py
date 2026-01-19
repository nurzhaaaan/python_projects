def cubes_dict(n):
    return {i: i**3 for i in range(1, n + 1)}

try:
    count = int(input("How many pairs (number:cube) do you want? "))
    print("Resulting dictionary:", cubes_dict(count))
except ValueError:
    print("Enter a valid integer.")

