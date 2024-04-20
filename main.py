matrix = [
        [2, 1, 3],
        [4, 2, 2],
        [2, 5, 3]
         ]

def row_switching(r1, r2):
    matrix[r1], matrix[r2] = matrix[r2], matrix[r1]

def row_multiplication(row, k):
    if k == 0:
        return
    for col in range(len(matrix[row])):
        matrix[row][col] *= k

def row_addition(r1, r2, k):
    # r1 += kr2
    for i in range(len(matrix[r1])):
        matrix[r1][i] += k * matrix[r2][i]



