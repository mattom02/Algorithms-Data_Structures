from __future__ import annotations
from typing import Any, Union

class Element:
    def __init__(self, value: Any, priority: int) -> None:
        self.__dane = value
        self.__priorytet = priority

    def __It__(self, other: Element) -> bool:
        return self.__priorytet < other.__priorytet
    
    def __gt__(self, other: Element) -> bool:
        return self.__priorytet > other.__priorytet
    
    def __repr__(self) -> str:
        return f"{self.__priorytet} : {self.__dane}"

class Queue:
    def __init__(self) -> None:
        self.__tab = []
        self.__size = 0

    def parent(self, index: int) -> int:
        return (index - 1) // 2
    
    def left(self, index: int) -> int:
        return (index * 2) + 1
    
    def right(self, index: int) -> int:
        return (index * 2) + 2

    def is_empty(self) -> bool:
        return self.__size == 0
    
    def peek(self) -> Union[None, Any]:
        if self.is_empty():
            return None
        else:
            return self.__tab[0]
        
    def repair(self, i: int) -> None:
        if self.__tab[i] is not None:
            left = self.left(i)
            right = self.right(i)
            if left < self.__size and right < self.__size:
                if self.__tab[left] > self.__tab[i] and self.__tab[left] > self.__tab[right]:
                    self.__tab[left], self.__tab[i] = self.__tab[i], self.__tab[left]
                    self.repair(left)
                elif self.__tab[right] > self.__tab[i] and self.__tab[right] > self.__tab[left]:
                    self.__tab[right], self.__tab[i] = self.__tab[i], self.__tab[right]
                    self.repair(right)
                elif self.__tab[right] > self.__tab[i] and self.__tab[left] > self.__tab[i]:
                    self.__tab[right], self.__tab[i] = self.__tab[i], self.__tab[right]
                    self.repair(right)
            elif left < self.__size and right >= self.__size:
                if self.__tab[left] > self.__tab[i]:
                    self.__tab[left], self.__tab[i] = self.__tab[i], self.__tab[left]
                    self.repair(left)
            elif right < self.__size and left >= self.__size:
                if self.__tab[right] > self.__tab[i]:
                    self.__tab[right], self.__tab[i] = self.__tab[i], self.__tab[right]
                    self.repair(right)

    def dequeue(self) -> Union[Element, None]:
        if self.is_empty():
            return None
        else:
            result = self.__tab[0]
            self.__tab[0] = self.__tab[self.__size-1]
            self.__tab[self.__size-1] = None
            self.__size -= 1
            self.repair(0)
            return result
        
    def enqueue(self, element: Element) -> None:
        if len(self.__tab) == 0:
            self.__tab.append(element)
            self.__size += 1
        elif len(self.__tab) == self.__size:
            self.__tab.append(element)
            self.__size += 1
            current = self.__size - 1
            while current > 0 and self.__tab[current] > self.__tab[self.parent(current)]:
                self.__tab[current], self.__tab[self.parent(current)] = self.__tab[self.parent(current)], self.__tab[current]
                current = self.parent(current)
        elif self.__size < len(self.__tab):
            self.__tab[self.__size] = element
            self.__size += 1
            current = self.__size - 1
            while current > 0 and self.__tab[current] > self.__tab[self.parent(current)]:
                self.__tab[current], self.__tab[self.parent(current)] = self.__tab[self.parent(current)], self.__tab[current]
                current = self.parent(current)

    def print_tab(self) -> None:
        print('{', end=' ')
        print(*self.__tab[:self.__size], sep=', ', end = ' ')
        print('}')

    def print_tree(self, idx: int, lvl: int) -> None:
        if idx < self.__size:           
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.__tab[idx] if self.__tab[idx] else None)           
            self.print_tree(self.left(idx), lvl + 1)
    