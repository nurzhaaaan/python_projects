# Create a list with different types of values, including duplicates
different = ["бір", "екі", "бір", "1", 1, "5", 1, "1", 123, 321, 123, 321, 90, "Python", "python", "Python", "lecture 4"]

# Convert the list to a set to get only unique values
unique_values = set(different)

# Print number of unique values and the values themselves
print("Бірегей мәндер саны:", len(unique_values))
print("Бірегей мәндер:", unique_values)

# Create two sets of strings
set_a = {"Айбек", "Аружан", "Мирас"}
set_b = {"Мирас", "Жансая", "Нұржан"}

# Combine both sets into a third one (union)
combined_set = set_a.union(set_b)

print("\nБіріктірілген жиын:", combined_set)

# Check if set_a is a subset of combined_set
is_subset = set_a.issubset(combined_set)
print("set_a жиыны combined_set ішкі жиыны ма?", is_subset)

# Create two sets of numbers
numbers1 = {10, 20, 30, 40}
numbers2 = {5, 15, 25, 35}

# Find max and min in each set
print("\nБірінші жиын:", numbers1)
print("Максимум:", max(numbers1))
print("Минимум:", min(numbers1))

print("\nЕкінші жиын:", numbers2)
print("Максимум:", max(numbers2))
print("Минимум:", min(numbers2))

# Find the set with the highest max number
if max(numbers1) > max(numbers2):
    print("\nБірінші жиында ең үлкен мән бар.")
else:
    print("\nЕкінші жиында ең үлкен мән бар.")

