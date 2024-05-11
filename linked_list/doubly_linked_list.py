from typing import Any

class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None

    def destroy(self) -> None:
        element = self.__head
        while element != None:
            temp = element._next
            element._prev = None
            element = None
            element = temp
        self.__head = None
        self.__tail = None

    def add(self, data: Any) -> None:
        newElement = Element(data)
        if self.__head == None:
            self.__head = newElement
            self.__tail = self.__head
        else:
            newElement._next = self.__head
            newElement._next._prev = newElement
            self.__head = newElement


    def append(self, data: Any) -> None:
        newElement = Element(data)
        if self.__head == None:
            self.__head = newElement
            self.__tail = self.__head
        else:
            newElement._prev = self.__tail
            self.__tail._next = newElement
            self.__tail = newElement

    def remove(self) -> None:
        if self.__head != None:
            self.__head = self.__head._next
            self.__head._prev = None

    def remove_end(self) -> None:
        if self.__head != None:
            if self.__head._next == None:
                self.__head = None
                self.__tail = None
            else:
                self.__tail._prev._next = None
                self.__tail = self.__tail._prev

    def is_empty(self) -> bool:
        if self.__head == None and self.__tail == None:
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
        self._prev = None
