stepCount = 1

def printStep(text, matrix):
    global stepCount
    print(f"Step {stepCount}: {text}")
    print_matrix(matrix)
    stepCount += 1
    print("-" * 60)
#=======================================================================================================================
def user_input():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    matrix = []
    print("Enter the entries rowwise: (type a number and press enter)")

    if R == 0 and C == 0:
        return []

    for i in range(R):
        row=[]
        for j in range(C):
            row.append(int(input()))
        matrix.append(row)

    return matrix
#=======================================================================================================================
def transform_matrix(matrix):
    for row in range(len(matrix)):
        # Encontre a primeira coluna não nula (da esquerda para a direita). Esta coluna é chamada de coluna pivô.
        # Na coluna pivô identifique o primeiro elemento (de cima para baixo) não nulo. Este elemento é chamado de elemento pivô.
        pivot_col = None
        pivot = 1
        pivot_line = 0

        for col in range(row, len(matrix[0])):
            for line in range(row, len(matrix)):
                if (matrix[line][col] != 0):
                    pivot_col = col
                    pivot_line = line
                    pivot = matrix[line][col]
                    break
            if (pivot_col != None):
                break

        if pivot_col == None:
           break 
        
        # Se o elemento pivô não pertence à primeira linha então permute a linha que contenha o pivô pela primeira linha.
        if pivot_line != 0:
            row_switching(row, pivot_line, matrix)

        # Multiplique a primeira linha pelo inverso do pivô, para obter na primeira linha da coluna do pivô o elemento 1.
        if pivot != 1:
            row_multiplication(row, 1/pivot, matrix)

        # Zerar os elementos da coluna do pivô que estão abaixo dele.
        for line in range(row+1, len(matrix)):
            below_pivot_element = matrix[line][pivot_col] 
            if below_pivot_element != 0:
                row_addition(line, row, below_pivot_element * -1, matrix)

        # Zerar os elementos da coluna do pivô que estão acima dele.
        for line in range(row-1, -1, -1):
            above_pivot_element = matrix[line][pivot_col]
            if above_pivot_element != 0:
                row_addition(line, row, above_pivot_element * -1, matrix)
#=======================================================================================================================
def row_switching(r1, r2, matrix):
    for col in range(len(matrix[0])):
        matrix[r1][col], matrix[r2][col] = matrix[r2][col], matrix[r1][col]
    
    printStep(f"Switching row {r1 + 1} with row {r2 + 1}.", matrix)
#=======================================================================================================================
def row_multiplication(row, k, matrix):
    if k == 0:
        return matrix
    for col in range(len(matrix[row])):
        matrix[row][col] *= k
    
    printStep(f"Multiplicating row {row + 1} by {k}.", matrix)
#=======================================================================================================================
def row_addition(r1, r2, k, matrix):
    for i in range(len(matrix[r1])):
        matrix[r1][i] += k * matrix[r2][i]
    
    printStep(f"Adding the product between row {r2 + 1} and {k} to row {r1 + 1}.", matrix)
#=======================================================================================================================
def print_matrix(matrix):
    # Find the maximum width of the numbers in each column
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*matrix)]
    
    # Print the matrix with walls and value alignment.
    print("")
    for row in matrix:
        print("| " + " | ".join(f"{str(cell).rjust(col_widths[i])}" for i, cell in enumerate(row)) + " |")
    print("")
#=======================================================================================================================
if __name__ == "__main__":
    while(True):
        stepCount = 1
        print("="*30)
        print("Welcome, create your matrix")
        print("="*30)
        matrix = user_input()
        
        print("This is your matrix:")
        print_matrix(matrix)
        print("-" * 60)
        
        transform_matrix(matrix)
        print("Row reduce echelon form:")
        print_matrix(matrix)
        
        print("=" * 60)
        
        option = "_"
        while (option not in "YyNn"):
            option = str(input("Continue? (Y/N)"))

        if (option in "Nn"):
            break
#=======================================================================================================================
