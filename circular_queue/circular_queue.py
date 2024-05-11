from typing import Any

class Queue:
    def __init__(self) -> None:
        self.__tab = [None for i in range(5)]
        self.__saveIndex = 0
        self.__getIndex = 0
        self.__size = 5

    def is_empty(self) -> bool:
        return self.__saveIndex == self.__getIndex

    def peek(self) -> Any:
        if self.is_empty():
            return None
        else:
            return self.__tab[self.__getIndex]
        
    def dequeue(self) -> Any:
        if self.is_empty():
            return None
        else:
            element = self.__tab[self.__getIndex]
            self.__tab[self.__getIndex] = None
            if self.__getIndex < self.__size - 1:
                self.__getIndex += 1
            else:
                self.__getIndex = 0
            return element

    def enqueue(self, data: Any) -> None:
        self.__tab[self.__saveIndex] = data
        if self.__saveIndex < self.__size - 1:
                self.__saveIndex += 1
        else:
            self.__saveIndex = 0
        if self.is_empty():
            self.__tab = self.__realloc(self.__tab, self.__size * 2)
            length = len(self.__tab) - 1 - (self.__size - 1 - self.__getIndex)
            self.__tab[length:] = self.__tab[self.__getIndex:self.__size]
            for i in range(self.__getIndex, self.__size):
                self.__tab[i] = None
            self.__getIndex = length
            self.__size *= 2

    def __str__(self) -> str:
        string = '['
        i = self.__getIndex
        while i != self.__saveIndex:
            string += str(self.__tab[i]) + ', '
            if i < self.__size - 1:
                i += 1
            else:
                i = 0
        if string != '[':
            string = string[:-2]
        string += ']'
        return string
    
    def getTab(self):
        return self.__tab
    
    def __realloc(self, tab: list[Any], size: int) -> list[Any]:
        oldSize = len(tab)
        return [tab[i] if i < oldSize else None for i in range(size)]