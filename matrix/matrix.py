from __future__ import annotations
from typing import Union

class Matrix:
    def __init__(self, argument: Union[list[list[float]], tuple[int, int]], elements: float = 0) -> None:
        if(isinstance(argument, tuple)):
            self.__matrix = [[elements for i in range(argument[1])] for j in range(argument[0])]
        else:
            self.__matrix = argument

    def size(self) -> tuple[int, int]:
        return len(self.__matrix), len(self.__matrix[0])
    
    def __add__(self, matrix: Matrix) -> Union[None, Matrix]:
        selfRows, selfCols = self.size()[0], self.size()[1]
        if(selfCols == matrix.size()[1] and selfRows == matrix.size()[0]):
            result = [[0 for i in range(selfCols)] for j in range(selfRows)]
            for i in range(selfRows):
                for j in range(selfCols):
                    result[i][j] = self.__matrix[i][j] + matrix[i][j]
            return Matrix(result)
        else:
            return None

    def __mul__(self, matrix: Matrix) -> Union[None, Matrix]:
        selfRows, selfCols = self.size()[0], self.size()[1]
        matrixRows, matrixCols = matrix.size()[0], matrix.size()[1]
        if(selfCols == matrixRows):
            result = [[0 for i in range(matrixCols)] for j in range(selfRows)]
            for i in range(selfRows):
                for j in range(matrixCols):
                    for k in range(matrixRows):
                        result[i][j] += self.__matrix[i][k] * matrix[k][j]
            return Matrix(result)
        else:
            return None

    def __getitem__(self, index: int) -> Union[list[float], float]:
        return self.__matrix[index]
    
    def __str__(self) -> str:
        string = ''
        for i in range(self.size()[0]):
            string += '|'
            for j in range(self.size()[1]):
                if self.__matrix[i][j] < 0:
                    string += str(self.__matrix[i][j])
                    string += ' '
                else:
                    string += ' '
                    string += str(self.__matrix[i][j])
                    string += ' '
            string += '|\n'
        return string
    
def transpose(matrix: Matrix) -> Matrix:
    rows, cols = matrix.size()[0], matrix.size()[1]
    result = [[0 for i in range(rows)] for j in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return Matrix(result)