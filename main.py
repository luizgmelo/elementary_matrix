matrix = [
        [2, 1, 3],
        [4, 2, 2],
        [2, 5, 3],
         ]

def transform_matrix(matrix):
    if matrix == []:
        return []

    # Encontre a primeira coluna não nula (da esquerda para a direita). Esta coluna é chamada de coluna pivô.
    # Na coluna pivô identifique o primeiro elemento (de cima para baixo) não nulo. Este elemento é chamado de elemento pivô.
    pivot_col = None
    pivot = 1
    pivot_line = 0

    for col in range(len(matrix[0])):
        for line in range(len(matrix)):
            if (matrix[line][col] != 0):
                pivot_col = col
                pivot_line = line
                pivot = matrix[line][col]
                break
        if (pivot_col != None):
            break

    if pivot_col == None:
        return
    
    # Se o elemento pivô não pertence à primeira linha então permute a linha que contenha o pivô pela primeira linha.
    if pivot_line != 0:
        row_switching(0, pivot_line, matrix)

    # Multiplique a primeira linha pelo inverso do pivô, para obter na primeira linha da coluna do pivô o elemento 1.
    row_multiplication(0, 1/pivot, matrix)

    # Zerar os elementos da coluna do pivô.
    for line in range(1, len(matrix)):
        below_pivot_element = matrix[line][pivot_col] 
        row_addition(line, 0, below_pivot_element * -1, matrix)
    
    # Seja B a submatriz de A obtida retirando-se a primeira linha de A. Repita os passos 1 a 5 para a matriz B.
    if matrix[1:] != []:
        transform_matrix(matrix[1:])

    # Determine all the leading ones in the row-echelon form obtained
    leading_ones_index = []
    for line in range(len(matrix)-1, -1, -1):
        try:
            lead = matrix[line].index(1)
        except ValueError:
            continue
        leading_ones_index.append(lead)
        for line_above in range(line-1, -1, -1):
            above_pivot_element = matrix[line_above][lead]
            row_addition(line_above, line, -1 * above_pivot_element, matrix)



def row_switching(r1, r2, matrix):
    for col in range(len(matrix[0])):
        matrix[r1][col], matrix[r2][col] = matrix[r2][col], matrix[r1][col]

def row_multiplication(row, k, matrix):
    if k == 0:
        return matrix
    for col in range(len(matrix[row])):
        matrix[row][col] *= k

def row_addition(r1, r2, k, matrix):
    # r1 += kr2
    for i in range(len(matrix[r1])):
        matrix[r1][i] += k * matrix[r2][i]

def print_matrix(matrix):
    print("[")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end="\t")
        print()
    print("]")

transform_matrix(matrix)
