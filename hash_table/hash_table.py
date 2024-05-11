from __future__ import annotations
from typing import Union, Any

class HashTable:
    def __init__(self, size: int, c1: int = 1, c2: int = 0) -> None:
        self.__tab = [None for i in range(size)]
        self.__size = size
        self.__c1 = c1
        self.__c2 = c2

    def hash(self, key: Union[int, str]) -> int:
        if isinstance(key, str):
            sum = 0
            for i in key:
                sum += ord(i)
            return sum % self.__size
        else:
            return key % self.__size
        
    def makeIndex(self, key: Union[int, str], i: int) -> int:
        k = self.hash(key)
        return (k + self.__c1 * i + self.__c2 * i**2) % self.__size
            
    def search(self, key: Union[int, str]) -> Any:
        for i in range(self.__size):
            index = self.makeIndex(key, i)
            if self.__tab[index] is not None:
                if self.__tab[index]._key == key and not self.__tab[index]._isDeleted:
                    return self.__tab[index]._value
        return None
        
    def insert(self, key: Union[int, str], value: Any) -> None:
        for i in range(self.__size):
            index = self.makeIndex(key, i)
            if self.__tab[index] is None or self.__tab[index]._isDeleted:
                self.__tab[index] = Element(key, value)
                return
            if self.__tab[index]._key is key:
                self.__tab[index]._value = value
                return
        print("Not enough space.")
        return None
        
    def remove(self, key: Union[int, str]) -> None:
        for i in range(self.__size):
            index = self.makeIndex(key, i)
            if self.__tab[index] is not None and not self.__tab[index]._isDeleted and self.__tab[index]._key == key:
                self.__tab[index]._isDeleted = True
                return
        print("There is no data with that key.")
        return None
        
    def __str__(self) -> str:
        string = "{"
        for i in self.__tab:
            string += f"{i}, "
        if string != '{':
            string = string[:-2]
        string += "}"
        return string   
            
class Element:
    def __init__(self, key: Union[int, str], value: Any) -> None:
        self._key = key
        self._value = value
        self._isDeleted = False

    def __eq__(self, other: Element) -> bool:
        return self._key == other._key
    
    def __str__(self) -> str:
        if self._isDeleted:
            return 'None'
        else:
            return f"{self._key}:{self._value}"
