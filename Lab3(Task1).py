# Create a queue with 13 elements, including some repeated values
my_queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]

# Insert the string "Qalaisyn?" at index 7
my_queue.insert(7, "Salem")
print("Queue after inserting 'Salem':", my_queue)

# Take the value at index 6
value_to_move = my_queue[6]

# Add this value to the beginning of the queue
my_queue.insert(0, value_to_move)

# Remove the original value (now at index 7 after insertion)
del my_queue[7]

print("Queue after moving value from index 6 to front and deleting original:", my_queue)

# Count the number of repeated values
unique_values = set(my_queue)
repeated_count = len(my_queue) - len(unique_values)
print("Number of repeated values:", repeated_count)

# Sort the queue
sorted_queue = sorted(my_queue, key=lambda x: str(x))  # Sort mixed types safely
print("Sorted queue:", sorted_queue)

# I created 3 lists and put them into a tuple.
# Then I changed the grade of the first subject and printed everything again.


