from random import randint

def generate_matrix(rows, cols):
    matrix = [[randint(0, 100) for _ in range(cols)] for _ in range(rows)]
    for row in matrix:
        print(row)
    return matrix

def diagonal_sums(matrix):
    size = min(len(matrix), len(matrix[0]))
    main_diag = sum(matrix[i][i] for i in range(size))
    counter_diag = sum(matrix[i][-(i + 1)] for i in range(size))
    return main_diag, counter_diag

try:
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    m = generate_matrix(r, c)
    main_d, counter_d = diagonal_sums(m)
    print("Main diagonal sum:", main_d)
    print("Counter diagonal sum:", counter_d)
except ValueError:
    print("Please enter valid integers.")

