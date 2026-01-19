# Create lists of subjects, grades, and students
subjects = ["Математика", "Физика", "Дене шынықтыру"]
grades = [45, 80, 90]
students = ["Айбек", "Аружан", "Мирас"]

# Create a tuple from the lists
my_tuple = (subjects, grades, students)

# Print a table
print("Пән атауы             | Баға     | Студент")
print("-----------------------------------------------")
for i in range(len(subjects)):
    print(f"{subjects[i]:<22} {grades[i]:<9} {students[i]}")

# Change Math grade from 45 to 55
grades[0] = 55

# Print updated table
print("\nЖаңартылған кесте:")
print("Пән атауы             | Баға     | Студент")
print("-----------------------------------------------")
for i in range(len(subjects)):
    print(f"{subjects[i]:<22} {grades[i]:<9} {students[i]}")

# Tuple is immutable, but we can simulate deleting by creating a new tuple
new_subjects = subjects[1:]      # remove first subject
new_grades = grades[1:]          # remove first grade
new_students = students[1:]      # remove first student

new_tuple = (new_subjects, new_grades, new_students)

# Print the new tuple
print("\nЖаңа кортеж (бір студент пен пәнді алып тастадық):")
print(new_tuple)

