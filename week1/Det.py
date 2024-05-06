import numpy as np

def input_matrix():
    
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    
    matrix = []

   
    print("Enter the elements of the matrix row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)

    return np.array(matrix)


matrix = input_matrix()


determinant = np.linalg.det(matrix)

print("Determinant of the matrix:")
print(determinant)

