from typing import Any

class LinkedList:
    def __init__(self) -> None:
        self.__head = None

    def destroy(self) -> None:
        self.__head = None

    def add(self, data: Any) -> None:
        newElement = Element(data)
        if self.__head == None:
            self.__head = newElement
        else:
            newElement._next = self.__head
            self.__head = newElement

    def append(self, data: Any) -> None:
        newElement = Element(data)
        if self.__head == None:
            self.__head = newElement
        else:
            element = self.__head
            while element._next != None:
                element = element._next
            element._next = newElement

    def remove(self) -> None:
        if self.__head != None:
            self.__head = self.__head._next

    def remove_end(self) -> None:
        if self.__head != None:
            element = self.__head
            if element._next == None:
                self.__head = None
            else:
                while element._next._next != None:
                    element = element._next
                element._next = None

    def is_empty(self) -> bool:
        if self.__head == None:
            return True
        else:
            return False
        
    def length(self) -> int:
        element = self.__head
        length = 0
        while element != None:
            element = element._next
            length += 1
        return length
    
    def get(self) -> Any:
        return self.__head._data
    
    def __str__(self) -> str:
        element = self.__head
        string = ''
        if self.__head != None:
            while element != None:
                string += '-> ' + str(element._data) + '\n'
                element = element._next
        return string

class Element:
    def __init__(self, data: Any) -> None:
        self._data = data
        self._next = None
