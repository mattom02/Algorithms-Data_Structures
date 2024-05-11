from matrix import Matrix

def chio(matrix: Matrix, n: int = 0, multiplier: float = 1) -> float:
    n = matrix.size()[0]
    if n > 2:
        newMatrix = [[0 for i in range(n - 1)] for i in range(n - 1)]
        swappedMatrix = [i[:] for i in matrix]
        if matrix[0][0] == 0:
            for i in range(1,n):
                if matrix[0][i] != 0:
                    for j in range(n):
                        swappedMatrix[j][0], swappedMatrix[j][i] = swappedMatrix[j][i], swappedMatrix[j][0]
                    multiplier *= -1
                    break
        for i in range(n - 1):
            for j in range(n - 1):
                    newMatrix[i][j] = swappedMatrix[0][0] * swappedMatrix[i + 1][j + 1] - swappedMatrix[0][j + 1] * swappedMatrix[i + 1][0]
        multiplier *= 1/(swappedMatrix[0][0]**(n-2))
        return chio(Matrix(newMatrix), n, multiplier)
    else:
        return ((matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])) * multiplier
    