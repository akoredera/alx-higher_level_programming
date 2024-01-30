def matrix_divided(matrix, div):
    if type(matrix) is not [[int]] or type(matrix) is not [[float]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            if j != i[j]
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[-1]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div mist be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return round(matrix / div, 2)
